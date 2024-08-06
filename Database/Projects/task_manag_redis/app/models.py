from . import db  # Use a instância de db que já foi criada

class Sprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    tasks = db.relationship('Task', backref='sprint', lazy=True)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    tasks = db.relationship('Task', backref='goal', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    complete = db.Column(db.Boolean, default=False)
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprint.id'), nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.id'), nullable=True)
