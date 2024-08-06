# Task Manager

This is a simple task manager application built with Flask, MySQL, and Redis. The application allows you to create, update, and delete tasks, as well as mark them as completed.

## Features

- Create new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- Store tasks in MySQL database
- Cache tasks with Redis for improved performance

## Requirements

- Python (Flask)
- MySQL
- **Redis**

## Visual Architecture:
(Layered Architecture)

```LUA
+-------------------+
|                   | 
|        User       | - Presentation Layer
+---------+---------+
          |
          v
+---------+---------+
|     Flask App     | - Application 
|                   |
|                   |
+---------+---------+
          |
    +-----+-----+
    |           |
    v           v
+---------+   +---------+
|  MySQL  |   |  Redis  |
|         |   | (Cache) |   - Data and Cache
|         |   +---------+
+---------+


```
## Data Flow

1. User Request: The user makes a request to the Flask App (for example, to view the list of tasks).

2. Redis Cache: The Flask App checks if the result is in the Redis cache. If it is, it returns the result directly.
3. MySQL Database: If the result is not in the cache, the Flask App queries the MySQL database.
4. Cache Storage: The result from the MySQL query is stored in Redis for future requests.
5. User Response: The Flask App sends the response to the user's browser, which displays the information.


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/task-manager.git
    cd task-manager
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the MySQL database:

    ```sql
    CREATE DATABASE task_manager;
    USE task_manager;

    CREATE TABLE tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    );
    ```

5. Configure the application settings in `config.py`:

    ```python
    import os

    class Config:
        SECRET_KEY = os.urandom(24)
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD = 'teste'
        MYSQL_DB = 'task_manager'
        MYSQL_CURSORCLASS = 'DictCursor'
        REDIS_URL = "redis://localhost:6379/0"
    ```

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://localhost:5000`.

## Project Structure

```plaintext
task_manager/
│
├── app.py
├── config.py
├── requirements.txt
└── templates/
    ├── index.html
    ├── add_task.html
    ├── update_task.html
```

## Notes
app.py: The main application file.
config.py: Configuration file for the application.
requirements.txt: List of required Python packages.
templates/: Directory containing HTML templates.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.


## License
This project is licensed under the MIT License.