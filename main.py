# Jonathan Gabriel Morales Torres
# Guía de aprendizaje #1 - Tercera unidad

# Importa la función iniciar_sesion desde el archivo login.py
from login import iniciar_sesion

# Importa los menús desde el archivo restaurante.py
from restaurante import menu_administrador, menu_usuario

# Ejecuta el login y guarda el rol del usuario
rol = iniciar_sesion()

# Verifica si el rol es administrador
if rol == "administrador":

    # Muestra el menú con todas las opciones
    menu_administrador()

# Verifica si el rol es usuario normal
elif rol == "usuario":

    # Muestra el menú limitado del mesero
    menu_usuario()

# Si el rol no coincide con ninguno de los anteriores
else:

    # Muestra mensaje de error
    print("❌ Rol no reconocido.")