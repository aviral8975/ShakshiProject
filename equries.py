import analysis as anal
import mysql.connector as mq

#class Choice:

#    ch=0
#   def __init__(self):
#        self.ch = int(input('Enter choice:'))
#        emp.start()
#        return self.ch

con= mq.connect(host='localhost', database = 'emp_db', user = 'root', password = '9868')

def dfetch(r, t):
    cursor = con.cursor()
    if r == 'Gender':
        q = "Select * from emp_db.emp_table WHERE Gender = %s ;"
    elif r == 'EmpDepartment':
        q = "Select * from emp_db.emp_table WHERE EmpDepartment = %s ;"
    elif r == 'EducationBackground':
        q = "Select * from emp_db.emp_table WHERE EducationBackground = %s ;"
    elif r == 'EmpJobRole':
        q = "Select * from emp_db.emp_table WHERE EmpJobRole = %s ;"

    cursor.execute(q, (t,))
    res = cursor.fetchall()
    print(pd.DataFrame(res))

def prate(x,y):
    cursor = con.cursor()
    e_id = x
    rate = y
    q = "Update emp_table set PerformanceRating=%s where EmployeeID= %s"
    cursor.execute(q, (rate, e_id,))
    con.commit()
    print("Record Updated successfully ")





