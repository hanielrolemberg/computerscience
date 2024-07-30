USE library;

INSERT INTO Authors (Name, Nationality, DateOfBirth)
VALUES
('J.K. Rowling', 'British', '1965-07-31'),
('George R.R. Martin', 'American', '1948-09-20');

INSERT INTO Books (Title, Genre, AuthorID, PublicationYear)
VALUES
('Harry Potter and the Philosopher\'s Stone', 'Fantasy', 1, 1997),
('A Game of Thrones', 'Fantasy', 2, 1996);
