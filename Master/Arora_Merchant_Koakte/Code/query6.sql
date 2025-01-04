SELECT B.Name
FROM   BORROWER AS B
JOIN   BOOK_LOANS AS BL ON BL.Returned_date = 'NULL'
WHERE  B.Card_no = BL.Card_no; 