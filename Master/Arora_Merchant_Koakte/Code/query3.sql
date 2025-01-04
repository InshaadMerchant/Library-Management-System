UPDATE BOOK_COPIES
SET No_of_Copies = No_of_Copies + 1
WHERE Branch_id = (SELECT LB.Branch_id FROM LIBRARY_BRANCH AS LB WHERE LB.Branch_name = 'East Branch');
