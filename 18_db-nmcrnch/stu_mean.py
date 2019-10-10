print(c.execute("SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"))
