import os
# Lista de libros registrados
libros = []
# Funcion para registrar un libro
def registrarLibro():
    try:
        print("Registrar libros para la biblioteca")
        nombre = input("Ingrese el nombre del libro: ").upper()
        autor = input("Ingrese el autor del libro: ").upper()
        publicacion = int(input("Ingrese año de la publicacion: "))
        sku = nombre[:6] + autor[:3] + str(publicacion)
        if nombre == "" or autor == "" or publicacion == "":
            print("Error, no se puede registrar un libro vacio")
        else:
            libro = {
                "Titulo": nombre,
                "Autor": autor,
                "Año de publicacion": publicacion,
                "SKU": sku
            }
            libros.append(libro)
            print("Libro registrado con exito")
    except ValueError:
        print("Error, Dato erroneo")
# Funcion para prestar un libro
def prestarLibro():
    try:
        print("Prestar libro")
        usuario = input("Ingrese nombre estudiante: ").upper()
        sku = input("Ingrese el sku del libro: ").upper()
        fecha_prestamo = input("Ingrese fecha de préstamo (dd/mm/yyyy): ")
        if usuario == "" or sku == "" or fecha_prestamo == "":
            print("Error, no se puede registrar un prestamo vacio")
        else:
            prestamo = {
                "Usuario": usuario,
                "Sku": sku,
                "Fecha de prestamo": fecha_prestamo
            }
            libros.append(prestamo)
            print("Préstamo registrado con éxito")
    except ValueError:
        print("Error, Dato erróneo")
# Funcion para listar todos los libros
def listarLibros():
    print("Listar todos los libros")
    print("TÍTULO\t\tAUTOR\t\tAÑO DE PUBLICACIÓN\t\tSKU")
    for libro in libros:
        if "Titulo" in libro:
            print(libro["Titulo"] + "\t\t" + libro["Autor"] + "\t\t" + str(libro["Año de publicacion"]) + "\t\t" + libro["SKU"])
    print("\nListar todos los préstamos")
    print("USUARIO\t\tSKU\t\tFECHA DE PRÉSTAMO")
    for libro in libros:
        if "Usuario" in libro:
            print(libro["Usuario"] + "\t\t" + libro["Sku"] + "\t\t" + libro["Fecha de préstamo"])
# Funcion para imprimir reporte de prestamos
def imprimirReporte():
    try:
        print("Reporte de libros prestados")
        with open('planilla_prestados.txt', 'w') as archivo:
            archivo.write("Usuario\t\tTitulo\t\tFecha de préstamo\n")
            for libro in libros:
                if "Usuario" in libro:
                    archivo.write(f"{libro['Usuario']}\t\t{libro['Sku']}\t\t{libro['Fecha de préstamo']}\n")
            print("Planilla generada exitosamente en:", os.getcwd())
    except ValueError:
        print("Dato erroneo.Intente nuevamente")
# Funcion para salir del programa
def salirPrograma():
    print("Programa finalizado...")
    print("Desarrollado por")
    print("Maria Martinez")
    print("RUN: 19.003.574-3")
# Menu principal
def menu():
    while True:
        try:
            print("--------Menu principal--------")
            print("1. Registrar Libro")
            print("2. Prestar Libro")
            print("3. Listar todos los Libros")
            print("4. Imprimir reporte de prestamos")
            print("5. Salir del programa")
            opcion = int(input("Ingrese opcion: "))
            if opcion == 1:
                registrarLibro()
            elif opcion == 2:
                prestarLibro()
            elif opcion == 3:
                listarLibros()
            elif opcion == 4:
                imprimirReporte()
            elif opcion == 5:
                salirPrograma()
                break
            else:
                print("Opción invalida. Intente nuevamente")
        except ValueError:
            print("Error,Dato erroneo")
