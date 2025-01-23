CREATE TABLE Books (
    Book_ID SERIAL PRIMARY KEY,
    Book_Name VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Quantity INT NOT NULL
);

CREATE TABLE RequestBook (
    Request_ID SERIAL PRIMARY KEY,
    StudentName VARCHAR(255) NOT NULL,
    PRN INT NOT NULL,
    Book_ID INT NOT NULL,
    FOREIGN KEY (Book_ID) REFERENCES Books (Book_ID)
);
