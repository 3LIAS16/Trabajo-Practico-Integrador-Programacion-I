from utils.menu import menu, menu_catalogo, menu_insertar, menu_buscar
from utils.operaciones import insertar,buscar, mostrarCatalogoPost, mostrarCatalogoIn, mostrarCatalogoPre 



def main_loop():
    arbol=[]
    main_menu=True
    while main_menu:
        opcion=menu()
        if opcion==1:
            arbol=sub_menu_insertar(arbol)
        elif opcion==2:
            sub_menu_buscar(arbol)
        elif opcion==3:
            sub_menu_catalogo(arbol)
        elif opcion==4:
            print("Saliendo del programa....")
            main_menu=False
        else:
            print("Opcion no valida")


def sub_menu_catalogo(arbol):
    opcion=menu_catalogo
    menu_cat=True
    while menu_cat:
        opcion=menu_catalogo()

        if opcion==1:
            print(f"Arbol en preorden: {mostrarCatalogoPre(arbol)}")
        elif opcion==2:
            print(mostrarCatalogoPost(arbol))
        elif opcion==3:
            print(mostrarCatalogoIn(arbol))
        elif opcion==4:
            print("Volviendo....")
            menu_cat=False
        else:
            print("Opcion no valida")

def sub_menu_insertar(arbol):
    insert=True
    while insert:
        valor = menu_insertar()
        if valor == 0:
            insert=False
            print("Volviendo...")
        else:
            arbol=insertar(arbol, valor)
            print(f"Producto {valor} Ingresado correctamente")
    return arbol

def sub_menu_buscar(arbol):
    valor=menu_buscar()
    variable=buscar(arbol,valor)
    if variable is False:
        print(f"No se encontro el articulo codigo: {valor}")
    else:
        print(f"Articulo codigo {valor} disponible")