import mysql.connector as mq
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import pandas as pd

con = mq.connect(host='localhost', database='emp_db', user='root', password='9868')

def analyse():
    q = 'Select * from emp_table'
    df = pd.read_sql(q, con)
    return df
def show_chart(df, x,y):
    window = tk.Tk()
    window.title("Data Analysis")
    window.geometry('1080x720')
    window.config(bg="#FFFFFF")
    figure = plt.Figure(figsize=(5, 7), dpi=120)
    ax = figure.add_subplot(211)
    chart_type = FigureCanvasTkAgg(figure, window)
    chart_type.get_tk_widget().pack()
    print(x)
    print(y)
    gdf = df[[x, y]].groupby(x).sum()
    gdf.plot(kind='bar', legend=True, ax=ax)



