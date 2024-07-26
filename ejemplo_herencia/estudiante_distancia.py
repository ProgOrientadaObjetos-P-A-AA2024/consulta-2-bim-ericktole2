import estudiantes
class EstudianteDistancia(estudiantes):
    def __init__(self):
        super().__init__()
        self._numero_asignaturas = 0
        self._costo_asignatura = 0.0
        self._matricula_distancia = 0.0

    def establecer_numero_asignaturas(self, numero):
        self._numero_asignaturas = numero

    def establecer_costo_asignatura(self, valor):
        self._costo_asignatura = valor

    def calcular_matricula_distancia(self):
        self._matricula_distancia = self._numero_asignaturas * self._costo_asignatura

    def obtener_numero_asignaturas(self):
        return self._numero_asignaturas

    def obtener_costo_asignatura(self):
        return self._costo_asignatura

    def obtener_matricula_distancia(self):
        return self._matricula_distancia

    def __str__(self):
        reporte = f"Nombres: {self.obtener_nombres_estudiante()}\n"
        return reporte
