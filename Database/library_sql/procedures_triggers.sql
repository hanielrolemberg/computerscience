USE library;

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
