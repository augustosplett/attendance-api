#consuming the conection information from Database.py
from services.DataBase import *

class Course:
    def __init__(self, name):
        self.Name = name

    def getCourses():
        query = "select * from Courses;"
        cursor = cnx.cursor()
        cursor.execute(query)
        courses = cursor.fetchall()
        cnx.close()
        return courses

    def getCourseByID(id):
        query = f"select * from Courses where id={id};"
        cursor = cnx.cursor()
        cursor.execute(query)
        course = cursor.fetchall()
        cnx.close()
        return course
    #create a new course
    def postCourse(course):
        query = f"insert into Courses(Name) values ('{course.Name}');"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        id = cursor.lastrowid
        newCourse = Course.getCourseByID(id)
        cnx.close()
        return newCourse

    def updateCourse(course, id):
        query = f"UPDATE Courses SET NAME ='{course.Name}' where id='{id}';"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        newCourse = Course.getCourseByID(id)
        cursor.close()
        cnx.close()
        return newCourse

    def deleteCourse(id):
        query = f"DELETE FROM Courses WHERE id={id};"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True