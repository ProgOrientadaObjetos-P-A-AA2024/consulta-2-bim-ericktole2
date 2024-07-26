from Persona import Persona
class PersonaEcuatoriana(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def obtener_nombre_pais(self):
        return "Ecuador"