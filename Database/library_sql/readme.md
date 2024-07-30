# Library Management Project

This project is a simple library management system using SQL. It covers setting up a local environment on Ubuntu, creating and populating the database, and executing queries and procedures using VSCode.

## My personal environment

- Ubuntu Linux
- VSCode
- MySQL Server

## Step 1: Install MySQL Server

Open a terminal and run the following commands to install MySQL Server:

```sh
sudo apt update
sudo apt install mysql-server

```

Start and enable the MySQL service:

```sh
sudo systemctl start mysql
sudo systemctl enable mysql
```

Run the MySQL secure installation script:
```sh
sudo mysql_secure_installation

```
Follow the prompts to set up your MySQL server, including setting the root password.

## Step 2: Install VSCode and Extensions
Download and install VSCode.

Install the SQLTools extension:

Open VSCode.
Go to the Extensions view (Ctrl+Shift+X).
Search for SQLTools and install it.
Install the SQLTools MySQL/MariaDB driver.

## Step 3: Configure MySQL Authentication
If you encounter authentication errors, you may need to change the MySQL authentication method.

Open a terminal and access MySQL:
```sh
sudo mysql -u root -p

```
Run the following commands to change the authentication method:

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
FLUSH PRIVILEGES;
```

Replace 'your_password' with your actual root password.

## Step 4: Create the Project Structure
Create a new folder for your project, e.g., Library_SQL_Project. Inside this folder, create the following SQL files:

create_database.sql
insert_data.sql
queries.sql
procedures_triggers.sql
Step 5: Write the SQL Scripts
create_database.sql

## Step 5: Write the SQL Scripts
create_database.sql


```sql
CREATE DATABASE Library;
USE Library;

CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Nationality VARCHAR(50),
    DateOfBirth DATE
);

CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Genre VARCHAR(50),
    AuthorID INT,
    PublicationYear YEAR,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

CREATE TABLE Loans (
    LoanID INT AUTO_INCREMENT PRIMARY KEY,
    BookID INT,
    LoanDate DATE,
    ReturnDate DATE,
    BorrowerName VARCHAR(100),
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);
```
insert_data.sql

```sql
USE Library;

INSERT INTO Authors (Name, Nationality, DateOfBirth)
VALUES
('J.K. Rowling', 'British', '1965-07-31'),
('George R.R. Martin', 'American', '1948-09-20');

INSERT INTO Books (Title, Genre, AuthorID, PublicationYear)
VALUES
('Harry Potter and the Philosopher\'s Stone', 'Fantasy', 1, 1997),
('A Game of Thrones', 'Fantasy', 2, 1996);
```

queries.sql
```sql
USE Library;

-- Query All Books and Their Authors
SELECT 
    Books.Title, 
    Books.Genre, 
    Authors.Name AS Author, 
    Books.PublicationYear
FROM 
    Books
JOIN 
    Authors ON Books.AuthorID = Authors.AuthorID;

-- Insert a New Loan
INSERT INTO Loans (BookID, LoanDate, ReturnDate, BorrowerName)
VALUES
(1, '2024-07-01', '2024-07-15', 'John Smith');

-- Query Current Loans
SELECT 
    Loans.LoanID,
    Books.Title,
    Loans.LoanDate,
    Loans.ReturnDate,
    Loans.BorrowerName
FROM 
    Loans
JOIN 
    Books ON Loans.BookID = Books.BookID
WHERE 
    Loans.ReturnDate >= CURDATE();


```
procedures_triggers.sql

```sql
USE Library;

DELIMITER //
CREATE PROCEDURE RegisterLoan (
    IN p_BookID INT,
    IN p_LoanDate DATE,
    IN p_ReturnDate DATE,
    IN p_BorrowerName VARCHAR(100)
)
BEGIN
    INSERT INTO Loans (BookID, LoanDate, ReturnDate, BorrowerName)
    VALUES (p_BookID, p_LoanDate, p_ReturnDate, p_BorrowerName);
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER UpdateBookStatus
AFTER INSERT ON Loans
FOR EACH ROW
BEGIN
    UPDATE Books
    SET Status = 'Loaned'
    WHERE BookID = NEW.BookID;
END //
DELIMITER ;
```

## Step 6: Configure SQLTools in VSCode
Open the Command Palette (Ctrl+Shift+P) and select SQLTools: New Connection.
Configure the connection with the following details:
Connection Name: MySQL_Local
Server/Host: localhost
Port: 3306
Username: root
Password: your_password
Database: (leave empty or specify the database name)
Step 7: Execute the SQL Scripts
Open each SQL file (create_database.sql, insert_data.sql, queries.sql, procedures_triggers.sql) in VSCode.
Select the entire content of the file.
Execute the selected query using Ctrl+Alt+E or right-click and select Run Query.

## MySQL Commands Reference
Here are some common MySQL commands you might find useful:

```sql
SHOW DATABASES;
USE database_name;
SHOW TABLES;
DESCRIBE table_name;
SELECT * FROM table_name;
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
UPDATE table_name SET column1 = value1 WHERE condition;
DELETE FROM table_name WHERE condition;
ALTER TABLE table_name ADD column_name column_type;
DROP TABLE table_name;
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'host';
REVOKE ALL PRIVILEGES ON database_name.* FROM 'username'@'host';
SHOW GRANTS FOR 'username'@'host';
DROP USER 'username'@'host';
SELECT CURRENT_USER();
SHOW TABLE STATUS FROM database_name;
SHOW CREATE DATABASE database_name;
SHOW CREATE TABLE table_name;
CALL procedure_name(parameter1, parameter2);


```sh
mysqldump -u username -p database_name > backup.sql
mysql -u username -p database_name < backup.sql

```


## Conclusion
```sql
This `README.md` file provides a comprehensive guide to setting up, configuring, and running the library management project using SQL and VSCode on Ubuntu. Feel free to modify it according to your specific needs.
```

