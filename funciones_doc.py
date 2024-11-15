# Funcionalidad básica:

# Agregar contacto: El programa debe permitir agregar nuevos contactos con información como nombre, teléfono, correo electrónico, etc.
# Mostrar contactos: Mostrar todos los contactos almacenados.
# Buscar contacto: Buscar un contacto por nombre o por algún otro dato (teléfono, email).
# Eliminar contacto: Eliminar un contacto de la agenda.
# Actualizar contacto: Modificar la información de un contacto ya existente.
# Menú: Un bucle while que presenta las opciones al usuario y ejecuta la función correspondiente según la elección.
# Usar libreria "uuid": Para que cada contacto tenga un ID unico.
    #UUID aleatorio (uuid4)
    #Este UUID se genera aleatoriamente, lo que lo hace adecuado cuando no necesitas incluir información como la dirección MAC o el tiempo. uuid4 es uno de los métodos más comunes para generar UUIDs de forma aleatoria.

# Nota: las funciones basicas deben afectar al JSON.


# Funcionalidad avanzada:

# Guardar contactos en un archivo: Utilizar un archivo (como .txt o JSON) para guardar la agenda de contactos y que no se pierdan cuando se cierre el programa.

# Ordenar contactos: Ordenar los contactos alfabéticamente por nombre o por otro criterio (como el número de teléfono o fecha de creación).

# Categorías de contactos: Asignar una categoría o etiqueta a cada contacto (por ejemplo, "Amigos", "Familia", "Trabajo").

# Validación de entrada: Asegurarse de que los datos que ingresa el usuario sean válidos (por ejemplo, que el teléfono tenga el formato correcto o que el correo sea válido).

# Búsqueda avanzada: Poder buscar por múltiples criterios (por ejemplo, buscar por nombre y mostrar solo aquellos que pertenecen a una categoría específica).


# Usar Programación Orientada a Objetos (POO)

# Clase Contacto:
# Esta clase se encargará de representar un contacto individual con los atributos necesarios (nombre, teléfono, email) y métodos para acceder o modificar esos atributos.

# Clase Agenda:
# La clase Agenda será la que maneje el conjunto de contactos. Tendrá métodos para agregar, eliminar, actualizar, mostrar y buscar contactos. Además, se encargará de guardar los contactos en un archivo JSON y cargarlos cuando el programa se ejecute.

# Clase Menu:
# Esta clase proporcionará la interfaz de usuario (en la consola), mostrando un menú y llamando a los métodos de las clases Agenda y Contacto según las opciones seleccionadas.


# ERRORES

# Los IDs cambiaban siempre cuando reiniciaba, ahora ya no deberain hacerlo, tuve que arreglar hasta la carga y save del json.