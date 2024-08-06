""" esto es una prueba para github"""

consigna = "Escribir un programa que permita cargar y procesar datos de alumnos del ITU en una lista de tuplas con la siguiente forma: (nombre, dni, materia)."

Alumnos = [
    {"Nombre": "diego", "DNI": 43749745, "Materia": "matematica"},
    {"Nombre": "juan", "DNI": 999101, "Materia": "lengua"},
    {"Nombre": "roberto", "DNI": 100101, "Materia": "lengua"},
    {"Nombre": "luci", "DNI": 778999, "Materia": "arte"},
    {"Nombre": "juan", "DNI": 223341, "Materia": "arte"},
    {"Nombre": "caro", "DNI": 4422222, "Materia": "biologia"},
    {"Nombre": "romi", "DNI": 5567721, "Materia": "ciencia"},
]


def Mostrar_Menu():
    print("1. Cargar alumnos")
    print("2. Busqueda")
    print("3. Salir")


def Cargar_Alumnos():
    CantAlumnos = input("Coloque la cantidad de alumnos que desea cargar: ")
    if CantAlumnos <= 0:
        print("La cantidad de alumnos debe ser mayor que 0.")
        return
    for i in range(1, int(CantAlumnos)):
        Nombre = input(f"Coloque el nombre del alumno n°{i}: ")
        DNI = int(input(f"Coloque el DNI del alumno n°{i}: "))
        Materia = input(
            f"Coloque la materia que cursa el alumno n°{i}: ")
        nuevo_alumno = {"Nombre": Nombre.lower(),
                        "DNI": DNI, "Materia": Materia.lower()}
        Alumnos.append(nuevo_alumno)
        print(Alumnos)


def Busqueda():
    print("1. Buscar alumno por nombre")
    print("2. Buscar alumno por DNI")
    print("3. Buscar alumno por Materia")
    opcion = input("Seleccione la opcion que desea: ")
    if opcion == "1":
        print("BUSQUEDA POR NOMBRE: ")
        Nombre = input("Coloque el nombre del alumno: ")
        for dic in Alumnos:
            if dic.get("Nombre") == Nombre.lower():
                print(dic)

    elif opcion == "2":
        DNI = int(input("Coloque el DNI del alumno: "))
        for alumno in Alumnos:
            if alumno.get("DNI") == DNI:
                print(alumno)
    elif opcion == "3":
        Materia = input("Coloque la materia que cursa el alumno: ")
        for dic in Alumnos:
            if dic.get("Materia") == Materia.lower():
                print(dic)
    else:
        print("opcion invalida, intente de nuevo")


while True:
    Mostrar_Menu()
    opcion = input("Seleccione la opción que desea: ")
    if opcion == "1":
        Cargar_Alumnos()
    elif opcion == "2":
        Busqueda()
    elif opcion == "3":
        print("Saliendo del menu")
        break
    else:
        print("Opcion invalida, intente de nuevo")
