
import analysis
import createdb
import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import equries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import mysql.connector as mq

data = pd.read_csv('Employee_Dataset.csv', index_col=False, delimiter=',')

createdb.cdb(data)

con = mq.connect(host='localhost', database='emp_db', user='root', password='9868')


def data_analysis(df):
    window = tk.Toplevel(root)
    window.title("Data Analysis")
    figure = plt.Figure(figsize=(8, 7), dpi=100)
    ax = figure.add_subplot(211)
    chart_type = FigureCanvasTkAgg(figure, window)
    chart_type.get_tk_widget().pack()
    gdf = df[['EmpDepartment', 'PerformanceRating']].groupby('EmpDepartment').sum()
    gdf.plot(kind='bar', legend=True, ax=ax)


def performance_rating():
    window = tk.Toplevel(root)
    window.title("Performance Rating")
    window.geometry('805x450+388+154')

    tk.Label(window, text="Enter Employee ID", font=("Helvetica", 14)).place(x=150, y=50)
    emp_id = tk.Entry(window, font=("Helvetica", 11), width=42)
    emp_id.place(x=340, y=60, height=25)
    tk.Label(window, text="Enter Performance Rating (1 to 5)", font=("Helvetica", 14), bg='#F4CE82').place(x=150, y=110)
    emp_rating = tk.Entry(window, font=("Helvetica", 11), width=26)
    emp_rating.place(x=470, y=110, height=25)
    tk.Label(window, text="Update Performance Ranking for ....", font=("Helvetica", 14), bg='#F4CE82').place(x=150,
                                                                                                             y=160)

    tk.Button(window, text="Update Rating", width=18, font=('Times New Roman', 16),
              command=lambda: equries.prate(emp_id.get(), emp_rating.get())).place(x=300, y=180)


def search_analysis():
    window = tk.Toplevel(root)
    window.title("Search Employees / Show Data Analysis")
    window.geometry('802x420+390+182')
    window.resizable(0, 0)

    l_g = ['Male', 'Female']
    l_eb = ['Marketing', 'Life Sciences', 'Human Resources', 'Medical', 'Other', 'Technical Degree']
    l_ed = ['Sales', 'Human Resources', 'Development', 'Data Science', 'Research & Development', 'Finance']
    l_ej = ['Sales Executive', 'Manager', 'Developer', 'Sales Representative', 'Human Resources', 'Senior Developer',
            'Data Scientist', 'Senior Manager R&D', 'Laboratory Technician', 'Manufacturing Director',
            'Research Scientist', 'Healthcare Representative', 'Research Director', 'Manager R&D', 'Finance Manager',
            'Technical Architect', 'Business Analyst', 'Technical Lead']

    def p_sub(e):
        if option_clicked.get() == "Gender":
            sub_option.config(values=l_g)
            sub_option.current(0)
        if option_clicked.get() == "EducationBackground":
            sub_option.config(values=l_eb)
            sub_option.current(0)
        if option_clicked.get() == "EmpDepartment":
            sub_option.config(values=l_ed)
            sub_option.current(0)
        if option_clicked.get() == "EmpJobRole":
            sub_option.config(values=l_ej)
            sub_option.current(0)

    tk.Label(window, text="Choose Category", font=("Helvetica", 16)).place(x=90, y=50, rely=0)
    clicked = tk.StringVar()
    option_clicked = ttk.Combobox(window, width=35, textvariable=clicked)
    option_clicked['values'] = (
    'Gender', 'EducationBackground', 'EmpDepartment', 'EmpJobRole')  ##### Here the column names will be be shown
    option_clicked.grid(padx=90, pady=100)
    option_clicked.current(0)

    option_clicked.bind("<Button-1>", p_sub)

    tk.Label(window, text="Choose sub-category", font=("Helvetica", 16)).place(x=480, y=50, rely=0)
    clicked_sub = tk.StringVar()
    sub_option = ttk.Combobox(window, width=35, textvariable=clicked_sub)
    sub_option['values'] = ()
    ###### Here the unique values from the chosen column will be shown
    sub_option.grid(row=0, column=2, padx=70, pady=0)

    tk.Button(window, text="Search for Employees", width=18, font=('Times New Roman', 16),
              command=lambda: pfetch(clicked.get(), clicked_sub.get())).place(x=300, y=220)

def pfetch(r, t):
    cursor = con.cursor()
    if r == 'Gender':
        q = "Select FullName,Gender,EmpDepartment,EmpJobRole,PerformanceRating from emp_db.emp_table WHERE Gender = %s ;"
    elif r == 'EmpDepartment':
        q = "Select FullName,EmpDepartment,EmpJobRole,PerformanceRating from emp_db.emp_table WHERE EmpDepartment = %s ;"
    elif r == 'EducationBackground':
        q = "Select FullName,EducationBackground,EmpDepartment,EmpJobRole,PerformanceRating from emp_db.emp_table WHERE EducationBackground = %s ;"
    elif r == 'EmpJobRole':
        q = "Select FullName,EmpDepartment,EmpJobRole,PerformanceRating from emp_db.emp_table WHERE EmpJobRole = %s ;"

    cursor.execute(q, (t,))
    columns = cursor.description
    df = pd.DataFrame([{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()])
    details_win = tk.Toplevel(root)
    details_win.geometry('850x500+365+132')

    n_rows = df.shape[0]
    n_cols = df.shape[1]

    column_names = df.columns
    i = 0
    for j, col in enumerate(column_names):
        text = Text(details_win, width=16, height=1, bg="#9BC2E6")
        text.grid(row=i, column=j)
        text.insert(INSERT, col)

    # adding all the other rows into the grid
    for i in range(n_rows):
        for j in range(n_cols):
            text = Text(details_win, width=16, height=1)
            text.grid(row=i + 1, column=j)
            text.insert(INSERT, df.loc[i][j])

root = tk.Tk()
root.title('Employee Management System')
root.geometry('800x420+390+182')
tk.Label(root, text="Employee Analysis Portal", font=('Helvetica', 18, "underline"), wraplength=400).place(x=260, y=50)
tk.Button(root, text='Enter Performance Ratings', width=20, font=('Times New Roman', 16),
          command=lambda: performance_rating()).place(
    x=274, y=140)
tk.Button(root, text='Search Employees', width=20, font=('Times New Roman', 16),
          command=lambda: search_analysis()).place(x=274, y=210)
tk.Button(root, text='Perform Data Analysis', width=20, font=('Times New Roman', 16),
          command=lambda: data_analysis(analysis.analyse())).place(x=274, y=280)
root.update()
root.mainloop()





