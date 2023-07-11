from flask import Flask, request, jsonify
from flask_cors import CORS
from services.student import Student

app = Flask(__name__)
cors = CORS(app)

#Students
@app.route("/student")
def get_all_users():
    return jsonify(Student.getStudents()), 200

@app.route("/student/<user_id>")
def get_user(user_id):
    return jsonify(Student.getStudentByID(user_id)),200
    

@app.route("/student", methods=["Post"])
def create_user():
    data = request.get_json()
    student = Student(data['first_name'], data['last_name'], data['email'])
    return jsonify(Student.postStudent(student)), 201

@app.route("/student/<user_id>", methods=["Put"])
def update_user(user_id):
    data = request.get_json()
    student = Student(data['first_name'], data['last_name'], data['email'])
    return jsonify(Student.updateStudent(student, user_id)), 201

@app.route("/student/<user_id>", methods=["Delete"])
def delete_user(user_id):
    Student.deleteStudent(user_id)
    return "Student deleted successfully", 200

if __name__ == "__main__":
    app.run(debug=True)