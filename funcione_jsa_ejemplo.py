import numpy

arreglo_res = numpy.zeros((3,3),int) 
lista_rut = []

acumulador = 0





def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in (1,2,3,4,5,6):
                return opcion
            else:
                print("Error opcion no valida")    
        except:
            print("Error debe ingresar numeros enteros") 

def ver_restaurant():
    for x in range(4):
            print(f"Fila {x+1}:\t" , end="")
            for y in range(3):   
                print(arreglo_res[x][y],end=" ")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni digito vereficador): "))
            if rut >= 1000000 and rut <= 99999999:
                lista_rut.append[rut]
                return rut
            else:
                print("Error rut no valido")
        except:
            print("Error debe ingresar numeros enteros")        

def validar_nombre():
    while True:
        nombre = input("Ingrese Nombre: ")
        if len(nombre.strip()) >= 3:
            return nombre
        else:
            print("Error debe tener al menos 3 caracteres")

def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("Error debe tener un @ en el correo")

def validar_cantidad_personas():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de personas que desea: "))
            if cantidad > 0 and cantidad <=6:
                return cantidad
            else:
                print("Error cantidad no valida")
        except:
            print("Error debe ingresar numeros enteros: ")        

def reservar_mesa():
    rut = validar_rut()
    nombre = validar_nombre()
    correo = validar_correo()
    cantidad = validar_cantidad_personas


def validar_bebestible():
    while True:
        print("""Bebestibles disponible
        1. Champagne  $4000
        2. Coca Cola  $3000
        3. Vino       $5000    
        4. Nada        """)
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            print("A seleccionado un Champagne")
            return 4000
        elif opcion == 2:
            print("A seleccionado una Coca Cola")
            return 3000
        elif opcion == 3:
            print("A seleccionado un Vino")
            return 5000
        else:
            return opcion
            

def validar_platos():
    while True:
        print("""Platos disponible
        1. Pasta Alfredo                     $7000
        2. Lomo Vetado con arroz y ensalada  $7500
        3. Sopa de Almejas                   $5000     
        4. Nada               """)
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            print("A seleccionado un Pasta Alfredo")
            return 7000
        elif opcion == 2:
            print("A seleccionado un Lomo Vetado con arroz y ensalada")
            return 7500
        elif opcion == 3:
            print("A seleccionado una Sopa de Almejas ")
            return 5000
        else:
            return opcion


def validar_postres():
    while True:
        print("""Postres disponible
        1. Leche de Tigre      $2500
        2. Suspiro Alimeño     $3500
        3. Helado de frambuesa $2000     """)
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            print("A seleccionado un Leche de Tigre")
            return 2500
        elif opcion == 2:
            print("A seleccionado un Suspiro Alimeño  ")
            return 3500
        elif opcion == 3:
            print("A seleccionado un Helado de frambuesa")
            return 2000
        else:
            return opcion

def validar_pedir():
    acumulador = acumulador + validar_bebestible

def carta():
    rut = validar_rut()
    bebestible = validar_bebestible()
    platos = validar_platos()
    postres = validar_postres()
        
def pagar():
    pass