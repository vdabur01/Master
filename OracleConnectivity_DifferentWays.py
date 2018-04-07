import pandas as pd
import numpy
import cx_Oracle
#print(dir(cx_Oracle))
Employee_Data = pd.read_csv("../data_set.csv",sep=',', usecols=[1,2]);

#===================================================Convert Pandas to Numpy
npd=Employee_Data.reset_index().values
print(npd)
#===================================================

Employee_Data.sort_values(by=['Employee_Salary'],ascending=False,inplace=True)
print(Employee_Data.Employee_Salary.iloc[1])

#===================================================One Way
connstr = 'vjdabur/Jan_2018@localhost:1521/xe'
db = cx_Oracle.connect(connstr)
con=db.cursor()
con.execute("select * from python_modules")
data=con.fetchall()

for row in data:
	print(row)
#===============2nd Way with Pandas Dataframe=================

connstr = 'vjdabur/Jan_2018@localhost:1521/xe'
db = cx_Oracle.connect(connstr)
query="select * from python_modules"
data=pd.read_sql(query,db)
for index,row in data.iterrows():
	print(row['MODULE_NAME'])

#=====================================================3rd way======
from pandas.io import sql
sql.execute('SELECT * FROM table_name', engine)


#Data Set from csv
# Emlpoyee_ID,Emloyee_Name,Employee_Salary
# 1,vijay,10000
# 2,Ankit,20000
# 3,Bose,12000
# 4,Sunil,50000
