import tkinter as tk
from tkinter import ttk
import sqlite3

class LibraryManagementSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        # Create GUI components (buttons, labels, entry fields, etc.)
        self.label_card_no = ttk.Label(root, text="Borrower Card No:")
        self.entry_card_no = ttk.Entry(root)

        self.label_name = ttk.Label(root, text="Borrower Name:")
        self.entry_name = ttk.Entry(root)

        self.button_query_5a = ttk.Button(root, text="Query 5a", command=self.query_5a)

        # Add event handlers for each button to execute the specified queries

    def execute_query(self, query, params):
        conn = sqlite3.connect("lms.db")
        cursor = conn.cursor()

        # Execute the query and fetch the results
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Display results in the GUI (update the Treeview widget)

        # Commit and close connection
        conn.commit()
        conn.close()

    def query_5a(self):
        # Construct the query for 5a
        query = """
        SELECT
            b.Card_no,
            b.Name AS Borrower_Name,
            COALESCE(SUM(vli.LateFeeBalance), 0) AS LateFee_Balance
        FROM
            BORROWER b
        LEFT JOIN vBookLoanInfo vli ON b.Card_no = vli.Card_no
        WHERE
            b.Card_no = COALESCE(?, b.Card_no) OR
            b.Name LIKE COALESCE(?, b.Name, '')
        GROUP BY
            b.Card_no, b.Name
        ORDER BY
            LateFee_Balance;
        """

        # Get input values from the entry fields
        card_no = self.entry_card_no.get()
        name = self.entry_name.get()

        # Execute the query with input parameters
        self.execute_query(query, (card_no, name))

# Instantiate the Tkinter application
root = tk.Tk()
app = LibraryManagementSystemApp(root)
root.mainloop()