#Read a file and wirte into DB.
import re
import cx_Oracle
from pprint import pprint
connstr = 'vjdabur/Jan_2018@localhost:1521/xe'
db = cx_Oracle.connect(connstr)
cursor = db.cursor();
#cursor.execute("insert into python_modules values(:1,:2)");
statement="insert into python_modules values(:1,:2)";

with open("ReadFile.txt","r") as f:
	for line in f:
		#print("first line read")
		for word in line.split():
			matchobj=re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+',word)
			#print(word)
			#matchobj=re.search(r'',word)			
			for matchobj in matchobj:
 				 cursor.execute(statement,('Email',matchobj));
db.commit()
cursor.execute("select * from python_modules");
print(cursor);
for row in cursor:
	pprint(row)
