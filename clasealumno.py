class Alumno:
    def __init__(self, dni, apellido, nombre, carrera, año):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.año = año
        self.materias_aprobadas = []

    def __lt__(self, otro):
        if self.año == otro.año:
            return (self.apellido, self.nombre) < (otro.apellido, otro.nombre)
        else:
            return self.año < otro.año

    def agregar_materia_aprobada(self, materia_aprobada):
        self.materias_aprobadas.append(materia_aprobada)

    def obtener_promedio(self, con_aplazos=True):
        notas = [materia.nota for materia in self.materias_aprobadas if con_aplazos or materia.nota >= 4]
        if notas:
            return sum(notas) / len(notas)
        else:
            return None
    
               