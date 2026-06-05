# Jonathan Gabriel Morales Torres
# Guía de aprendizaje #1 - Tercera unidad
# Importa la función obtener_conexion desde el archivo conexion.py
from conexion import obtener_conexion

# Define una función llamada iniciar_sesion
def iniciar_sesion():

    # Crea una conexión con la base de datos
    conexion = obtener_conexion()

    # Crea un cursor para ejecutar instrucciones SQL
    cursor = conexion.cursor()

    # Muestra el título del login
    print("===== 🍽️ BIENVENIDO AL SISTEMA DEL RESTAURANTE =====")

    # Inicia un bucle que se repetirá hasta que el usuario ingrese datos correctos
    while True:

        # Solicita el nombre de usuario
        usuario = input("Usuario: ")

        # Solicita la contraseña del usuario
        contraseña = input("Contraseña: ")

        # Consulta SQL que busca el rol del usuario si el usuario y contraseña coinciden
        sql = "SELECT rol FROM usuarios WHERE usuario = %s AND contraseña = %s"

        # Guarda los valores que se enviarán a la consulta SQL
        valores = (usuario, contraseña)

        # Ejecuta la consulta SQL con los valores ingresados por el usuario
        cursor.execute(sql, valores)

        # Obtiene un solo resultado de la consulta
        resultado = cursor.fetchone()

        # Verifica si se encontró un usuario válido
        if resultado:

            # Guarda el rol encontrado en la variable rol
            rol = resultado[0]

            # Muestra un mensaje de bienvenida con el nombre del usuario
            print(f"\n👋 Bienvenido, {usuario}")

            # Muestra el rol del usuario
            print(f"🔑 Rol: {rol}\n")

            # Cierra el cursor
            cursor.close()

            # Cierra la conexión con la base de datos
            conexion.close()

            # Devuelve el rol para que main.py sepa qué menú mostrar
            return rol

        # Si no se encontró usuario, muestra mensaje de error
        else:

            # Informa que los datos son incorrectos
            print("\n❌ Usuario o contraseña incorrectos. Intente nuevamente.\n")