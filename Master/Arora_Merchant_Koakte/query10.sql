SELECT B.Name, B.Address
FROM BORROWER AS B, LIBRARY_BRANCH AS LB,  BOOK_LOANS AS BL 
WHERE BL.branch_id = LB.branch_id AND B.card_no = BL.card_no AND LB.branch_name = 'West Branch';

