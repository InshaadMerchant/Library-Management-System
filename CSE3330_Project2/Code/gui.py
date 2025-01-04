from tkinter import *
import sqlite3

root = Tk()
root.title('Library Mangement System')
root.geometry("500x500")
#address_book_connect = sqlite3.connect(os.path.abspath('lms.db'))
#address_book_cur = address_book_connect.cursor()



#query-1
def query1():
    query1_pop = Toplevel(root)
    query1_pop.geometry("500x500")
    query1_pop.title("query1")

    info = Label(query1_pop, text="Please enter your card_no, branch_id, book_id by referring to the list below\nthe list: book_id, Title, per_Book_copies, Branch_id\n", fg="BLUE")
    info.grid(row=0, column=1, padx=20)

    bookid = Entry(query1_pop, width=60)
    bookid.grid(row=1, column=1, padx=20)
    bookid_label = Label(query1_pop, text='Bookid: ', fg="BLUE")
    bookid_label.grid(row=1, column=0, sticky=E)

    branchid = Entry(query1_pop, width=60)
    branchid.grid(row=2, column=1, padx=20)
    branchid_label = Label(query1_pop, text='branchid: ', fg="BLUE")
    branchid_label.grid(row=2, column=0, sticky=E)

    cardno = Entry(query1_pop, width=60)
    cardno.grid(row=3, column=1, padx=20)
    cardno_label = Label(query1_pop, text='card_no: ', fg="BLUE")
    cardno_label.grid(row=3, column=0, sticky=E)

    datedue = Entry(query1_pop, width=60)
    datedue.grid(row=4, column=1, padx=20)
    datedue_label = Label(query1_pop, text='datedue: ', fg="BLUE")
    datedue_label.grid(row=4, column=0, sticky=E)

    dateout = Entry(query1_pop, width=60)
    dateout.grid(row=5, column=1, padx=20)
    dateout_label = Label(query1_pop, text='dateout: ', fg="BLUE")
    dateout_label.grid(row=5, column=0, sticky=E)

    iq_conn = sqlite3.connect('lms.db')
    iq_cur = iq_conn.cursor()

    iq_cur.execute("""
        SELECT B.Book_id, B.Title, COUNT(BC.no_of_copies) AS per_Book_copies, BC.Branch_Id 
        FROM BOOK_COPIES as BC
        INNER JOIN BOOK as B ON B.Book_id = BC.Book_id
        GROUP BY B.Book_id, BC.Branch_Id
    """)
    
    output_records = iq_cur.fetchall()
    print_record = ''
    for output_record in output_records:
        print_record += ("{},{},{},{} \n".format(output_record[0], output_record[1], output_record[2], output_record[3]))
    
    iq_label = Label(query1_pop, text=print_record, fg="BLUE")
    iq_label.grid(row=8, column=0, columnspan=2)

    # commit changes
    iq_conn.commit()
    # close the DB connection
    iq_cur.close()
    iq_conn.close()

    submit_btn = Button(query1_pop, text='CHECKOUT', bg="BLUE", fg="WHITE", command=lambda: submit1(bookid.get(), branchid.get(), cardno.get(), dateout.get(), datedue.get(), query1_pop))
    submit_btn.grid(row=6, column=0, columnspan=2, pady=5, padx=5)


def submit1(bi, bri, cn, do, dd, query1_pop):
    submit_conn = sqlite3.connect('lms.db')
    submit_cur = submit_conn.cursor()
    try:
        submit_cur.execute("""
            INSERT INTO BOOK_LOANS (Book_id, Branch_id, Card_No, Date_Out, Due_Date)
            VALUES (?, ?, ?, ?, ?)
        """, (bi, bri, cn, do, dd))
    except sqlite3.Error as e:
        print('Error Insert failed:', e)
    
    submit_cur.execute("""
        UPDATE BOOK_COPIES 
        SET no_of_copies = no_of_copies - 1 
        WHERE Branch_Id = ? AND Book_id = ?
    """, (bri, bi))
    
    submit_cur.execute("""
        SELECT no_of_copies 
        FROM BOOK_COPIES 
        WHERE Branch_Id = ? AND Book_id = ?
    """, (bri, bi))
    
    output_records = submit_cur.fetchone()
    print_record = "The updated no_of_copies at the selected branch is " + str(output_records)
    
    label = Label(query1_pop, text=print_record, fg="BLUE")
    label.grid(row=7, column=0, columnspan=2)
    
    submit_conn.commit()
    submit_conn.close()





