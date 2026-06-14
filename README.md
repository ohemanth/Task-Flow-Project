# TaskFlow

TaskFlow is a modern Student Task Management System built with Flask, SQLAlchemy, Flask-Login, Bootstrap 5, Font Awesome, and a dark-first premium UI.

## Features

- User registration, login, logout, password hashing, protected routes, and CSRF protection
- Dashboard statistics for total, completed, pending, and overdue tasks
- Create, edit, delete, reorder, and complete tasks
- Search and filter tasks by title, category, priority, and status without page reloads
- Custom categories with starter examples like Study, Assignment, Project, Exam, and Personal
- Calendar view for upcoming deadlines, today's tasks, and overdue tasks
- Profile editing and password changes
- Toast notifications, responsive sidebar, animated loading screen, keyboard shortcuts, pagination, and theme switching

## Setup

```bash
python -m pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

## Keyboard Shortcuts

- `n`: create a new task
- `/`: focus task search on the tasks page

## Project Structure

```text
student-task-manager/
├── app.py
├── requirements.txt
├── models.py
├── forms.py
├── config.py
├── extensions.py
├── instance/
│   └── database.db
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
└── templates/
    ├── base.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── tasks.html
    ├── add_task.html
    ├── edit_task.html
    ├── calendar.html
    └── profile.html
```

## Notes

The SQLite database is created automatically in `instance/database.db` when the app starts.
