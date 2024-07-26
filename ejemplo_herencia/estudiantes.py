class Estudiante:
    def __init__(self):
        self._nombres_estudiante = ""
        self._apellidos_estudiante = ""
        self._identificacion_estudiante = ""
        self._edad_estudiante = 0

    def establecer_nombres_estudiante(self, nom):
        self._nombres_estudiante = nom

    def establecer_apellido_estudiante(self, ape):
        self._apellidos_estudiante = ape

    def establecer_identificacion_estudiante(self, iden):
        self._identificacion_estudiante = iden

    def establecer_edad_estudiante(self, ed):
        self._edad_estudiante = ed

    def obtener_nombres_estudiante(self):
        return self._nombres_estudiante

    def obtener_apellido_estudiante(self):
        return self._apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self._identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self._edad_estudiante