#query2
def q2():
    #q2_conn = sqlite3.connect('lms.db');
    #q2_cursor = q2_conn.cursor();
    q2_pop = Toplevel(root)
    q2_pop.geometry("900x600")
    q2_pop.title("Query #2")

    q2_purposeText = Label(q2_pop,text='Add information about borrower in the given fields:\n', fg="BLUE")
    q2_purposeText2 = Label(q2_pop,text='Enter full name in "Name" Field and Address in "Address" Field\n and phone number in "PhoneNum" Field in the format XXX-XXX-XXXX \n', fg="BLUE")
    q2_purposeText.grid(row =0, column =1)
    q2_purposeText2.grid(row =1, column =1)
    
    name = Entry(q2_pop, width = 60)
    name.grid(row =2, column =1)

    addr = Entry(q2_pop, width = 60)
    addr.grid(row =3, column =1)

    phone = Entry(q2_pop, width = 60)
    phone.grid(row =4, column =1)

    in_name_label = Label(q2_pop, text = 'Name', fg="BLUE")
    in_name_label.grid(row =2, column =0)
    in_addr_label = Label(q2_pop, text = 'Address', fg="BLUE")
    in_addr_label.grid(row =3, column =0)
    in_phone_label = Label(q2_pop, text = 'PhoneNum', fg="BLUE")
    in_phone_label.grid(row =4, column =0)

    
    submit_btn = Button(q2_pop, text = 'ADD BORROWER', bg="BLUE", fg="WHITE", command = lambda :q2_submit(name,addr,phone,q2_pop))
    submit_btn.grid(row =5, column = 0, columnspan=2, pady=5, padx=5)
   
def q2_submit(name, addr, phone, q2_pop):
    q2_conn = sqlite3.connect('lms.db')
    q2_cur = q2_conn.cursor()
    q2_cur.execute("INSERT INTO BORROWER(Name, address, phone) VALUES (:Name, :address, :phone)",
                   {
                       'Name': name.get(),
                       'address': addr.get(),
                       'phone': phone.get()
                   })
    
    q2_cur.execute("SELECT Card_no FROM BORROWER WHERE Name = ? AND address = ? AND phone = ?",(name.get(),addr.get(),phone.get()))
    output = q2_cur.fetchone()
    print_record = ''
    print(output[0])
    print_record += str(output[0])
    print_record = "Card Number assigned: " + print_record +"\n"
    output_label = Label(q2_pop, text=print_record)
    output_label.grid(row=10,column=0, columnspan=2, pady=5, padx=5)

    q2_conn.commit()
    q2_conn.close()






#query-3
def q3():
    def submit():
        book_title_t = book_title.get()
        author_name_t = author_name.get()
        publisher_name_t = publisher_name.get()

        submit_conn = sqlite3.connect('lms.db')
        submit_cur = submit_conn.cursor()

       
        submit_cur.execute('INSERT INTO BOOK (Title, Publisher_Name) VALUES (?, ?)', (book_title_t, publisher_name_t))
        book_id = submit_cur.lastrowid

        
        submit_cur.execute('INSERT INTO BOOK_AUTHORS (Book_Id, Author_Name) VALUES (?, ?)', (book_id, author_name_t))


        for i in range(1, 6):
            submit_cur.execute('INSERT INTO BOOK_COPIES (Book_Id, Branch_Id, no_of_copies) VALUES (?, ?, ?)',
                               (book_id, i, 5))



        submit_conn.commit()
        submit_conn.close()

    iq = sqlite3.connect('lms.db')
    iq_cur = iq.cursor()

    root = Tk()
    root.title('Add Book')
    root.geometry("500x500")



    book_title = Entry(root, width=60)
    book_title.grid(row=0, column=1, padx=20)

    author_name = Entry(root, width=60)
    author_name.grid(row=1, column=1)

    publisher_name = Entry(root, width=60)
    publisher_name.grid(row=2, column=1)




    book_title_label = Label(root, text='Book Title: ', fg="BLUE")
    book_title_label.grid(row=0, column=0, padx=20)

    author_name_label = Label(root, text='Author Name: ', fg="BLUE")
    author_name_label.grid(row=1, column=0)

    publisher_name_label = Label(root, text='Publisher Name: ', fg="BLUE")
    publisher_name_label.grid(row=2, column=0)

  

    submit_button = Button(root, text='ADD', bg="BLUE", fg="WHITE", command = submit)
    submit_button.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

    iq.commit()
    iq.close()









