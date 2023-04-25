import analysis as anal
import mysql.connector as mq

#class Choice:

#    ch=0
#   def __init__(self):
#        self.ch = int(input('Enter choice:'))
#        emp.start()
#        return self.ch

con= mq.connect(host='localhost', database = 'emp_db', user = 'root', password = '9868')

def prate(x,y):
    cursor = con.cursor()
    e_id = x
    rate = y
    q = "Update emp_table set PerformanceRating=%s where EmployeeID= %s"
    cursor.execute(q, (rate, e_id,))
    con.commit()
    print("Record Updated successfully ")





