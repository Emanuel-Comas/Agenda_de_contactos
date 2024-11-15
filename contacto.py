import uuid

class Contact:
    
    def __init__(self, nombre, apellido, telefono, gmail, linkedin, id = uuid):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.gmail = gmail
        self.linkedin = linkedin
        if id is None:
            self.id = str(uuid.uuid4())  # Generar un UUID único para cada contacto
        else:
            self.id = id  # Usar el ID pasado al crear el contacto


    # Método to_dict: Convierte un objeto Contacto en un diccionario. 
    # Este paso es necesario porque el módulo json solo puede serializar datos tipo diccionario, lista, número, etc.,
    def to_dict(self):
        """Convierte el objeto Contacto en un diccionario para guardarlo en JSON"""
        # Retorna un diccionario con las claves y valores correspondientes al objeto Contacto.
        return {
            # Convierte el valor de 'nombre' a minúsculas antes de agregarlo al diccionario.
            "nombre": self.nombre,
            # Convierte el valor de 'apellido' a minúsculas antes de agregarlo al diccionario.
            "apellido": self.apellido,
            # Convierte el valor de 'telefono' a minúsculas antes de agregarlo al diccionario.
            "telefono": self.telefono,
            # Convierte el valor de 'gmail' a minúsculas antes de agregarlo al diccionario.
            "gmail": self.gmail,
            # Convierte el valor de 'linkedin' a minúsculas antes de agregarlo al diccionario.
            "linkedin": self.linkedin,
            # Agrega el valor de 'id' tal como está, ya que no se requiere convertirlo a minúsculas.
            "id": self.id
        }

    
    # Comandos
    def establecerNombre(self, nombre):
        # Asigna el valor recibido como parámetro al atributo 'nombre' del objeto
        self.nombre = nombre

    def establecerApellido(self, apellido):
        # Asigna el valor recibido como parámetro al atributo 'apellido' del objeto
        self.apellido = apellido

    def establecerTelefono(self, telefono):
        # Asigna el valor recibido como parámetro al atributo 'telefono' del objeto
        self.telefono = telefono

    def establecerGmail(self, gmail):
        # Asigna el valor recibido como parámetro al atributo 'gmail' del objeto
        self.gmail = gmail

    def establecerLinkedin(self, linkedin):
        # Asigna el valor recibido como parámetro al atributo 'linkedin' del objeto
        self.linkedin = linkedin

    def establecerID(self, id):
        # Asigna el valor recibido como parámetro al atributo 'id' del objeto
        self.id = id

    # Método especial '__str__' para representar el objeto como cadena
    def __str__(self) -> str:
        # Devuelve una representación del objeto en formato de texto, mostrando todos los atributos importantes del contacto
        return f" \n Nombre: {self.nombre}\n Apellido: {self.apellido}\n Telefono: {self.telefono}\n Gmail: {self.gmail}\n LinkedIn: {self.linkedin}\n ID: {self.id}"


# contact1 = Contact(input("Ingrese nombre: "), input("Ingrese apellido: "), input("Ingrese telefono: "), input("Ingrese gmail: "), input("Ingrese linkedin: "))

# print(contact1)




    
    