#query-4
def q4():
    q4_pop = Toplevel(root)
    q4_pop.geometry("900x600")
    q4_pop.title("Query #4")

    q4_purposeText = Label(q4_pop,text='From the book list below enter a book title in the text field below:\n', fg="BLUE")
    q4_purposeText.grid(row =0, column =0)
    q4_conn = sqlite3.connect('lms.db')
    q4_cur = q4_conn.cursor()
    q4_cur.execute("SELECT Book_id, Title FROM BOOK")

    output = q4_cur.fetchall()
    print_rec = ''
    
    for outp in output:
        print_rec += str(str(outp[0]) + " " + outp[1]+"\n")

    out_label = Label(q4_pop, text = print_rec, fg="BLUE")
    out_label.grid(row =2, column=0, columnspan =2)

    q4_conn.commit()
    q4_conn.close()  
  
    title = Entry(q4_pop, width = 80)
    title.grid(row =3, column =1)

    title_label = Label(q4_pop, text = 'Enter the book title: ', fg="BLUE")
    title_label.grid(row =3, column = 0)

    submit_btn = Button(q4_pop, text = 'ENTER TITLE', bg="BLUE", fg="WHITE", command = lambda :q4_submit(title, q4_pop))
    submit_btn.grid(row =4, column = 0, columnspan =2, pady=5, padx=5)

def q4_submit(title, q4_pop):
    q4_conn = sqlite3.connect('lms.db')
    q4_cur = q4_conn.cursor()
    #t = str("'"+str(title.get())+"'")
    t = title.get()
    #print(t)
    #print(len(t))
    q4_cur.execute("SELECT Branch_Name, COUNT(*) FROM BOOK_LOANS as BL,LIBRARY_BRANCH as LB, BOOK as B WHERE BL.Branch_id = LB.Branch_id AND BL.Book_id = B.Book_id AND Title like ? GROUP BY Branch_name",(t,))
    output = q4_cur.fetchall()
    print_rec = 'Branch Name               Number of Copies\n\n'
    #output = str(output)
    #print(output)
    for outp in output:
        print_rec += str(str(outp[0]) + "                " + str(outp[1])+"\n")

    #print(print_rec)
    output_label = Label(q4_pop, text=print_rec)
    output_label.grid(row=5,column=0, columnspan=2)
    q4_conn.commit()
    q4_conn.close()







#query-6b
def query6b():
    query6b_pop = Toplevel(root)
    query6b_pop.geometry("600x500")
    query6b_pop.title("query6b")

    info = Label(query6b_pop, text="Search For Book Information by entering Borrower ID or Book ID/Title or None \n"
                                  "the Output will be in the following order: Borrower ID, Book Title, LateFeeBalance \n", fg="BLUE")
    info.grid(row=0, column=1, padx=20)

    borrower_id = Entry(query6b_pop, width=60)
    borrower_id.grid(row=1, column=1, padx=20)
    borrower_id_label = Label(query6b_pop, text='Borrower ID: ', fg="BLUE")
    borrower_id_label.grid(row=1, column=0)

    book_info = Entry(query6b_pop, width=60)
    book_info.grid(row=2, column=1, padx=20)
    book_info_label = Label(query6b_pop, text='Book ID/Title: ', fg="BLUE")
    book_info_label.grid(row=2, column=0)

    submit_btn = Button(query6b_pop, text='SEARCH', bg="BLUE", fg="WHITE", command=lambda: submit6b(borrower_id.get(), book_info.get(), query6b_pop))
    submit_btn.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

    query6b_pop.mainloop()

