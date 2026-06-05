# Jonathan Gabriel Morales Torres
# Guía de aprendizaje #1 - Tercera unidad

# Importa la función obtener_conexion desde el archivo conexion.py
from conexion import obtener_conexion

# Define una función para mostrar los platillos registrados
def mostrar_platillos():

    # Crea una conexión con la base de datos
    conexion = obtener_conexion()

    # Crea un cursor para ejecutar instrucciones SQL
    cursor = conexion.cursor()

    # Ejecuta una consulta SQL para obtener el id y nombre de todos los platillos
    cursor.execute("SELECT id, nombre FROM platillos")

    # Guarda todos los resultados de la consulta en la variable platillos
    platillos = cursor.fetchall()

    # Verifica si la lista de platillos está vacía
    if len(platillos) == 0:

        # Muestra mensaje si no hay platillos registrados
        print("\n📋 No hay platillos en el menú.\n")

    # Si sí hay platillos registrados
    else:

        # Muestra el título del menú
        print("\n===== 🍴 MENÚ DEL RESTAURANTE =====")

        # Recorre cada platillo obtenido desde la base de datos
        for platillo in platillos:

            # Muestra el id y el nombre del platillo
            print(f"{platillo[0]}. {platillo[1]}")

        # Imprime una línea en blanco
        print()

    # Cierra el cursor
    cursor.close()

    # Cierra la conexión con la base de datos
    conexion.close()


# Define una función para agregar platillos
def agregar_platillo():

    # Crea una conexión con la base de datos
    conexion = obtener_conexion()

    # Crea un cursor para ejecutar instrucciones SQL
    cursor = conexion.cursor()

    # Solicita al usuario el nombre del platillo y elimina espacios innecesarios
    platillo = input("Ingrese el nombre del platillo: ").strip()

    # Verifica si el usuario escribió algo
    if platillo:

        # Prepara la consulta SQL para insertar un platillo
        sql = "INSERT INTO platillos (nombre) VALUES (%s)"

        # Guarda el nombre del platillo en una tupla
        valores = (platillo,)

        # Ejecuta la consulta SQL con el valor ingresado
        cursor.execute(sql, valores)

        # Guarda definitivamente el cambio en la base de datos
        conexion.commit()

        # Muestra mensaje de confirmación
        print(f"\n✅ Platillo '{platillo}' agregado al menú correctamente.\n")

    # Si el usuario no escribió nada
    else:

        # Muestra advertencia
        print("\n⚠️ No puede ingresar un platillo vacío.\n")

    # Cierra el cursor
    cursor.close()

    # Cierra la conexión con la base de datos
    conexion.close()


# Define una función para eliminar platillos
def eliminar_platillo():

    # Crea una conexión con la base de datos
    conexion = obtener_conexion()

    # Crea un cursor para ejecutar instrucciones SQL
    cursor = conexion.cursor()

    # Solicita el nombre del platillo que se desea eliminar
    platillo = input("Ingrese el nombre del platillo a eliminar: ").strip()

    # Prepara la consulta SQL para eliminar el platillo por nombre
    sql = "DELETE FROM platillos WHERE nombre = %s"

    # Guarda el nombre del platillo en una tupla
    valores = (platillo,)

    # Ejecuta la consulta SQL
    cursor.execute(sql, valores)

    # Guarda definitivamente el cambio en la base de datos
    conexion.commit()

    # Verifica si se eliminó al menos un registro
    if cursor.rowcount > 0:

        # Muestra mensaje si el platillo fue eliminado
        print(f"\n🗑️ Platillo '{platillo}' eliminado del menú correctamente.\n")

    # Si no se eliminó ningún registro
    else:

        # Muestra mensaje indicando que el platillo no existe
        print(f"\n⚠️ El platillo '{platillo}' no existe en el menú.\n")

    # Cierra el cursor
    cursor.close()

    # Cierra la conexión con la base de datos
    conexion.close()


# Define el menú para el administrador
def menu_administrador():

    # Inicia un bucle para mostrar el menú repetidamente
    while True:

        # Muestra el título del menú administrador
        print("===== 👨‍🍳 MENÚ ADMINISTRADOR =====")

        # Muestra la opción para agregar platillos
        print("1. Agregar un platillo")

        # Muestra la opción para eliminar platillos
        print("2. Eliminar un platillo")

        # Muestra la opción para mostrar el menú
        print("3. Ver menú del restaurante")

        # Muestra la opción para salir
        print("4. Salir")

        # Solicita al usuario una opción
        opcion = input("Seleccione una opción: ")

        # Si el usuario elige la opción 1
        if opcion == "1":

            # Llama a la función agregar_platillo
            agregar_platillo()

        # Si el usuario elige la opción 2
        elif opcion == "2":

            # Llama a la función eliminar_platillo
            eliminar_platillo()

        # Si el usuario elige la opción 3
        elif opcion == "3":

            # Llama a la función mostrar_platillos
            mostrar_platillos()

        # Si el usuario elige la opción 4
        elif opcion == "4":

            # Muestra mensaje de despedida
            print("\n👋 Gracias por usar el sistema.\n")

            # Rompe el bucle y sale del menú
            break

        # Si el usuario escribe una opción incorrecta
        else:

            # Muestra mensaje de error
            print("\n❌ Opción inválida.\n")


# Define el menú para el usuario (mesero)
def menu_usuario():

    # Inicia un bucle para mostrar el menú repetidamente
    while True:

        # Muestra el título del menú usuario
        print("===== 🧑‍🍽️ MENÚ MESERO =====")

        # Muestra la opción para ver el menú del restaurante
        print("1. Ver menú del restaurante")

        # Muestra la opción para salir
        print("2. Salir")

        # Solicita al usuario una opción
        opcion = input("Seleccione una opción: ")

        # Si el usuario elige la opción 1
        if opcion == "1":

            # Llama a la función mostrar_platillos
            mostrar_platillos()

        # Si el usuario elige la opción 2
        elif opcion == "2":

            # Muestra mensaje de despedida
            print("\n👋 Gracias por usar el sistema.\n")

            # Rompe el bucle y sale del menú
            break

        # Si el usuario escribe una opción incorrecta
        else:

            # Muestra mensaje de error
            print("\n❌ Opción inválida.\n")