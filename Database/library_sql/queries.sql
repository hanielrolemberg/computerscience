USE library;

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