def submit6b(borrower_id, book_info, query6b_pop):
    submit_conn = sqlite3.connect('lms.db')
    submit_cur = submit_conn.cursor()

    try:
        submit_cur.execute("SELECT v.Card_no, BORROWER.name, b.Title, "
                    "CASE WHEN LateFeeBalance IS NULL THEN 'Non-Applicable' "
                    "ELSE '$' || printf('%.2f', LateFeeBalance) END AS LateFeeBalance "
                    "FROM vBookLoanInfo v "
                    "JOIN BOOK b ON v.Book_id = b.Book_id "
                    "JOIN BORROWER ON v.Card_no = BORROWER.Card_no "  
                    "WHERE v.Card_no = ? OR v.Book_id = ? OR b.Title LIKE '%' || ? || '%' "
                    "ORDER BY LateFeeBalance DESC",
                    (borrower_id, book_info, book_info))

    except sqlite3.Error as e:
        print('Error Select failed:', e)

    output_records = submit_cur.fetchall()
    print_record = ''
    for output_record in output_records:
        print_record += ("{},{},{},{} \n".format(output_record[0], output_record[1], output_record[2], output_record[3]))

    iq_label = Label(query6b_pop, text=print_record)
    iq_label.grid(row=4, column=0, columnspan=2)

    # close the DB connection
    submit_cur.close()
    submit_conn.close()

#query-5
def query5():
    query5_pop = Toplevel(root)
    query5_pop.geometry("700x500")
    query5_pop.title("query5")

    iq_conn = sqlite3.connect('lms.db')
    iq_cur = iq_conn.cursor()

    info = Label(query5_pop, text = " Please enter the range of the due date for the retrieve of the late books \n the list: book_id, Branch_id, card_no, date_out, Due_Date, Returned_date, num_days_late\n", fg="BLUE")
    info.grid(row = 0, column = 1, padx = 20)
    start = Entry(query5_pop, width = 60)
    start.grid(row = 1, column = 1, padx = 20)
    start_label = Label(query5_pop, text = 'first due date: ', fg="BLUE")
    start_label.grid(row =1, column = 0, sticky=E)

    finish = Entry(query5_pop, width = 60)
    finish.grid(row = 2, column = 1, padx = 20)
    finish_label = Label(query5_pop, text = 'last due date: ', fg="BLUE")
    finish_label.grid(row =2, column = 0, sticky=E)

    submit_btn = Button(query5_pop, text ='FIND', bg="BLUE", fg="WHITE", command=lambda: submit5(start.get(), finish.get() ,query5_pop))
    submit_btn.grid(row = 3, column =0, columnspan = 2, pady = 5, padx = 5)
    #commit changes
    iq_conn.commit()
    #close the DB connection
    iq_cur.close()
    iq_conn.close()

def submit5(st,fh,query5_pop):
    submit_conn = sqlite3.connect('lms.db')
    submit_cur = submit_conn.cursor()
    try:
        submit_cur.execute(" SELECT Book_id, Branch_id, Card_No, Date_Out, Due_Date, Returned_date, CAST(JULIANDAY(Returned_date) AS INTEGER) - CAST(JULIANDAY(Due_Date)AS INTEGER) AS num_days_late FROM BOOK_LOANS WHERE Late = '1' AND (Due_Date < ? AND   Due_Date > ?) ",
        (fh, st,))
    except sqlite3.Error as e:
        print('Error Select failed:',e)
    output_records = submit_cur.fetchall()
    print_record = ''
    for output_record in output_records:
        print_record += ( "{},{},{},{},{},{},{} \n".format(output_record[0],output_record[1],output_record[2],output_record[3],output_record[4],output_record[5],output_record[6]))
    iq_label = Label(query5_pop, text = print_record, fg="BLUE")
    iq_label.grid(row = 4, column = 0, columnspan = 2)



