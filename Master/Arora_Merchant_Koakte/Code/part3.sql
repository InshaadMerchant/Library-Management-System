ALTER TABLE BOOK_LOANS
ADD COLUMN Late INT;

UPDATE BOOK_LOANS
SET Late = CASE 
    WHEN Returned_Date IS NULL OR Due_Date IS NULL THEN NULL  
    WHEN Returned_Date > Due_Date THEN 1 
    WHEN Returned_Date > Due_Date THEN 1 
    ELSE 0 
END;
