SELECT BOOK.Title, BOOK_AUTHORS.Author_Name, CAST(JULIANDAY(Returned_date) AS INTEGER) - CAST(JULIANDAY(Date_out) AS INTEGER) as Days_Borrowed,
CASE WHEN BOOK_LOANS.Returned_date IS NULL THEN 'YES' WHEN CAST(JULIANDAY(Returned_date) AS INTEGER) - CAST(JULIANDAY(Due_Date)AS INTEGER) > 0 THEN 'YES' ELSE 'NO'
END AS Late
FROM  BORROWER ,BOOK , BOOK_AUTHORS
JOIN  BOOK_LOANS ON BORROWER.Card_no=BOOK_LOANS.Card_No 
WHERE BORROWER.Name = 'Ethan Martinez' AND BOOK_LOANS.Book_id=BOOK.Book_id AND BOOK.Book_id=BOOK_AUTHORS.Book_Id 
ORDER BY BOOK_LOANS.Date_Out;