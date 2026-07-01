def registrar_mascota():
    a = open("mascotas.txt", "a")
    nombre = input("Nombre de su mascota: ")
    especie = input("Especie (Perro, Gato, etc): ")
    edad = input("Edad de su mascota: ")
    a.write(nombre + ";" + especie + ";" + edad + "\n")
    a.close()
    print("Mascota registrada correctamente")
def ver_mascotas():
    a = open("mascotas.txt", "r")
    print("\nMascotas Registradas")
    for x in a:
        d = x.split(";")
        print("Nombre de la mascota:", d[0])
        print("Especie:", d[1])
        print("Edad de la mascota:", d[2])
    a.close()
def registrar_turno():
    a = open("turnos.txt", "a")
    nombre = input("Mascota: ")
    fecha = input("Fecha: ")
    a.write(nombre + ";" + fecha + "\n")
    a.close()
    print("Turno registrado correctamente")
def ver_turnos():
    a = open("turnos.txt", "r")
    print("\nTurnos Registrados")
    for x in a:
        d = x.split(";")
        print("Mascota:", d[0])
        print("Fecha:", d[1])
    a.close()
def registrar_atencion():
    a = open("atenciones.txt", "a")
    nombre = input("Mascota: ")
    servicio = input("Servicio: ")
    a.write(nombre + ";" + servicio + "\n")
    a.close()
    print("Atención registrada correctamente")
def ver_estadisticas():
    a = open("atenciones.txt", "r")
    c = 0
    v = 0
    o = 0
    for x in a:
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
    a.close()
def mostrar_menu():
    print("\n1 Registrar mascota")
    print("2-Ver mascotas registradas")
    print("3-Registrar turno")
    print("4-Ver turnos")
    print("5-Registrar atención realizada")
    print("6-Ver estadisticas")
    print("7-Salir")
def main():
    opcion = 0
    while opcion != 7:
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
            print("Gracias por utilizar el sistema")
        else:
            print("Opcion incorrecta, intente nuevamente")
main()
