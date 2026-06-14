from datetime import date, datetime, timedelta

from flask import Flask, abort, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from config import Config
from extensions import csrf, db, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    login_manager.login_view = "login"
    login_manager.login_message_category = "info"

    with app.app_context():
        from models import Task, User

        db.create_all()

    register_routes(app)
    register_template_helpers(app)
    return app


def register_template_helpers(app):
    @app.context_processor
    def inject_globals():
        return {
            "today": date.today(),
            "timedelta": timedelta,
            "current_year": datetime.now().year,
        }


def get_user_task(task_id):
    from models import Task

    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        abort(404)
    return task


def task_stats(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task.completed)
    pending = total - completed
    overdue = sum(1 for task in tasks if task.is_overdue)
    progress = round((completed / total) * 100) if total else 0
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue,
        "progress": progress,
    }


def register_routes(app):
    from forms import LoginForm, PasswordForm, ProfileForm, RegisterForm, TaskForm
    from models import Task, User

    @app.route("/")
    def index():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        return redirect(url_for("login"))

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        form = RegisterForm()
        if form.validate_on_submit():
            user = User(
                fullname=form.fullname.data.strip(),
                email=form.email.data.lower().strip(),
                username=form.username.data.strip(),
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Welcome to TaskFlow. Your workspace is ready.", "success")
            return redirect(url_for("dashboard"))
        return render_template("register.html", form=form, auth_page=True)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data.lower().strip()).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember.data)
                flash("Login successful. Good to see you again.", "success")
                next_page = request.args.get("next")
                return redirect(next_page or url_for("dashboard"))
            flash("Invalid email or password.", "danger")
        return render_template("login.html", form=form, auth_page=True)

    @app.route("/logout", methods=["POST"])
    @login_required
    def logout():
        logout_user()
        flash("You have been logged out.", "info")
        return redirect(url_for("login"))

    @app.route("/dashboard")
    @login_required
    def dashboard():
        tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.sort_order.asc(), Task.due_date.asc()).all()
        stats = task_stats(tasks)
        upcoming = [task for task in tasks if not task.completed and task.due_date >= date.today()][:5]
        overdue = [task for task in tasks if task.is_overdue][:5]
        categories = sorted({task.category for task in tasks}) or ["Study", "Assignment", "Project", "Exam", "Personal"]
        return render_template("dashboard.html", tasks=tasks[:8], stats=stats, upcoming=upcoming, overdue=overdue, categories=categories)

    @app.route("/tasks")
    @login_required
    def tasks():
        page = request.args.get("page", 1, type=int)
        query = Task.query.filter_by(user_id=current_user.id).order_by(Task.completed.asc(), Task.sort_order.asc(), Task.due_date.asc())
        pagination = query.paginate(page=page, per_page=8, error_out=False)
        all_tasks = Task.query.filter_by(user_id=current_user.id).all()
        categories = sorted({task.category for task in all_tasks}) or ["Study", "Assignment", "Project", "Exam", "Personal"]
        stats = task_stats(all_tasks)
        return render_template("tasks.html", tasks=pagination.items, pagination=pagination, categories=categories, stats=stats)

    @app.route("/tasks/add", methods=["GET", "POST"])
    @login_required
    def add_task():
        form = TaskForm()
        if request.method == "GET" and not form.category.data:
            form.category.data = request.args.get("category", "Study")
        if form.validate_on_submit():
            max_order = db.session.query(db.func.max(Task.sort_order)).filter_by(user_id=current_user.id).scalar() or 0
            task = Task(
                title=form.title.data.strip(),
                description=form.description.data.strip() if form.description.data else "",
                priority=form.priority.data,
                category=form.category.data.strip(),
                due_date=form.due_date.data,
                sort_order=max_order + 1,
                owner=current_user,
            )
            db.session.add(task)
            db.session.commit()
            flash("Task created.", "success")
            return redirect(url_for("tasks"))
        return render_template("add_task.html", form=form)

    @app.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
    @login_required
    def edit_task(task_id):
        task = get_user_task(task_id)
        form = TaskForm(obj=task)
        if form.validate_on_submit():
            task.title = form.title.data.strip()
            task.description = form.description.data.strip() if form.description.data else ""
            task.priority = form.priority.data
            task.category = form.category.data.strip()
            task.due_date = form.due_date.data
            db.session.commit()
            flash("Task updated.", "success")
            return redirect(url_for("tasks"))
        return render_template("edit_task.html", form=form, task=task)

    @app.route("/tasks/<int:task_id>/delete", methods=["POST"])
    @login_required
    def delete_task(task_id):
        task = get_user_task(task_id)
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted.", "warning")
        return redirect(url_for("tasks"))

    @app.route("/tasks/<int:task_id>/toggle", methods=["POST"])
    @login_required
    def toggle_task(task_id):
        task = get_user_task(task_id)
        task.completed = not task.completed
        db.session.commit()
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"completed": task.completed, "message": "Task status updated."})
        flash("Task status updated.", "success")
        return redirect(request.referrer or url_for("tasks"))

    @app.route("/tasks/reorder", methods=["POST"])
    @login_required
    def reorder_tasks():
        payload = request.get_json(silent=True) or {}
        ids = payload.get("ids", [])
        tasks_by_id = {
            task.id: task
            for task in Task.query.filter(Task.user_id == current_user.id, Task.id.in_(ids)).all()
        }
        for index, task_id in enumerate(ids):
            task = tasks_by_id.get(int(task_id))
            if task:
                task.sort_order = index
        db.session.commit()
        return jsonify({"message": "Order saved."})

    @app.route("/calendar")
    @login_required
    def calendar():
        tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.due_date.asc()).all()
        start = date.today()
        end = start + timedelta(days=30)
        window_tasks = [task for task in tasks if task.due_date <= end]
        return render_template("calendar.html", tasks=tasks, window_tasks=window_tasks)

    @app.route("/profile", methods=["GET", "POST"])
    @login_required
    def profile():
        profile_form = ProfileForm(obj=current_user)
        password_form = PasswordForm()

        if request.method == "POST" and "update_profile" in request.form and profile_form.validate_on_submit():
            email = profile_form.email.data.lower().strip()
            username = profile_form.username.data.strip()
            email_exists = User.query.filter(User.email == email, User.id != current_user.id).first()
            username_exists = User.query.filter(User.username == username, User.id != current_user.id).first()
            if email_exists:
                flash("That email is already used by another account.", "danger")
            elif username_exists:
                flash("That username is already used by another account.", "danger")
            else:
                current_user.fullname = profile_form.fullname.data.strip()
                current_user.email = email
                current_user.username = username
                db.session.commit()
                flash("Profile updated.", "success")
                return redirect(url_for("profile"))

        if request.method == "POST" and "change_password" in request.form and password_form.validate_on_submit():
            if not current_user.check_password(password_form.current_password.data):
                flash("Current password is incorrect.", "danger")
            else:
                current_user.set_password(password_form.new_password.data)
                db.session.commit()
                flash("Password changed.", "success")
                return redirect(url_for("profile"))

        return render_template("profile.html", profile_form=profile_form, password_form=password_form)


app = create_app()


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
