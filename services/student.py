#consuming the conection information from Database.py
from services.DataBase import *

class Student:
    def __init__(self, fname, lname, email):
        self.first_Name = fname
        self.last_Name = lname
        self.email = email

    def getStudents():
        query = "select * from Students;"
        cursor = cnx.cursor()
        cursor.execute(query)
        names = cursor.fetchall()
        #cnx.close()
        return names

    def getStudentByID(id):
        query = f"select * from Students where id={id};"
        cursor = cnx.cursor()
        cursor.execute(query)
        name = cursor.fetchall()
        #cnx.close()
        return name
    
    #create a new student
    def postStudent(student):
        print(student.first_Name)
        query = f"insert into Students(first_Name, last_Name, email) values ('{student.first_Name}', '{student.last_Name}', '{student.email}');"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        id = cursor.lastrowid
        newStudent = Student.getStudentByID(id)
        #cnx.close()
        return newStudent

    def updateStudent(student, id):
        query = f"UPDATE Students SET First_Name ='{student.first_Name}', Last_Name = '{student.last_Name}', email= '{student.email}' where id='{id}';"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        newStudent = Student.getStudentByID(id)
        cursor.close()
        #cnx.close()
        return newStudent

    def deleteStudent(id):
        query = f"DELETE FROM Students WHERE id={id};"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        #cnx.close()
        return True