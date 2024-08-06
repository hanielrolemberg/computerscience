from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import redis

app = Flask(__name__)
app.config.from_object('config.Config')

mysql = MySQL(app)
cache = redis.StrictRedis.from_url(app.config['REDIS_URL'])

@app.route('/')
def index():
    cached_tasks = cache.get('tasks')
    if cached_tasks:
        tasks = eval(cached_tasks)
    else:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cache.set('tasks', str(tasks))

    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
        mysql.connection.commit()
        cache.delete('tasks')
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        cursor.execute("UPDATE tasks SET title=%s, description=%s, status=%s WHERE id=%s", (title, description, status, id))
        mysql.connection.commit()
        cache.delete('tasks')
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM tasks WHERE id=%s", (id,))
    task = cursor.fetchone()
    return render_template('update_task.html', task=task)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    mysql.connection.commit()
    cache.delete('tasks')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


