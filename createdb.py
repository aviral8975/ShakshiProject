import mysql.connector as mq
from mysql.connector import Error

def cdb(x):
    try:
        con= mq.connect(host='localhost', database = 'emp_db', user = 'root', password = '9868')
        if con.is_connected():
            cursor=con.cursor()
            cursor.execute('select database();')
            rec=cursor.fetchone()
            print('connected', rec)
            cursor.execute('DROP TABLE IF EXISTS emp_table;')
            cursor.execute("CREATE TABLE emp_table(EmployeeID varchar(50) NOT NULL, FullName varchar(255) NOT NULL, Gender varchar(10) NOT NULL, Age int,  HireDate varchar(50) NOT NULL, EducationBackground varchar(50),MaritalStatus varchar(50),EmpDepartment varchar(50), EmpJobRole varchar(50), BusinessTravelFrequency varchar(50), AnnualSalary int, DistanceFromHome int, EmpEducationLevel int, EmpEnvironmentSatisfaction int, EmpHourlyRate int, EmpJobInvolvement int, EmpJobLevel int, EmpJobSatisfaction int, NumCompaniesWorked int, OverTime varchar(10), EmpLastSalaryHikePercent int, EmpRelationshipSatisfaction int, TotalWorkExperienceInYears int, TrainingTimesLastYear int, EmpWorkLifeBalance int, ExperienceYearsAtThisCompany int, ExperienceYearsInCurrentRole int, YearsSinceLastPromotion int, YearsWithCurrManager int, Attrition varchar(10), PerformanceRating int, PRIMARY KEY(EmployeeID))")
            print('table created')
            for i,r in x.iterrows():
                sql = "INSERT INTO emp_db.emp_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, tuple(r))
                print('row inserted')
                con.commit()

    except Error as e:
        print("Error while connecting to MySQL",e)