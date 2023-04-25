import tkinter as tk
import mysql.connector as mq


con = mq.connect(host='localhost', database='emp_db', user='root', password='9868')

def prate(window,x, y):
    try:
        if con.is_connected():
            print("Connected")
            cursor = con.cursor()
            e_id = x
            rate = y
            q = "Update emp_table set PerformanceRating=" + rate + " where EmployeeID=%s"
            cursor.execute(q, (e_id,))
            con.commit()
            tk.Label(window, text="Record Updated successfully", font=('Helvetica', 14), bg='#e7c6ff').place(x=282,
                                                                                                             y=310)
    except Exception as e:
        error_msg = "Error while connecting to MySQL"
        tk.Label(window, text=error_msg, font=("Helvetica", 14), bg="#F4CE82").place(x=282, y=310)
