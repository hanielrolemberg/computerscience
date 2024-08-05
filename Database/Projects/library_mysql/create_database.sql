CREATE DATABASE library;
USE library;

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
