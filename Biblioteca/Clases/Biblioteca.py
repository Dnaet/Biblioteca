class Biblioteca:
    def __init__(self, id_biblioteca, nombre_biblioteca, direccion_biblioteca, telefono_biblioteca):
        self.id_biblioteca = id_biblioteca
        self.nombre_biblioteca = nombre_biblioteca
        self.direccion_biblioteca = direccion_biblioteca
        self.telefono_biblioteca = telefono_biblioteca

    def buscar_libro(self, isbn):
        pass  

    def devolver_libro(self, libro):
        pass  

    def prestar_libro(self, libro, usuario):
        pass  

    def info(self):
        return f"Biblioteca: {self.nombre_biblioteca}, Dirección: {self.direccion_biblioteca}, Teléfono: {self.telefono_biblioteca}"


import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="mike",
    password="s3cre3t!")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# Close connection
cnx.close()