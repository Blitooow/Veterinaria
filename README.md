### Sistema de gestión de veterinaria

--Trabajo Integrador Python--
Algoritmos y estructuras de datos (2026) - UTN FRRe
Comision k1.2
Grupo B 44
Integrantes:
- Kuray Pablo
- Vilaqui Tobias
- Fontana Jeremias Adan

## Descripcion Breve
El sistema funciona como un operador para una veterinaria, en el cual se pueden registrar turnos para sus mascotas, historial de atenciones realizadas, etc. El sistema implementa una solucion para veterinarias que necesiten orden en sus registros de turnos, mascotas, etc. El programa funciona mejor para que lo usen los operarios de la veterinaria.

## Video demo del programa
Link: 

## Instrucciones de ejecución
1. Clonar este repositorio
2. Abrir la terminal dentro de la carpeta
3. Ejecutar el programa con el comando:
Python vet.py

## Uso de IA
Se uso chatgpt para generar ideas para la estructura del programa (menu principal), y para contestar dudas en el tema del uso de archivos .txt, tambien se utilizo claude para guiarnos con la implementacion de funciones en el codigo inicial.

## Codigo Fuente:
```python
def registrar_mascota():
    a = open("mascotas_registradas.txt", "a")
    nombre = input("Nombre de su mascota: ")
    especie = input("Especie (Perro, Gato, etc): ")
    edad = input("Edad de su mascota: ")
    a.write(nombre + ";" + especie + ";" + edad + "\n")
    a.close()
    print("Mascota registrada correctamente")
def ver_mascotas():
    a = open("mascotas_registradas.txt", "r")
    print("\nMascotas Registradas")
    for x in a:
        d = x.split(";")
        print("Nombre de la mascota:", d[0])
        print("Especie:", d[1])
        print("Edad de la mascota:", d[2])
    a.close()
def registrar_turno():
    a = open("turnos_registrados.txt", "a")
    nombre = input("Mascota: ")
    fecha = input("Fecha: ")
    a.write(nombre + ";" + fecha + "\n")
    a.close()
    print("Turno registrado correctamente")
def ver_turnos():
    a = open("turnos_registrados.txt", "r")
    print("\nTurnos Registrados")
    for x in a:
        d = x.split(";")
        print("Mascota:", d[0])
        print("Fecha:", d[1])
    a.close()
def registrar_atencion():
    a = open("atenciones_registradas.txt", "a")
    nombre = input("Mascota: ")
    servicio = input("Servicio Realizado: ")
    a.write(nombre + ";" + servicio + "\n")
    a.close()
    print("Atención registrada correctamente")
def ver_estadisticas():
    a = open("atenciones_registradas.txt", "r")
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
def buscar_mascota():
    a = open("mascotas_registradas.txt", "r")
    nombre = input("Ingrese el nombre de la mascota que busca: ")
    encontrada = False
    for x in a:
        datos = x.split(";")
        if datos[0] == nombre:
            print("\nMascota encontrada")
            print("Nombre de la mascota: ", datos[0])
            print("Especie: ", datos[1])
            print("Edad: ", datos[2])
            encontrada = True
    if encontrada == False:
        print("La mascota no esta registrada")
    a.close()
def cantidad_mascotas():
    a = open("mascotas_registradas.txt", "r")
    contador = 0
    for x in a:
        contador = contador + 1
    print("Hay", contador, "mascotas registradas en el sistema")
    a.close()
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
            print("Opción incorrecta, intente nuevamente")
menu_principal()
```
