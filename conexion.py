# Jonathan Gabriel Morales Torres
# Guía de aprendizaje #1 - Tercera unidad

#pip install mysql-connector-python

# Importa la librería mysql.connector para conectar Python con MySQL
import mysql.connector

# Define una función llamada obtener_conexion
def obtener_conexion():

    # Crea la conexión con la base de datos MySQL
    conexion = mysql.connector.connect(

        # Indica que MySQL está instalado en la misma computadora
        host="localhost",

        # Indica el usuario de MySQL
        user="root",

        # Indica la contraseña del usuario root de MySQL
        password="admin",

        # Indica el nombre de la base de datos que se va a utilizar
        database="restaurante_db"
    )

    # Devuelve la conexión para poder usarla en otros archivos
    return conexion