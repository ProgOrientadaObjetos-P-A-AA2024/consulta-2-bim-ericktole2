from persona_ecuatoriana import PersonaEcuatoriana
from persona_peruana import PersonaPeruana
class Main:
    def run(self):
        persona1 = PersonaEcuatoriana("René", 39)
        persona2 = PersonaPeruana("Santiago", 20)

        print(persona1.obtener_edad())
        print(persona2.obtener_edad())

        mi_lista = [persona1, persona2]
        promedio = persona1.promedio_edades(mi_lista)
        print(f"{promedio:.2f}")

        # Demostración de polimorfismo
        print(persona1.obtener_nombre_pais())  # Ecuador
        print(persona2.obtener_nombre_pais())  # Perú
    
if __name__ == "__main__":
 Main().run()