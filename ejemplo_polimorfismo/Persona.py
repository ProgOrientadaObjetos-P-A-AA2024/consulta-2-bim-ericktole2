
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def promedio_edades(self, lista):
        suma = sum(persona.obtener_edad() for persona in lista)
        return suma / len(lista)

    def obtener_nombre_pais(self):
        return "Desconocido"


