
DROP VIEW IF EXISTS vBookLoanInfo;


CREATE VIEW vBookLoanInfo AS
SELECT
    bl.Card_no,
    b.Name AS "Borrower Name",
    bl.Date_out,
    bl.Due_Date,
    bl.Returned_date,
    CAST((julianday(bl.Returned_date) - julianday(bl.Date_out)) AS INTEGER) AS TotalDays,
    bo.Title AS "Book Title",
    ba.Book_id,
    CASE
        WHEN bl.Returned_date <= bl.Due_Date THEN 0
        ELSE CAST((julianday(bl.Returned_date) - julianday(bl.Due_Date)) AS INTEGER)
    END AS "Number of days returned late",
    bl.Branch_id,
    CASE
        WHEN bl.Returned_date <= bl.Due_Date THEN 0
        ELSE CAST((julianday(bl.Returned_date) - julianday(bl.Due_Date)) AS INTEGER) * lb.LateFee
    END AS LateFeeBalance
FROM
    BOOK_LOANS bl
JOIN BORROWER b ON bl.Card_no = b.Card_no
JOIN BOOK bo ON bl.Book_id = bo.Book_id
JOIN BOOK_AUTHORS ba ON bo.Book_id = ba.Book_id 
JOIN LIBRARY_BRANCH lb ON bl.Branch_id = lb.Branch_id;
