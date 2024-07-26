import estudiantes
class EstudiantePresencial(estudiantes):
    def __init__(self):
        super().__init__()
        self._numero_creditos = 0
        self._costo_credito = 0.0
        self._matricula_presencial = 0.0

    def establecer_numero_creditos(self, numero):
        self._numero_creditos = numero

    def establecer_costo_credito(self, valor):
        self._costo_credito = valor

    def calcular_matricula_presencial(self):
        self._matricula_presencial = self._numero_creditos * self._costo_credito

    def obtener_numero_creditos(self):
        return self._numero_creditos

    def obtener_costo_credito(self):
        return self._costo_credito

    def obtener_matricula_presencial(self):
        return self._matricula_presencial

    def __str__(self):
        cadena = f"Nombre: {self.obtener_nombres_estudiante()}\n" \
                 f"Costo Matricula: {self._matricula_presencial:.2f}\n"
        return cadena