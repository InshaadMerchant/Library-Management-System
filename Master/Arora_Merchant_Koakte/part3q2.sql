
ALTER TABLE LIBRARY_BRANCH
ADD COLUMN LateFee INT;

UPDATE LIBRARY_BRANCH
SET LateFee = CASE 
    WHEN Branch_id = 1 THEN 1  
    WHEN Branch_id = 2 THEN 2
    WHEN Branch_id = 3 THEN 3  
    WHEN Branch_id = 4 THEN 4  
    WHEN Branch_id = 5 THEN 5  

    ELSE 0  
END;
