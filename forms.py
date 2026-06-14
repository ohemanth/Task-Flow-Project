from datetime import date

from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, PasswordField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, ValidationError

from models import User


class RegisterForm(FlaskForm):
    fullname = StringField("Full Name", validators=[DataRequired(), Length(min=2, max=120)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=160)])
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, message="Use at least 8 characters.")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Create account")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data.lower().strip()).first():
            raise ValidationError("That email is already registered.")

    def validate_username(self, username):
        if User.query.filter_by(username=username.data.strip()).first():
            raise ValidationError("That username is already taken.")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Keep me signed in")
    submit = SubmitField("Sign in")


class TaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2, max=180)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=1500)])
    priority = SelectField("Priority", choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")], validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired(), Length(min=2, max=80)])
    due_date = DateField("Due Date", validators=[DataRequired()], default=date.today)
    submit = SubmitField("Save task")


class ProfileForm(FlaskForm):
    fullname = StringField("Full Name", validators=[DataRequired(), Length(min=2, max=120)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=160)])
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField("Update profile")


class PasswordForm(FlaskForm):
    current_password = PasswordField("Current Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("new_password")])
    submit = SubmitField("Change password")
