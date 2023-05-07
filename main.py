from alumno import Alumno
from manejador_alumnos import ManejadorAlumnos
from manejador_materias import ManejadorMaterias

# Carga de datos
alumnos = ManejadorAlumnos(np.empty(0, dtype=Alumno))
alumnos.cargar_datos("alumnos.csv")

materias = ManejadorMaterias([])
materias.cargar_datos("materiasAprobadas.csv")

# Menú de opciones
while True:
    print("------ Menú de opciones ------")
    print("1. Informar promedio de un alumno")
    print("2. Informar estudiantes que aprobaron una materia")
    print("3. Obtener listado de alumnos ordenado")
    print("0. Salir")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        dni = input("Ingrese el DNI del alumno: ")
        prom_aplazos, prom_sin_aplazos = alumnos.informar_promedio(dni)
        print(f"Promedio con aplazos: {prom_aplazos:.2f}")
        print(f"Promedio sin aplazos: {prom_sin_aplazos:.2f}")
    
    elif opcion == "2":
        materia = input("Ingrese el nombre de la materia: ")
        materias_aprobadas = materias.buscar_materias_aprobadas(materia, nota_minima=7, tipo_aprobacion="P")
        print("Estudiantes que aprobaron la materia en forma promocional:")
        for m in materias_aprobadas:
            print(m)
    
    elif opcion == "3":
        alumnos_ordenados = sorted(alumnos, key=lambda a: (a.anio_cursada, a.apellido, a.nombre))
        print("Listado de alumnos:")
        for a in alumnos_ordenados:
            print(a)
    
    elif opcion == "0":
        break
    
    else:
        print("Opción inválida")