import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="attendance",
    password="password",
    database="attendance",
    auth_plugin='mysql_native_password'
)