def query6():
    query6_pop = Toplevel(root)
    query6_pop.geometry("500x500")
    query6_pop.title("query6a")

    info = Label(query6_pop, text="Search For Borrower's information by entering ID or name or None \n"
                                  "the Output will be in the following order: Card_no, Name, LateFeeBalance \n", fg="BLUE")
    info.grid(row=0, column=1, padx=20)

    borrower = Entry(query6_pop, width=60)
    borrower.grid(row=1, column=1, padx=20)
    borrower_label = Label(query6_pop, text='BorrowerID: ', fg="BLUE")
    borrower_label.grid(row=1, column=0)

    name = Entry(query6_pop, width=60)
    name.grid(row=2, column=1, padx=20)
    name_label = Label(query6_pop, text='Name: ', fg="BLUE")
    name_label.grid(row=2, column=0)

    submit_btn = Button(query6_pop, text='SEARCH ', bg="BLUE", fg="WHITE", command=lambda: submit6(borrower.get(), name.get(), query6_pop))
    submit_btn.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

    query6_pop.mainloop()

def submit6(id, nme, query6_pop):
    submit_conn = sqlite3.connect('lms.db')
    submit_cur = submit_conn.cursor()

    try:
        if (id == "" and nme != ""):
            submit_cur.execute("SELECT DISTINCT vBookLoanInfo.Card_no, BORROWER.Name, IFNULL(LateFeeBalance, 0) "
                               "FROM BORROWER "
                               "LEFT JOIN vBookLoanInfo ON BORROWER.Card_no = vBookLoanInfo.Card_no "
                               "WHERE BORROWER.Name LIKE '%'||?||'%'",
                               (nme,))
        elif (nme == "" and id != ""):
            submit_cur.execute("SELECT DISTINCT vBookLoanInfo.Card_no, BORROWER.Name, IFNULL(LateFeeBalance, 0) "
                               "FROM vBookLoanInfo "
                               "LEFT JOIN BORROWER ON vBookLoanInfo.Card_no = BORROWER.Card_no "
                               "WHERE vBookLoanInfo.Card_no = ?",
                               (id,))
        elif (nme != "" and id != ""):
            submit_cur.execute("SELECT DISTINCT vBookLoanInfo.Card_no, BORROWER.Name, IFNULL(LateFeeBalance, 0) "
                               "FROM vBookLoanInfo "
                               "LEFT JOIN BORROWER ON vBookLoanInfo.Card_no = BORROWER.Card_no "
                               "WHERE vBookLoanInfo.Card_no = ? AND BORROWER.Name LIKE '%'||?||'%'",
                               (id, nme,))
        else:
            submit_cur.execute("SELECT DISTINCT vBookLoanInfo.Card_no, BORROWER.Name, IFNULL(LateFeeBalance, 0) "
                               "FROM vBookLoanInfo "
                               "LEFT JOIN BORROWER ON vBookLoanInfo.Card_no = BORROWER.Card_no "
                               "ORDER BY LateFeeBalance DESC")
    except sqlite3.Error as e:
        print('Error Select failed:', e)

    output_records = submit_cur.fetchall()
    print_record = ''
    for output_record in output_records:
        print_record += ("{},{},${:.2f} \n".format(output_record[0], output_record[1], output_record[2]))

    iq_label = Label(query6_pop, text=print_record)
    iq_label.grid(row=4, column=0, columnspan=2)

    # close the DB connection
    submit_cur.close()
    submit_conn.close()

#Buttons on the main window
query1_btn = Button(root, text='QUERY-1', bg="BLUE", fg="WHITE", command=query1)
query1_btn.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

q2_btn = Button(root, text='QUERY-2', bg="BLUE", fg="WHITE", command=q2)
q2_btn.grid(row=1, column=0, columnspan=2, pady=5, padx=5)

q3_button = Button(root, text='QUERY-3', bg="BLUE", fg="WHITE", command=q3)
q3_button.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

q4_btn = Button(root, text='QUERY-4', bg="BLUE", fg="WHITE", command=q4)
q4_btn.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

query5_btn = Button(root, text='QUERY-5', bg="BLUE", fg="WHITE", command=query5)
query5_btn.grid(row=4, column=0, columnspan=2, pady=5, padx=5)

query6_btn = Button(root, text='QUERY-6A', bg="BLUE", fg="WHITE", command=query6)
query6_btn.grid(row=5, column=0, columnspan=2, pady=5, padx=5)

q6b_btn = Button(root, text='QUERY-6B', bg="BLUE", fg="WHITE", command=query6b)
q6b_btn.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

# Configure columns to center the buttons
root.columnconfigure(0, weight=1)

root.mainloop()