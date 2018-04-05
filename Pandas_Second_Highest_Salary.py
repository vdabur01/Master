import pandas as pd

Employee_Data = pd.read_csv("../data_set.csv",sep=',', usecols=[1,2]);
Employee_Data.sort_values(by=['Employee_Salary'],ascending=False,inplace=True)
print(Employee_Data.Employee_Salary.iloc[1])



#Data Set from csv
# Emlpoyee_ID,Emloyee_Name,Employee_Salary
# 1,vijay,10000
# 2,Ankit,20000
# 3,Bose,12000
# 4,Sunil,50000
