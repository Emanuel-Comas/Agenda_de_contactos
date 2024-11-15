# Importo directamente la instancia de agenda.
from agenda import agenda

print("""

         MENU
      
1 - Agregar contacto.
2 - Mostrar contactos
3 - Buscar contactos
4 - Eliminar contactos
5 - Actualizar contactos
6 - Salir

""")

opcion = input("Elija una opcion: ")

match opcion:
    # Si el usuario elige la opción 1 (Agregar contacto)
    case "1":
        # Solicitar datos del contacto
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        telefono = input("Ingrese teléfono: ")
        gmail = input("Ingrese gmail: ")
        linkedin = input("Ingrese linkedin: ")

        # Llamar al método para agregar el contacto
        agenda.agregarContact(nombre, apellido, telefono, gmail, linkedin)
        
    # Si el usuario elige la opción 2 (Mostrar contactos)   
    case "2":
        # Llamo a la instancia de la agenda.
        agenda.mostrarContactos()

    # Si el usuario elige la opción 3 (Buscar contacto)
    case "3":
        # Llamamos al método 'buscarContact' de la clase Agenda para buscar un contacto
        agenda.buscarContact()

    # Si el usuario elige la opción 4 (Eliminar contacto)
    case "4":
        # Llamamos al método 'eliminarContact' de la clase Agenda para eliminar un contacto
        agenda.eliminarContact()

    # Si el usuario elige la opción 5 (Actualizar contacto)
    case "5":
        # Llamamos al método 'updateContact' de la clase Agenda para actualizar un contacto
        agenda.updateContact()

    # Si el usuario elige la opción 6 (Salir)
    case "6":
        # Imprime un mensaje de salida
        print("Haz salido.")

    # Si el usuario ingresa una opción que no está en el menú
    case _:
        # Imprime un mensaje de error indicando que la opción no es válida
        print("Opcion no valida.") 