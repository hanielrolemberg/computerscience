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

- **User Authentication and Authorization**
User Registration: Allows new users to sign up for the application.
Login: Allows users to authenticate and start a session.
Logout: Allows users to sign out of the application.
Switch User: Allows the current user to log out and log in with another account.

- **Goal Management**
Create New Goal: Allows users to create new goals.
Update Goal: Allows users to update details of an existing goal.
Delete Goal: Allows users to delete an existing goal.
View Goals: Displays a list of goals associated with the current user on the dashboard.

- **Navigation**
Dashboard: The main page after login, where users can view and manage their goals.
Home (Index): The landing page of the site with links to login and register.
Navigation Links: Added links for creating a new goal, switching users, and logging out on the dashboard.

- **User Feedback**
Success and Error Messages: Uses Flask's messaging system to inform the user about the status of their actions (e.g., successful login, failed login, goal created successfully).

- **Templates and Rendering**
HTML Templates: Uses Jinja2 to render dynamic HTML templates for different pages (login, registration, dashboard, etc.).

- **Security**
Encrypted Passwords: User passwords are encrypted using bcrypt.
Access Authorization: Access to protected pages is restricted to authenticated users (e.g., dashboard and goal management).



## Technologies Used
- Here's a list of the technologies used in my Flask project:

1. Programming Language
Python: The main programming language used for backend development.
2. Web Framework
Flask: The web framework used for building the web application.
3. Templating Engine
Jinja2: The templating engine used for rendering HTML templates.
4. Database
SQLAlchemy: The ORM (Object-Relational Mapping) library used for database interactions.
MySQL: The database system used for storing user and goal data.
5. Password Encryption
bcrypt: The library used for hashing and verifying passwords.
6. User Authentication
Flask-Login: The extension used for managing user sessions and authentication.
7. Form Handling
Flask-WTF: An extension used for handling web forms and validation.
8. Development Tools
VSCode: The code editor used for development.
Git: The version control system used for managing source code.
9. Dependency Management
pip: The package installer used for managing Python libraries.
venv: The virtual environment tool used to create isolated Python environments.
10. Web Server
Werkzeug: The WSGI server used by Flask for serving the application during development.
11. Project Management
GitHub: The platform used for hosting the project's code repository and version control.

## Setup Instructions

1. **Clone the repository**
    ```sh
    git clone https://github.com/hanielrolemberg/computerscience/tree/master/Basic_Software_Programming/python/Projects/i-manage
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
