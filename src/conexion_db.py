import mysql.connector

conexio = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='evaluaciones2',
    port='3306'
)

print("conexion")