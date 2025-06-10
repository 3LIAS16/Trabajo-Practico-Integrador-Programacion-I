

def menu():
    print("1 - Ingresar producto")
    print("2 - Buscar por codigo")
    print("3 - Mostrar catalogo")
    print("4 - Salir del programa")
    opcion=int(input("Seleccione la opcion: "))
    return opcion

def menu_catalogo():
    print("1 - Mostrar en Preorden")
    print("2 - Mostrar en Postorden")
    print("3 - Mostrar en Inorden")
    print("4 - Volver")
    opcion=int(input("Ingrese la opcion: "))
    return opcion

def menu_insertar():
    valor=int(input("Ingrese el codigo del producto a registrar o ingrese '0' para salir: "))
    return valor

def menu_buscar():
    valor=int(input("Ingrese el codigo del producto a buscar: "))
    return valor