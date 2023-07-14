from services import fake_student

class Student:

    def __init__(self, fname, lname, email):
        self.first_name = fname
        self.last_name = lname
        self.email = email

    def getStudents():
        student_data = []

        for student in all_students:
            student_data.append({
                'first_name': student.first_name,
                'last_name': student.last_name,
                'email': student.email
            })
        return student_data

    def getStudentByID(id):
        id = int(id)
        student_data = ({

            'first_name': all_students[id].first_name,
            'last_name': all_students[id].last_name,
            'email': all_students[id].email
        })
        return student_data
    
    #create a new student
    def postStudent(student):
        mystudent = fake_student.Student(student.first_name, student.last_name, student.email)
        all_students.extend([mystudent])
        return 'Student Created successfuly'

    def updateStudent(student, id):
        id = int(id)
        mystudent = fake_student.Student(student.first_name, student.last_name, student.email)
        all_students[id] = mystudent

        student_data = ({

            'first_name': all_students[id].first_name,
            'last_name': all_students[id].last_name,
            'email': all_students[id].email
        })
        return student_data

    
    def deleteStudent(id):
        id = int(id)
        all_students.remove(all_students[id])
        return 'Student deleted successfully'

student1 = fake_student.Student('Augusto', 'Splett', 'augusto@gmail.com')
student2 = fake_student.Student('Priscilla', 'Silva', 'priscilla@gmail.com')
student3 = fake_student.Student('Cecilia', 'Luz', 'cecilia@gmail.com')

all_students = []
all_students.extend([student1, student2, student3])

