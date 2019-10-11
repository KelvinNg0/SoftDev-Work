#Team omegalul Kelvin Ng & David Xiedeng
#SoftDev1 pd1
#K18 -- Average
#2019-10-10

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

c.execute("CREATE TABLE IF NOT EXISTS courses(code STRING, mark INTEGER, id INTEGER)") #checks to see if table exists before creating it
c.execute("DELETE FROM courses")	#clears the table if it already has values in it

with open('courses.csv', 'r') as csvCourse:
	readCourse = csv.DictReader(csvCourse)	#creates a dictionary from csvCourse
	for row in readCourse:
		c.execute("INSERT INTO courses(code, mark, id) VALUES (' "+ row['code'] +" ' , "+ row['mark'] +", "+ row['id'] +") ")
		#for every row in readCourse, insert the values of 'code', 'mark', and 'id' into the courses table and into their respective categories


c.execute("CREATE TABLE IF NOT EXISTS students(name STRING, age INTEGER, id INTEGER)") #checks to see if table exists before creating it
c.execute("DELETE FROM students")	#clears the table if it already has values in it

with open('students.csv', 'r') as csvStudent:
	readStudent = csv.DictReader(csvStudent)	#creates a dictionary from csvStudent
	for row in readStudent:
		c.execute("INSERT INTO students(name, age, id) VALUES (' "+ row['name'] +" ' , "+ row['age'] +", "+ row['id'] +") ")
		#for every row in readStudent, insert the values of 'name', 'age', and 'id' into the students table and into their respective categories


c.execute("CREATE TABLE IF NOT EXISTS stu_avg(id INTEGER, avg INTEGER)") #checks to see if table exists before creating it
c.execute("DELETE FROM stu_avg")


c.execute("SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id")
rows = c.fetchall()
stu = rows[0][0]
stuID = rows[0][1]
avg = 0
count = 0
print(rows)
for row in rows:
	if stu == row[0]:
		count += 1
		avg += row[2]
	else:
		avg /= count
		print(stu, stuID, avg)
		c.execute("INSERT INTO stu_avg(id, avg) VALUES (' "+ str(stuID) +" ', " + str(avg) +")")
		count = 1
		avg = row[2]
		stu = row[0]
		stuID = row[1]

c.execute("SELECT * FROM stu_avg")
print(c.fetchall())

#==========================================================

db.commit() #save changes
db.close()  #close database
