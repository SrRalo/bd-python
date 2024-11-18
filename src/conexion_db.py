import mysql.connector

class ConexionBD:
    def __init__(self, host='localhost', user='root', password='', database='evaluaciones2', port='3306'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.conn = None
        self.cursor = None

    def conectar(self):
        if self.conn is None:
            try:
                self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    port=self.port
                )
                self.cursor = self.conn.cursor()
                print("Conexión exitosa a la base de datos")
            except mysql.connector.Error as err:
                print(f"Error de conexión: {err}")
                return None
        return self.conn

    def cerrar_conexion(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            self.conn = None
            print("Conexión cerrada.")
