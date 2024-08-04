# Flask CRUD API

This project is an example of a RESTful API developed with Flask and SQLAlchemy to perform CRUD (Create, Read, Update, Delete) operations on a MySQL database.

## Technologies Used

- Flask
- Flask_SQLAlchemy
- MySQL
- MySQL Connector

## Environment Setup

### Prerequisites

- Python 3.x
- MySQL Server

### Installing Dependencies

```bash
pip install flask
pip install flask_sqlalchemy
pip install mysql-connector-python
```

### Database Setup
Ensure that the MySQL Server is running and create a database named flaskcrud. Run the following commands in MySQL:
```sql
CREATE DATABASE flaskcrud;
USE flaskcrud;
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(100)
);
```
### Application Configuration
Modify the database URI configuration as needed in the line:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://teste:teste@localhost/flaskcrud'
```
### Running the Application
To run the application, execute the command:
```bash
python app.py

```


## API Endpoints
Get All Users
- URL: /user
- Method: GET
- Success Response: `200 OK`

```json
{
  "usuarios": [
    {"id": 1, "nome": "Name", "email": "email@example.com"},
    ...
  ]
}
```
Get a User by ID
- URL: /user/<id>
- Method: GET
- Success Response: `200 OK`
```json
{
  "usuario": {"id": 1, "nome": "Name", "email": "email@example.com"}
}
```

Create New User
- URL: /user
- Method: POST
- Request Body
```json
{
  "nome": "Name",
  "email": "email@example.com"
}
```

Update User by ID
- URL: /user/<id>
- Method: PUT
- Request Body
```json 
{
  "nome": "Updated Name",
  "email": "updated_email@example.com"
}
```
Delete User by ID
URL: /user/<id>
Method: DELETE
Success Response: `200 OK`
```json
{
  "usuario": {"id": 1, "nome": "Name", "email": "email@example.com"},
  "mensagem": "Successfully deleted"
}
```

## Contribution
Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you would like to make.

## License
This project is licensed under the MIT License.

### Summary
This project demonstrates a simple implementation of a REST API with Flask, using SQLAlchemy for object-relational mapping and CRUD operations with a MySQL database.