#se definen todas las opciones en funciones
#en esta parte se registran las macotas y se leen
def registrar_mascota():
    archivo = open("mascotas_registradas.txt", "a")
    nombre = input("Nombre de su mascota: ")
    especie = input("Especie (Perro, Gato, etc): ")
    edad = input("Edad de su mascota: ")
    archivo.write(nombre + ";" + especie + ";" + edad + "\n")
    archivo.close()
    print("Mascota registrada correctamente")
def ver_mascotas():
    archivo = open("mascotas_registradas.txt", "r")
    print("\nMascotas Registradas")
    for x in a:
        d = x.split(";")
        print("Nombre de la mascota:", d[0])
        print("Especie:", d[1])
        print("Edad de la mascota:", d[2])
    archivo.close()
#en esta parte se registran los turnos y se leen
def registrar_turno():
    archivo = open("turnos_registrados.txt", "a")
    nombre = input("Mascota: ")
    fecha = input("Fecha: ")
    archivo.write(nombre + ";" + fecha + "\n")
    archivo.close()
    print("Turno registrado correctamente")
def ver_turnos():
    archivo = open("turnos_registrados.txt", "r")
    print("\nTurnos Registrados")
    for x in archivo:
        d = x.split(";")
        print("Mascota:", d[0])
        print("Fecha:", d[1])
    archivo.close()
#aca se registran las atenciones realizadas por el veterinario y se ven las estadisticas
def registrar_atencion():
    archivo = open("atenciones_registradas.txt", "a")
    nombre = input("Mascota: ")
    servicio = input("Servicio Realizado: ")
    archivo.write(nombre + ";" + servicio + "\n")
    archivo.close()
    print("Atención registrada correctamente")
def ver_estadisticas():
    archivo = open("atenciones_registradas.txt", "r")
    c = 0
    v = 0
    o = 0
    for x in archivo:
        d = x.split(";")
        if d[1].strip() == "Consulta":
            c = c + 1
        elif d[1].strip() == "Vacuna":
            v = v + 1
        else:
            o = o + 1
    print("\nEstadisticas")
    print("Consultas:", c)
    print("Vacunas:", v)
    print("Otros:", o)
    archivo.close()
#parte en la que se pueden buscar mascotas y contar cuantas hay
def buscar_mascota():
    archivo = open("mascotas_registradas.txt", "r")
    nombre = input("Ingrese el nombre de la mascota que busca: ")
    encontrada = False
    for x in archcivo:
        datos = x.split(";")
        if datos[0] == nombre:
            print("\nMascota encontrada")
            print("Nombre de la mascota: ", datos[0])
            print("Especie: ", datos[1])
            print("Edad: ", datos[2])
            encontrada = True
    if encontrada == False:
        print("La mascota no esta registrada")
    archivo.close()
def cantidad_mascotas():
    archivo = open("mascotas_registradas.txt", "r")
    contador = 0
    for x in archivo:
        contador = contador + 1
    print("Hay", contador, "mascotas registradas en el sistema")
    archivo.close()
#menu principal del sistema
def mostrar_menu():
    print("\n1-Registrar mascota")
    print("2-Ver mascotas registradas")
    print("3-Registrar turno")
    print("4-Ver turnos")
    print("5-Registrar atención realizada")
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
            print("Opcion incorrecta, intente nuevamente")
menu_principal()
