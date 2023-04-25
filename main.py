import pandas as pd

import analysis
import createdb
import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import equries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


data = pd.read_csv('Employee_Dataset.csv', index_col=False, delimiter=',')

createdb.cdb(data)

def show_emp():
    details_win = tk.Toplevel(root)
    details_win.geometry('850x500+365+132')

    h = Scrollbar(details_win, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)

    v = Scrollbar(details_win)
    v.pack(side=RIGHT, fill=Y)

    t = Text(details_win, width=80, height=50, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)

    for i in range(200):
        t.insert(END, "this is some text jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj\n")

    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)

    details_win.lift()


def data_analysis(df):
    window = tk.Toplevel(root)
    window.title("Data Analysis")
    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
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
    tk.Label(window, text="Update Performance Ranking for ....", font=("Helvetica", 14), bg='#F4CE82').place(x=150, y=160)

    tk.Button(window, text="Update Rating", width=18, font=('Times New Roman', 16), command=lambda : equries.prate(emp_id.get(), emp_rating.get())).place(x=300, y=180)


def search_analysis():
    window = tk.Toplevel(root)
    window.title("Search Employees / Show Data Analysis")
    window.geometry('802x420+390+182')
    window.resizable(0, 0)

    l_g = ['Male', 'Female']
    l_eb = ['Marketing','Life Sciences','Human Resources','Medical','Other','Technical Degree']
    l_ed = ['Sales','Human Resources','Development','Data Science','Research & Development','Finance']
    l_ej = ['Sales Executive','Manager','Developer','Sales Representative','Human Resources','Senior Developer','Data Scientist','Senior Manager R&D','Laboratory Technician','Manufacturing Director','Research Scientist','Healthcare Representative','Research Director','Manager R&D','Finance Manager','Technical Architect','Business Analyst','Technical Lead']

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
    option_clicked['values'] = ('Gender', 'EducationBackground', 'EmpDepartment', 'EmpJobRole')  ##### Here the column names will be be shown
    option_clicked.grid(padx=90, pady=100)
    option_clicked.current(0)

    option_clicked.bind("<Button-1>",p_sub)

    tk.Label(window, text="Choose sub-category", font=("Helvetica", 16)).place(x=480, y=50, rely=0)
    clicked_sub = tk.StringVar()
    sub_option = ttk.Combobox(window, width=35, textvariable=clicked_sub)
    sub_option['values'] = ()
    ###### Here the unique values from the chosen column will be shown
    sub_option.grid(row=0, column=2, padx=70, pady=0)

    tk.Button(window, text="Search for Employees", width=18, font=('Times New Roman', 16),
              command=lambda: equries.dfetch(clicked.get(),clicked_sub.get())).place(x=300, y=220)



root = tk.Tk()
root.title('Employee Management System')
root.geometry('800x420+390+182')
tk.Label(root, text="Employee Analysis Portal", font=('Helvetica', 18, "underline"), wraplength=400).place(x=260, y=50)
tk.Button(root, text='Enter Performance Ratings', width=20, font=('Times New Roman', 16), command=lambda: performance_rating()).place(
    x=274, y=140)
tk.Button(root, text='Search Employees', width=20, font=('Times New Roman', 16),
          command=lambda: search_analysis()).place(x=274, y=210)
tk.Button(root, text='Perform Data Analysis', width=20, font=('Times New Roman', 16),
          command=lambda: data_analysis(analysis.analyse())).place(x=274, y=280)
root.update()
root.mainloop()





