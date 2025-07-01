import mysql.connector

class mysql_connect():

    conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="vet"
    )

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM cliente")
    for fila in cursor.fetchall():
        print(fila)

    cursor.close()
    conexion.close()


mysql_connect()