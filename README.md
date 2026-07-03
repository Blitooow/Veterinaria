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
Link: https://drive.google.com/drive/folders/1RzZr15ZBvpUwYcowNUeLHY3QqA2nFsZ3?usp=sharing

## Instrucciones de ejecución
1. Clonar este repositorio
2. Abrir la terminal dentro de la carpeta
3. Ejecutar el programa con el comando:
Python vet.py

## Uso de IA
Se uso chatgpt para generar ideas para la estructura del programa (menu principal), y para contestar dudas en el tema del uso de archivos .txt, tambien se utilizo claude para guiarnos con la implementacion de funciones en la estructura principal del codigo inicial. ChatGPT nos recomendo el uso de la funcion .isdigit() para que el dato de la edad sea obligatoriamente numerico y tambien ayudo con las validaciones y excepciones, recomendo el uso de try except FileNotFoundError. Claude tambien nos ayudo a ordenar el codigo final.

## Codigo Fuente:
```python
#se definen todas las opciones en funciones
#en esta parte se registran las macotas y se leen
def registrar_mascota():
    nombre = input("Nombre de su mascota: ")
    especie = input("Especie (Perro, Gato, etc): ")
    edad = input("Edad de su mascota: ")
    while edad.isdigit() == False:
        print("La edad debe ser un numero, intente nuevamente")
        edad = input("Edad de su mascota: ")
    with open("mascotas_registradas.txt", "a") as archivoM:
        archivoM.write(nombre + ";" + especie + ";" + edad + "\n")
    print("Su mascota fue registrada")
def ver_mascotas():
    try:
        with open("mascotas_registradas.txt", "r") as archivoM:
            print("\n--Mascotas Registradas--")
            for linea in archivoM:
                datos = linea.split(";")
                print("Nombre de la mascota:", datos[0])
                print("Especie:", datos[1])
                print("Edad de la mascota:", datos[2])
    except FileNotFoundError:
        print("No hay mascotas registradas en el sistema")

#en esta parte se registran los turnos y se leen
def registrar_turno():
    with open("turnos_registrados.txt", "a") as archivoT:
        nombre = input("Mascota: ")
        fecha = input("Fecha: ")
        archivoT.write(nombre + ";" + fecha + "\n")
        print("Turno registrado correctamente")
def ver_turnos():
    try:
        with open("turnos_registrados.txt", "r") as archivoT:
            print("\n--Turnos Registrados--")
            for linea in archivoT:
                datos = linea.split(";")
                print("Mascota:", datos[0])
                print("Fecha:", datos[1])
    except FileNotFoundError:
        print("No hay turnos registrados en el sistema")

#aca se registran las atenciones realizadas por el veterinario y se ven las estadisticas
def registrar_atencion():
    with open("atenciones_registradas.txt", "a") as archivoA:
        nombre = input("Mascota: ")
        servicio = input("Servicio Realizado (Vacuna, Consulta, Cirugia, Radiografia, Otro): ")
        archivoA.write(nombre + ";" + servicio + "\n")
        print("Atención registrada correctamente")
def ver_estadisticas():
    try:
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
                if datos[1].strip() == "Cirugia":
                    cirugias = cirugias + 1
                elif datos[1].strip() == "Radiografia":
                    radiografias = radiografias + 1
                else:
                    otro = otro + 1
        print("\n--Estadisticas--")
        print("Consultas:", consultas)
        print("Vacunas:", vacunas)
        print("Cirugias: ", cirugias)
        print("Radiografias: ", radiografias)
        print("Otros:", otro)
    except FileNotFoundError:
        print("No hay estadisticas registradas en el sistema")

#parte en la que se pueden buscar mascotas y contar cuantas hay
def buscar_mascota():
    try:
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
    except FileNotFoundError:
        print("No hay mascotas registradas en el sistema")
def cantidad_mascotas():
    try:
        with open("mascotas_registradas.txt", "r") as archivoM:
            contador = 0
            for linea in archivoM:
                contador = contador + 1
            print("Hay", contador, "mascotas registradas en el sistema")
    except FileNotFoundError:
        print("No hay mascotas registradas en el sistema")

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
        try:
            opcion = int(input("Elija una opción: "))
        except ValueError:
            print("Debe ingresar un numero, intente nuevamente")
            opcion = 0
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
