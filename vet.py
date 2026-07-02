#se definen todas las opciones en funciones
#en esta parte se registran las macotas y se leen
def registrar_mascota():
    with open("mascotas_registradas.txt", "a") as archivoM:
        nombre = input("Nombre de su mascota: ")
        especie = input("Especie (Perro, Gato, etc): ")
        edad = input("Edad de su mascota: ")
        archivoM.write(nombre + ";" + especie + ";" + edad + "\n")
        print("Mascota registrada correctamente")
        while edad.isdigit() == False:
            print("La edad debe ser un numero, intente nuevamente")
            edad = input("Edad de su mascota: ")
def ver_mascotas():
    with open("mascotas_registradas.txt", "r") as archivoM:
        print("\n--Mascotas Registradas--")
        for linea in archivoM:
            datos = linea.split(";")
            print("Nombre de la mascota:", datos[0])
            print("Especie:", datos[1])
            print("Edad de la mascota:", datos[2])

#en esta parte se registran los turnos y se leen
def registrar_turno():
    with open("turnos_registrados.txt", "a") as archivoT:
        nombre = input("Mascota: ")
        fecha = input("Fecha: ")
        archivoT.write(nombre + ";" + fecha + "\n")
        print("Turno registrado correctamente")
def ver_turnos():
    with open("turnos_registrados.txt", "r") as archivoT:
        print("\n--Turnos Registrados--")
        for linea in archivoT:
            datos = linea.split(";")
            print("Mascota:", datos[0])
            print("Fecha:", datos[1])

#aca se registran las atenciones realizadas por el veterinario y se ven las estadisticas
def registrar_atencion():
    with open("atenciones_registradas.txt", "a") as archivoA:
        nombre = input("Mascota: ")
        servicio = input("Servicio Realizado (Vacuna, Consulta, Otro): ")
        archivoA.write(nombre + ";" + servicio + "\n")
        print("Atención registrada correctamente")
def ver_estadisticas():
    with open("atenciones_registradas.txt", "r") as archivoA:
        consultas = 0
        vacunas = 0
        otro = 0
        for linea in archivoA:
            datos = linea.split(";")
            if datos[1].strip() == "Consulta":
                consultas = consultas + 1
            elif datos[1].strip() == "Vacuna":
                vacunas = vacunas + 1
            else:
                otro = otro + 1
    print("\n--Estadisticas--")
    print("Consultas:", consultas)
    print("Vacunas:", vacunas)
    print("Otros:", otro)

#parte en la que se pueden buscar mascotas y contar cuantas hay
def buscar_mascota():
    with open("mascotas_registradas.txt", "r") as archivoM:
        nombre = input("Ingrese el nombre de la mascota que busca: ")
        encontrada = False
        for linea in archivoM:
            datos = linea.split(";")
            if datos[0] == nombre:
                print("\nMascota encontrada")
                print("Nombre de la mascota: ", datos[0])
                print("Especie: ", datos[1])
                print("Edad: ", datos[2])
                encontrada = True
        if encontrada == False:
            print("La mascota no esta registrada")
def cantidad_mascotas():
    with open("mascotas_registradas.txt", "r") as archivoM:
        contador = 0
        for linea in archivoM:
            contador = contador + 1
        print("Hay", contador, "mascotas registradas en el sistema")

#menu principal del sistema
def mostrar_menu():
    print("\n1-Registrar mascota")
    print("2-Ver mascotas registradas")
    print("3-Registrar turno")
    print("4-Ver turnos")
    print("5-Registrar atención medica realizada")
    print("6-Ver estadisticas")
    print("7-Buscar una mascota registrada: ")
    print("8-Consultar cuantas mascotas hay registradas: ")
    print("9-Salir")
def menu_principal():
    opcion = 0
    while opcion != 9:
        mostrar_menu()
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            registrar_mascota()
        elif opcion == 2:
            ver_mascotas()
        elif opcion == 3:
            registrar_turno()
        elif opcion == 4:
            ver_turnos()
        elif opcion == 5:
            registrar_atencion()
        elif opcion == 6:
            ver_estadisticas()
        elif opcion == 7:
            buscar_mascota()
        elif opcion == 8:
            cantidad_mascotas()
        elif opcion == 9:
            print("Gracias por utilizar el sistema")
        else:
            print("Opción incorrecta, intente nuevamente")
menu_principal()
