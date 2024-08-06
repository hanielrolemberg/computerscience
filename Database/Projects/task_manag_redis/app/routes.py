from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from . import db
from .models import Task, Sprint, Goal

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()
    sprints = Sprint.query.all()
    goals = Goal.query.all()
    return render_template('index.html', tasks=tasks, sprints=sprints, goals=goals)

@main.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    sprint_id = request.form.get('sprint_id')

    if not title or not description or not sprint_id:
        flash('Please fill in all fields.', 'warning')
        return redirect(url_for('main.index'))

    new_task = Task(title=title, description=description, sprint_id=sprint_id)
    db.session.add(new_task)
    db.session.commit()
    flash('Task added successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/add_sprint', methods=['POST'])
def add_sprint():
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    if not start_date or not end_date:
        flash('Please fill in all fields.', 'warning')
        return redirect(url_for('main.index'))

    new_sprint = Sprint(start_date=start_date, end_date=end_date)
    db.session.add(new_sprint)
    db.session.commit()
    flash('Sprint added successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/add_goal', methods=['POST'])
def add_goal():
    name = request.form.get('name')
    description = request.form.get('description')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    if not name or not description or not start_date or not end_date:
        flash('Please fill in all fields.', 'warning')
        return redirect(url_for('main.index'))

    new_goal = Goal(name=name, description=description, start_date=start_date, end_date=end_date)
    db.session.add(new_goal)
    db.session.commit()
    flash('Goal added successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.complete = not task.complete
    db.session.commit()
    flash('Task status updated!', 'success')
    return redirect(url_for('main.index'))

@main.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/assign_task_to_goal', methods=['POST'])
def assign_task_to_goal():
    task_id = request.form.get('task_id')
    goal_id = request.form.get('goal_id')

    if not task_id or not goal_id:
        flash('Task ID and Goal ID are required.', 'warning')
        return redirect(url_for('main.index'))

    task = Task.query.get_or_404(task_id)
    goal = Goal.query.get_or_404(goal_id)
    
    if task in goal.tasks:
        flash('Task is already assigned to this goal.', 'info')
    else:
        goal.tasks.append(task)
        db.session.commit()
        flash('Task assigned to goal successfully!', 'success')

    return redirect(url_for('main.index'))

@main.route('/toggle_status/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    task = Task.query.get_or_404(task_id)
    task.complete = not task.complete
    db.session.commit()
    return jsonify({'task_id': task.id, 'status': 'complete' if task.complete else 'incomplete'})
