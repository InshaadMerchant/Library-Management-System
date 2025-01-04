DROP TABLE IF EXISTS LIBRARY_BRANCH;
CREATE TABLE LIBRARY_BRANCH(
		Branch_id			INTEGER				PRIMARY KEY AUTOINCREMENT,
		Branch_name			VARCHAR(20)			NOT NULL,
		Address				TEXT				NOT NULL			
		);

DROP TABLE IF EXISTS PUBLISHER;
CREATE TABLE PUBLISHER(
		Publisher_name		CHAR(20)			NOT NULL,
		Phone_no			VARCHAR(13)			NOT NULL,
		Address				TEXT				NOT NULL,
		PRIMARY KEY (Publisher_name));        

DROP TABLE IF EXISTS BOOK;
CREATE TABLE BOOK(
		Book_id				INTEGER				PRIMARY KEY AUTOINCREMENT,
		Title				VARCHAR(20)			NOT NULL,
		Publisher_name		VARCHAR(50)			NOT NULL,
		FOREIGN KEY (Publisher_name) REFERENCES PUBLISHER(Publisher_name)
		ON UPDATE CASCADE
		ON DELETE CASCADE);


DROP TABLE IF EXISTS BOOK_AUTHORS;
CREATE TABLE BOOK_AUTHORS(
		Book_id				INTEGER				PRIMARY KEY AUTOINCREMENT,
		Author_name			VARCHAR(50)			NOT NULL
		);

DROP TABLE IF EXISTS BOOK_COPIES;
CREATE TABLE BOOK_COPIES(
		Book_id				INT					NOT NULL,
		Branch_id			INT					NOT NULL,
		No_of_Copies		INT					NOT NULL,
		FOREIGN KEY (Book_id) REFERENCES BOOK(Book_id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (Branch_id) REFERENCES LIBRARY_BRANCH(Branch_id)
		ON UPDATE CASCADE
		ON DELETE CASCADE);

DROP TABLE IF EXISTS BORROWER;
CREATE TABLE BORROWER(
		Card_no				INTEGER				PRIMARY KEY AUTOINCREMENT,
		Name				VARCHAR(30)			NOT NULL,
		Address				TEXT				NOT NULL,
		Phone				VARCHAR(13)			NOT NULL
		);


DROP TABLE IF EXISTS BOOK_LOANS;
CREATE TABLE BOOK_LOANS(
		Book_id				INT					NOT NULL,
		Branch_id			INT					NOT NULL,
		Card_no				INT					NOT NULL,
		Date_out			DATE				NOT NULL,
		Due_Date			DATE				NOT NULL,
		Returned_date		DATE				NULL,
		FOREIGN KEY (Book_id) 	REFERENCES BOOK(Book_id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (Branch_id) REFERENCES LIBRARY_BRANCH(Branch_id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (Card_no) 	REFERENCES BORROWER(Card_no)
		ON UPDATE CASCADE
		ON DELETE CASCADE);

