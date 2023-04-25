import mysql.connector as mq
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import pandas as pd

con = mq.connect(host='localhost', database='emp_db', user='root', password='9868')

def analyse():
    q = 'Select * from emp_table'
    df = pd.read_sql(q, con)
    return df


