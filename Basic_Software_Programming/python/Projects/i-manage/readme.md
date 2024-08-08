# Life Management System

The Life Management System is a web application designed to help users manage their goals and track their progress. It is built using Python, Flask, and MySQL, and includes user authentication, goal management, and a dashboard to view and manage goals.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Topics in Computer Science](#topics-in-computer-science)
- [Project Structure](#project-structure)
- [Usage](#usage)

## Features
- User Authentication (Registration and Login)
- Goal Management (Create, Read, Update, Delete goals)
- Dashboard to view goals

## Technologies Used
- Python
- Flask
- MySQL
- SQLAlchemy
- Flask-WTF
- Flask-Bcrypt
- Flask-Login

## Setup Instructions

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/life_management_system.git
    cd life_management_system
    ```

2. **Set up a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the application**
    - Rename `config.py.example` to `config.py`
    - Update the `SQLALCHEMY_DATABASE_URI` in `config.py` with your MySQL database credentials

5. **Initialize the database**
    ```sh
    flask db init
    flask db migrate -m "initial migration"
    flask db upgrade
    ```

6. **Run the application**
    ```sh
    python run.py
    ```

7. **Open your browser and navigate to**
    ```
    http://localhost:5000
    ```

## Topics in Computer Science

This project touches on several important topics in computer science:

- **Web Development:** Building web applications using Flask.
- **Database Management:** Using MySQL to store and manage application data.
- **ORM (Object-Relational Mapping):** Using SQLAlchemy to interact with the database in an object-oriented way.
- **Authentication and Authorization:** Implementing user authentication and protecting routes.
- **Forms and Data Validation:** Using Flask-WTF for form handling and data validation.
- **HTTP and RESTful APIs:** Understanding and implementing RESTful principles in web development.
- **MVC Architecture:** Structuring the application using the Model-View-Controller pattern.

## Project Structure

/life_management_system
    /app
        __init__.py
        models.py
        routes.py
        /templates
            index.html
            login.html
            register.html
            dashboard.html
    /migrations
    /static
        /css
            styles.css
    config.py
    run.py


## Usage

- **Register a new user:** Create an account by providing a username, email, and password.
- **Login:** Access your account using your email and password.
- **Dashboard:** View your existing goals and manage them.
- **Create a new goal:** Add new goals to your list.
- **Update a goal:** Edit the details of an existing goal.
- **Delete a goal:** Remove a goal from your list.

## Contribution

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
