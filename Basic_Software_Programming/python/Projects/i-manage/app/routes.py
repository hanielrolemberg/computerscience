# Defining the Routes and Views


# /app/routes.py
from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from . import db, bcrypt
from .models import User, Goal
from .forms import RegistrationForm, LoginForm, GoalForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    goals = Goal.query.filter_by(author=current_user)
    return render_template('dashboard.html', goals=goals)

@main.route('/goal/new', methods=['GET', 'POST'])
@login_required
def new_goal():
    form = GoalForm()
    if form.validate_on_submit():
        goal = Goal(title=form.title.data, description=form.description.data, author=current_user)
        db.session.add(goal)
        db.session.commit()
        flash('Your goal has been created!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('create_goal.html', title='New Goal', form=form)

@main.route('/goal/<int:goal_id>/update', methods=['GET', 'POST'])
@login_required
def update_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    if goal.author != current_user:
        abort(403)
    form = GoalForm()
    if form.validate_on_submit():
        goal.title = form.title.data
        goal.description = form.description.data
        db.session.commit()
        flash('Your goal has been updated!', 'success')
        return redirect(url_for('main.dashboard'))
    elif request.method == 'GET':
        form.title.data = goal.title
        form.description.data = goal.description
    return render_template('create_goal.html', title='Update Goal', form=form)

@main.route('/goal/<int:goal_id>/delete', methods=['POST'])
@login_required
def delete_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    if goal.author != current_user:
        abort(403)
    db.session.delete(goal)
    db.session.commit()
    flash('Your goal has been deleted!', 'success')
    return redirect(url_for('main.dashboard'))