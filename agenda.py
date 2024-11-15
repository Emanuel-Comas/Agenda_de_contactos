from contacto import Contact
import json

class Agenda:
    

    # "archivo_json (str)": La ruta del archivo JSON que contiene la información de los contactos.
    # "contactos (list)": Lista de contactos cargados desde el archivo JSON.
    def __init__(self,archivo_json):

        # "archivo_json (str)": Se almacena la ruta del archivo JSON proporcionado como argumento.
        # "contactos (list)": Se inicializa con los contactos leídos desde el archivo JSON
        self.archivo_json = archivo_json
        self.contactos = self.cargar_contactos()  # Cargar los contactos del archivo JSON

    def cargar_contactos(self):
        """Carga los contactos desde el archivo JSON, si existe."""
        try:
            # Intento abrir el archivo JSON en modo lectura ('r')
            with open(self.archivo_json, 'r') as file:
                # Si el archivo se abrió correctamente, cargamos el contenido JSON en la variable "contactos"
                # json.load(file) deserializa el contenido del archivo JSON en una lista de diccionarios,
                # como argumentos de palabras clave al constructor de la clase Contact.
                # Esto asume que el diccionario tiene claves que coinciden con los parámetros del constructor de Contact.
                contactos = json.load(file)
                # Usamos una lista por comprensión para crear una lista de objetos Contact
                # Por cada diccionario en `contactos`, usamos el operador ** para pasar los elementos del diccionario.

                # Lo que hace es iterar sobre cada diccionario en la lista contactos, crear un objeto Contact,
                # usando los valores de cada diccionario y luego devolver una lista con todos los objetos,
                # Contact creados.
                # Cada vez que carga un contacto que ya estaba guardado en "JSON", crea un "objeto" de ese contacto.
                return [Contact(**contacto) for contacto in contactos]
        # Capturamos dos tipos de excepciones:
        except (FileNotFoundError, json.JSONDecodeError):
            # Si ocurre una excepción, como que el archivo no se encuentre o esté mal formateado,
            # devuelvo una lista vacía, lo que indica que no se pudieron cargar los contactos.
            return []  # Si el archivo no existe, está vacío o lso datos son invalidos, devolvemos una lista vacía

    
    def guardar_contactos(self):
        """Guarda todos los contactos en el archivo JSON."""
        try:
            # Intentamos abrir el archivo JSON en modo escritura ('w')
            with open(self.archivo_json, 'w') as file:
                # Convierto cada contacto a un diccionario usando el método `to_dict`
                # y luego usamos json.dump para escribir los datos en el archivo en formato JSON
                json.dump([contacto.to_dict() for contacto in self.contactos], file, indent=4)
            # Si la operación es exitosa, imprimimos un mensaje de confirmación
            print(f"Actualizado {self.archivo_json}")
        # Si ocurre cualquier excepción, imprimimos un mensaje de error con detalles
        except Exception as e:
            print(f"Error al guardar los contactos: {e}")



    # Creo un objeto de la clase contact
    def agregarContact(self, nombre, apellido, telefono, gmail, linkedin):
        # Crear un nuevo objeto de la clase Contact
        nuevoContact = Contact(nombre, apellido, telefono, gmail, linkedin)

        # Agrego el nuevo contacto a la lista.
        self.contactos.append(nuevoContact)
        self.guardar_contactos()  # Guardar en el archivo JSON
        print(f"Contacto agregado: {nuevoContact}")


    def mostrarContactos(self):
        # Verifo si la lista de contactos está vacía
        if not self.contactos:
            # Si la lista está vacía, imprimimos un mensaje indicando que no hay contactos
            print("No hay contactos en la agenda.")
        else:
            # Si hay contactos en la lista, imprimo un mensaje indicando que se mostrarán los contactos
            print("Los contactos de la lista son: ")
            # Recorremos todos los contactos en la lista de contactos
            for i in self.contactos:
                # Imprimo cada contacto en la lista
                print(i)


    def buscarContact(self):
        # Los "IDs" nunca eran los mismos, se reseteaban, "Solucionado".
        # El "ID" se convierte a minúsculas y se eliminan los espacios extra al principio y al final
        valorBusqueda = input("Ingrese el id del contacto a borrar: ").lower().strip()

        # itero todos los contactos guardados en la lista "self.contactos"
        for contacto in self.contactos:
            # Comparo el "ID" ingresado con el "ID" de cada contacto
            if valorBusqueda == contacto.id:
                # Si encuentra el contacto con el "ID" que coincide, lo imprimo.
                print(contacto)
                # Sale del bucle ya que solo necesito encontrar el primer contacto con ese "ID"
                break
        else:
            # Si no encuentra ningún contacto con el "ID" ingresado, imprimo un mensaje de "No encontrado"
            print("No encontrado.")
            
                

    def eliminarContact(self):

        # Solicita al usuario que ingrese el "ID" del contacto que desea eliminar.
        # Se convierte a minúsculas y se eliminan los espacios al principio y al final.
        valorBusqueda = input("Ingrese el id del contacto a borrar: ").lower().strip()
        # Imprime el tipo de valor y el valor ingresado para fines de depuración.
        print(type(valorBusqueda), valorBusqueda)

        # itero todos los contactos almacenados en "self.contactos".
        for contacto in self.contactos:
            # Imprimo un mensaje de depuración que muestra el valor ingresado por el usuario y el "ID" del contacto en la iteración actual.
            print(f"Comparando: {valorBusqueda} con {contacto.id}")  # Depuración

            if valorBusqueda.lower() == contacto.id.lower():  # Comparar el ID
                self.contactos.remove(contacto)  # Eliminar el contacto
                # Imprimo un mensaje indicando que el contacto ha sido eliminado.
                print(f"Se ha eliminado: {contacto}")
                self.guardar_contactos()  # Guardar los cambios en el archivo
                # Sale del bucle después de eliminar el primer contacto que coincida con el "ID".
                break
        else:
            print("ID no encontrado.")


    def updateContact(self):

        # Solicita al usuario que ingrese el "ID" del contacto que desea actualizar.
        valorBusqueda = input("Ingrese el id a actualizar: ").lower().strip()

        # Recorre todos los contactos almacenados en "self.contactos" con 'enumerate', que también proporciona el índice.
        for contacto in self.contactos:

            # Compara si el "ID" ingresado por el usuario está contenido en el "ID" del contacto (en minúsculas para ignorar mayúsculas).
            if valorBusqueda.lower() in contacto.id:
                # Si se encuentra un contacto que coincide parcialmente con el "ID" ingresado, se muestra un menú de opciones.
                print("""
                      Contacto encontrado.

                      
                        1 - Nombre.
                        2 - Apellido. 
                        3 - Telefono. 
                        4 - Gmail.
                        5 - LinkedIn
                        6 - ID
                        7 - Salir
                      
                        """)
                
                # Solicita al usuario que seleccione qué campo del contacto desea actualizar.
                opcion = input("Que desea actualizar?: ")

                # Uso la declaración 'match' (similar a un switch-case) para manejar diferentes opciones.
                match opcion:
                    case "1":
                        # Si el usuario selecciona la opción 1, pide el nuevo nombre y lo asigna al contacto.
                        nuevoNombre = input("Ingrese el nuevo nombre: ")
                        # Usar el setter para cambiar el nombre del contacto
                        contacto.establecerNombre(nuevoNombre)
                        print(f"Contacto actualizado: {contacto}")
                        break
                        

                    case "2":
                        # Si el usuario selecciona la opción 2, pide el nuevo apellido y lo asigna al contacto.
                        nuevoApellido = input("Ingrese el nuevo Apellido: ")
                        contacto.establecerApellido(nuevoApellido)
                        print(f"Contacto actualizado: {contacto}")
                        break

                    case "3":
                        # Si el usuario selecciona la opción 3, pide el nuevo teléfono y lo asigna al contacto.
                        nuevoTelefono = input("Ingrese el nuevo Telefono: ")
                        contacto.establecerTelefono(nuevoTelefono)
                        print(f"Contacto actualizado: {contacto}")
                        break

                    case "4":
                        # Si el usuario selecciona la opción 4, pide el nuevo Gmail y lo asigna al contacto.
                        nuevoGmail = input("Ingrese el nuevo Gmail: ")
                        contacto.establecerGmail(nuevoGmail)
                        print(f"Contacto actualizado: {contacto}")
                        break

                    case "5":
                        # Si el usuario selecciona la opción 5, pide el nuevo LinkedIn y lo asigna al contacto.
                        nuevoLinkedIn = input("Ingrese el nuevo LinkedIn: ")
                        contacto.establecerLinkedin(nuevoLinkedIn)
                        print(f"Contacto actualizado: {contacto}")
                        break

                    case "6":
                        # Si el usuario selecciona la opción 6, pide el nuevo ID y lo asigna al contacto.
                        nuevoID = input("Ingrese el nuevo ID: ")
                        contacto.establecerID(nuevoID)
                        print(f"Contacto actualizado: {contacto}")
                        break                        

                    case "7":
                        # Si el usuario selecciona la opción 7, simplemente imprime un mensaje de salida y termina la actualización.
                        print("Haz salido.")
                        break

                    case _:
                        # Si el usuario ingresa una opción no válida, se muestra un mensaje de error.
                        print("Opcion no valida.")
                        break
                        
        # Llamo a guardar_contactos para guardar los cambios en el archivo JSON
        self.guardar_contactos()
        print("JSON actualizado.")
        

                    






# Crear una instancia de la clase Agenda, pasando como argumento el archivo JSON ,
# donde se almacenarán los contactos. El archivo "contactos.json" es el, 
# encargado de guardar la lista de contactos, de forma persistente entre ejecuciones.
agenda = Agenda("contactos.json")
