SELECT LIBRARY_BRANCH.Branch_Name,
    COUNT(BOOK_LOANS.Book_id) AS Num_of_Book_Borrowed,
    COUNT(CASE WHEN DATE('now') >= BOOK_LOANS.Returned_date THEN BOOK_LOANS.Book_id END) AS 
    Num_of_Books_Returned,
    COUNT(CASE WHEN BOOK_LOANS.Returned_date IS NULL OR BOOK_LOANS.Returned_date = 'NULL' THEN 
    BOOK_LOANS.Book_id END) AS Num_of_Books_Still_Borrowed,
    COUNT(CASE WHEN BOOK_LOANS.Returned_date > BOOK_LOANS.Due_Date AND 
    BOOK_LOANS.Returned_date IS NOT 'NULL' THEN BOOK_LOANS.Book_id END) AS 
    Num_of_Late_Returns
FROM LIBRARY_BRANCH, BOOK_LOANS
WHERE LIBRARY_BRANCH.Branch_Id = BOOK_LOANS.Branch_Id
GROUP BY LIBRARY_BRANCH.Branch_Name;
