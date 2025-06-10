

def insertar(arbol, valor):
    if arbol == [] or arbol is None:
        return [valor, None, None]
    elif valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor)
    elif valor > arbol[0]:
        arbol[2] = insertar(arbol[2], valor)
    return arbol





def buscar(arbol, valor):
    
    if arbol is None:
        return False
    elif arbol[0]==valor:
        return True
    elif valor < arbol[0]:
        return buscar(arbol[1], valor)
    elif valor > arbol[0]:
        return buscar(arbol[2], valor)
    
    
def mostrarCatalogoPre(arbol):
    if arbol is None:
        return []
    return  arbol[0] , mostrarCatalogoPre(arbol[1]) , mostrarCatalogoPre(arbol[2])

def mostrarCatalogoPost(arbol):
    if arbol is None:
        return []
    return mostrarCatalogoPost(arbol[1]), mostrarCatalogoPost(arbol[2]), arbol[0]

def mostrarCatalogoIn(arbol):
    if arbol is None:
        return []
    return mostrarCatalogoIn(arbol[1]), arbol[0], mostrarCatalogoIn(arbol[2])