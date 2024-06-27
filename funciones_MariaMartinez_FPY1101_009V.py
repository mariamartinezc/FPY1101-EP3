import os
libros = []
prestados = []
usuarios_reg = []
#funcion 1
def registrar_libros():
    try:
        nom_titulo = input("Ingrese titulo del Libro: ").upper()
        nom_autor = input("Ingrese nombre del Autor:").upper()
        publicacion =int(input("Ingrese año de la publicacion del libro : "))
        sku = input("SKU es las 6 primeras letras del título del libro ,las 3 primeras letras del autor y año de publicación.").upper()
        if nom_titulo == "" or nom_autor =="" or publicacion == "" or sku =="":
            print("faltaron datos por ingresar")
        else:
            libro ={
                "Titulo":nom_titulo,
                "Autor": nom_autor,
                "Año de publicacion": publicacion,
                "SkU" : sku
                }
            libros.append(libro)
            print("Registro se realizo correctamente")
    except ValueError:
         print("dato erroneo.intente nuevamente")
def prestar_libros():
    try:
        usuario = input("Ingrese Nomnre de usuario: ").upper()
        nom_titulo= input("Ingrese nombre del Autor:").upper()
        sku = input("SKU es las 6 primeras letras del título del libro – las 3 primeras letras del autor – año de publicación.").upper()
        fecha = int(input("Ingrese fecha del prestamo: "))
        if usuario == "" or nom_titulo==""or fecha == ""  or sku =="":
            print("faltaron datos por ingresar")
        else:
            reg_usuario ={
                "Usuario":usuario,
                "Titulo": nom_titulo,
                "SkU" : sku,
                "Fecha del Prestamo": fecha 
                }
            usuarios_reg.append(reg_usuario)
            print("Registro se realizo correctamente")
    except ValueError:
         print("dato erroneo.intente nuevamente")
#funcion 3
def lista_todos_los_libros():
    print("Titulo\t\tAutor\t\tAño de publicacion\t\tSKU\n")
    for libro in libros:
        print(f"Titulo{libro['nom_titulo']}\t\tAutor{libro['nom_autor']}\t\tAño de publicacion{libro['publicacion']}\t\tSKU{libro['sku']}\n")
def imprimir_reporte_de_prestamos():
    try:
        with open('planilla_prestados.txt','w')as archivo:
            archivo.write("Usuario\t\tTitulo\t\tFecha de prestamo\n")
            for reg_usuario in usuarios_reg:
                archivo.write(f"Usuario{reg_usuario['usuario']}\t\tTitulo{reg_usuario['nom_titulo']}\t\tFecha de prestamo{reg_usuario['fecha']}\n")
        print("panilla generada exitosamente en : ",os.getcwd())
    except ValueError:
        print("dato erroneo.intente nuevamente")
#menu bucle
def menu():
    while True:
        try:
            print("-----------Menu-----------")
            print("1.Registrar Libro")
            print("2.Prestar  Libro")
            print("3.Listar todos los Libro")
            print("4.Imprimir reporte de prestamos")
            print("5.Salir del programa ")
            opcion = int(input("Ingrese opcion : "))
        except ValueError: 
            print("dato erroneo.intente nuevamente")   
            if opcion == "1":
                registrar_libros ()
            elif opcion == "2":
                prestar_libros ()
            elif opcion == "3":
                lista_todos_los_libros ()
            elif opcion == "4":
                imprimir_reporte_de_prestamos ()
            elif opcion == "5":
                print("Programa finalizado...\nDesarrollado por Maria Martinez\nRUN: 19.003.574-3")
                break  
            else:
                print("opcion invalida.intente nuevamente")
