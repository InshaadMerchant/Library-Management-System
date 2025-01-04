# Library Management System (LMS)

# Project Overview

This Library Management System (LMS) is developed as a part of CSE 3330 – 004 Project 2 - Part 3 by Group 14, comprising Araohat Kokate, Inshaad Merchant, and Athrva Arora. The project is built to handle the operations of book loans, borrower management, and library branch service optimizations.

# Features

View and Modify Book Loans: Display book loan records and update them to reflect late returns.

Manage Library Branches: Add attributes to library branches and calculate late fees.

Complex Queries on Books and Borrowers: Perform sophisticated queries to manage books and borrowers efficiently.

Dynamic Views Creation: Create views to provide summarized information about book loans, including late fee calculations.

Interactive GUI: A front-end interface for easy interaction with the database.

# Getting Started

# Prerequisites

SQLite

Python 3.x

Dependencies listed in requirements.txt

# Installation

Clone the repository:

git clone https://github.com/InshaadMerchant/Library-Management-System.git

Install the required packages:

pip install -r requirements.txt

Running the System

Navigate to the project directory and run the Python script that initiates the GUI:

python main.py

# Usage

The system supports various operations through an interactive GUI and SQL queries. Here are some common tasks:

# Viewing Book Loans

To view the current book loans:

.headers on

.mode column

SELECT * FROM BOOK_LOANS;

# Updating Book Loans for Lateness

To mark a book as returned late:

ALTER TABLE BOOK_LOANS

ADD COLUMN Late INT;

UPDATE BOOK_LOANS

SET Late = CASE 

    WHEN Returned_Date > Due_Date THEN 1 
    
    ELSE 0 
    
END;

# Managing Library Branches

To manage details of library branches including late fees:

ALTER TABLE LIBRARY_BRANCH

ADD COLUMN LateFee INT;

UPDATE LIBRARY_BRANCH

SET LateFee = CASE 

    WHEN Branch_id = 1 THEN 1   
    
    ELSE 0 
    
END;

# Querying Borrower Details

To fetch details about borrowers and any associated late fees:

SELECT DISTINCT vBookLoanInfo.Card_no, BORROWER.Name, IFNULL(LateFeeBalance, 0)

FROM vBookLoanInfo

LEFT JOIN BORROWER ON vBookLoanInfo.Card_no = BORROWER.Card_no

ORDER BY LateFeeBalance DESC;

# Contributing

Group 14 welcomes contributions. Please open an issue first to discuss what you would like to change. Ensure to update tests as appropriate.

# Acknowledgments

UT Arlington's tradition of academic integrity

Our professor for guidance and project specifications
