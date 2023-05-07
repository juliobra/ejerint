class ManejadorMaterias:
    def __init__(self):
        self.materias = []
    
    def cargar_datos(self, archivo):
        with open(archivo, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                dni = int(row[0])
                nombre = row[1]
                fecha = row[2]
                nota = float(row[3])
                aprobacion = row[4]
                materia = Materia(dni, nombre, fecha, nota, aprobacion)
                self.materias.append(materia)