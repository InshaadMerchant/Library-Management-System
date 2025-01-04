SELECT B.Title, LB.Branch_Name, 
CAST(JULIANDAY(BL.Returned_date) AS INTEGER) - CAST(JULIANDAY(BL.Date_out) AS INTEGER) AS Borrowed_Days
FROM    BOOK AS B, LIBRARY_BRANCH  AS LB, BOOK_LOANS AS BL
WHERE   B.Book_Id = BL.Book_Id AND 
        BL.Branch_Id = LB.Branch_Id AND 
        BL.Date_Out BETWEEN '2022-03-05' AND '2022-03-23' AND 
        BL.Returned_date IS NOT NULL;