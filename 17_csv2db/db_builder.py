#Team 5head Kelvin Ng
#SoftDev1 pd1
#K17 -- No Trouble
#2019-10-7

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

command = "CREATE TABLE courses(code STRING, mark INTEGER, id INTEGER)"
c.execute(command)

with open('courses.csv', 'r') as csvCourse:			#remove the header
	readCourse = csv.DictReader('csvCourse')
	for row in readCourse:
		command = ""

#==========================================================

db.commit() #save changes
db.close()  #close database
