class ManejadorAlumnos:
    def __init__(self):
        self.alumnos = np.empty((0,), dtype=Alumno)
    
    def cargar_alumnos(self, archivo):
        with open(archivo, 'r') as f:
            for line in f:
                datos = line.strip().split(',')
                dni = datos[0]
                apellido = datos[1]
                nombre = datos[2]
                carrera = datos[3]
                año = int(datos[4])
                alumno = Alumno(dni, apellido, nombre, carrera, año)
                self.alumnos = np.append(self.alumnos, alumno)