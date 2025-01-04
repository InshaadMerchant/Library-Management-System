/*Query 1*/
INSERT INTO BORROWER(Name, Address, Phone)
VALUES('Araohat Kokate','587 Spaniolo Dr, Arlington TX, 76010','682-340-0275');
/*Query 2*/
UPDATE BORROWER
SET Phone = '837-721-8965'
WHERE Name like 'Araohat Kokate';
/*Query 3*/
UPDATE BOOK_COPIES
SET No_Of_Copies = No_Of_Copies + 1
WHERE LIBRARY_BRANCH.Branch_Name = 'East Branch';
/*Query 4-a*/
INSERT INTO BOOK(Title, Publisher_name)
VALUES('Harry Potter and the Sorcerer"s Stone','Oxford Publishing');

INSERT INTO BOOK_AUTHORS(Author_Name)
VALUES('J.K.Rowling');
/*Query 4-b*/
INSERT INTO LIBRARY_BRANCH(Branch_Name, Branch_Address)
VALUES('North Branch','456 NW, Irving, TX 76100');

INSERT INTO LIBRARY_BRANCH(Branch_Name, Branch_Address)
VALUES('UTA Branch','123 Cooper St, Arlington TX 76101');
/*Query 5*/
SELECT Title, Branch_Name, CAST(JULIANDAY(Returned_date) AS INTEGER) - CAST(JULIANDAY(Date_out) AS INTEGER) AS Borrowed_Days
FROM BOOK, BOOK_LOANS, LIBRARY_BRANCH
WHERE BOOK.Book_Id = BOOK_LOANS.Book_Id AND BOOK_LOANS.Branch_Id = LIBRARY_BRANCH.Branch_Id AND Date_Out BETWEEN '2022/03/05' AND '2022/03/23';
/*Query 6*/
SELECT Name
FROM BORROWER, BOOK_LOANS
WHERE BORROWER.Card_No = BOOK_LOANS.Card_No AND BOOK_LOANS.Returned_date = NULL;
/*Query 7*/

/*Query 8*/
SELECT Title, MAX(CAST((Returned_date)AS INTEGER) - CAST((Date_out) AS INTEGER) AS Borrowed_Days)
FROM BOOK, BOOK_LOANS
WHERE BOOK.Book_Id = BOOK_LOANS.BOOK_Id;
/*Query 9*/
SELECT Title, Author_Name
/*Query 10*/
SELECT Name
FROM BORROWER, LIBRARY_BRANCH, BOOK_LOANS
WHERE BORROWER.Card_No = BOOK_LOANS.Card_No AND BOOK_LOANS.Branch_Id = LIBRARY_BRANCH.Branch_Id AND LIBRARY_BRANCH.Branch_Name = 'West Branch';