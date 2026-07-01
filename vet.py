opcion = 0
while opcion != 7:
    print("\n1 Registrar mascota")
    print("2-Ver mascotas registradas")
    print("3-Registrar turno")
    print("4-Ver turnos")
    print("5-Registrar atención realizada")
    print("6-Ver estadisticas")
    print("7-Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        a = open("mascotas.txt", "a")
        nombre = input("Nombre: ")
        especie = input("Especie: ")
        edad = input("Edad: ")
        a.write(nombre + ";" + especie + ";" + edad + "\n")
        a.close()
        print("Mascota registrada correctamente")

    elif opcion == 2:
        a = open("mascotas.txt", "r")
        print("\nMascotas")
        for x in a:
            d = x.split(";")
            print("Nombre:", d[0])
            print("Especie:", d[1])
            print("Edad:", d[2])
        a.close()

    elif opcion == 3:
        a = open("turnos.txt", "a")
        nombre = input("Mascota: ")
        fecha = input("Fecha: ")
        a.write(nombre + ";" + fecha + "\n")
        a.close()
        print("Turno registrado correctamente")

    elif opcion == 4:
        a = open("turnos.txt", "r")
        print("\nTurnos")
        for x in a:
            d = x.split(";")
            print("Mascota:", d[0])
            print("Fecha:", d[1])
        a.close()

    elif opcion == 5:
        a = open("atenciones.txt", "a")
        nombre = input("Mascota: ")
        servicio = input("Servicio: ")
        a.write(nombre + ";" + servicio + "\n")
        a.close()
        print("Atención registrada correctamente")

    elif opcion == 6:
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
    elif opcion == 7:
        print("Gracias por utilizar el sistema")
    else:
        print("Opcion incorrecta, intente nuevamente")