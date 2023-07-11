#consuming the conection information from Database.py
from services.DataBase import *

class Professor:
    def __init__(self, name):
        self.Name = name

    def getProfessors():
        query = "select * from Professors;"
        cursor = cnx.cursor()
        cursor.execute(query)
        names = cursor.fetchall()
        cnx.close()
        return names

    def getProfessorByID(id):
        query = f"select * from Professors where id={id};"
        cursor = cnx.cursor()
        cursor.execute(query)
        name = cursor.fetchall()
        cnx.close()
        return name
    #create a new professor
    def postProfessor(professor):
        query = f"insert into Professors(Name) values ('{professor.Name}');"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        id = cursor.lastrowid
        newProfessor = Professor.getProfessorByID(id)
        cnx.close()
        return newProfessor

    def updateProfessor(professor, id):
        query = f"UPDATE Professors SET NAME ='{professor.Name}' where id='{id}';"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        newProfessor = Professor.getProfessorByID(id)
        cursor.close()
        cnx.close()
        return newProfessor

    def deleteProfessor(id):
        query = f"DELETE FROM Professors WHERE id={id};"
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True