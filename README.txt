=====================================================
  PROYECTO: Catálogo de Productos con Árbol Binario
=====================================================

Alumnos: González, Nicolás - Carulla, Elias
Materia: Programación I
Profesor: Prof. Cinthia Rigoni, Prof. Ariel Enferrel

-----------------------------------------------------
📌 DESCRIPCIÓN GENERAL
-----------------------------------------------------
Este proyecto implementa un sistema de catálogo de productos usando un Árbol Binario de Búsqueda (ABB), representado mediante listas simples en Python, sin utilizar clases ni objetos. muestra cómo funcionan estructuras de árbol de manera básica.

Formato del nodo:
    [valor, hijo_izquierdo, hijo_derecho]

Ejemplo:
    [50, [30, None, None], [70, None, None]]

-----------------------------------------------------
⚙️ FUNCIONALIDADES PRINCIPALES
-----------------------------------------------------

1. 📥 Inserción de productos
   - Inserta un nuevo valor en el árbol respetando las reglas del ABB.
   - Evita valores duplicados.

2. 🔍 Búsqueda
   - Verifica si un valor existe en el árbol.

3. 🧭 Recorridos del árbol
   - Preorden: Nodo → Izquierda → Derecha
   - Inorden:  Izquierda → Nodo → Derecha
   - Postorden: Izquierda → Derecha → Nodo
   - Todos devuelven una lista ordenada de los valores visitados.

-----------------------------------------------------
▶️ USO BÁSICO
-----------------------------------------------------

1. Insertar elementos:
       arbol = insertar(arbol, valor)
       arbol = insertar(arbol, valor)
       ...

3. buscar en el árbol:
       buscar(arbol, valor)

4. Mostrar recorridos:
       print(mostrarCatalogoPre(arbol))
       print(mostrarCatalogoIn(arbol))
       print(mostrarCatalogoPost(arbol))

-----------------------------------------------------
🗂️ ESTRUCTURA DE ARCHIVOS
-----------------------------------------------------

Proyecto integrador programacion I/
│
├── README.txt                          # Instrucciones y guía general del proyecto
│
├── documentacion/                     # Material de apoyo y entrega
│   ├── trabajo integrador programacion I.pdf       # Informe en PDF del trabajo
│   └── video explicativo trabajo programacion.mp4  # Video explicando el proyecto
│
└── proyecto integrador/              # Código fuente del programa
    ├── main.py                        # Script principal que ejecuta el programa
    │
    └── utils/                         # Módulos auxiliares
        ├── operaciones.py             # Funciones de árbol (insertar, eliminar, recorridos)
        ├── mainMenu.py                # Menú principal interactivo
        └── menu.py                    # Submenús y navegación

-----------------------------------------------------
📌 ACLARACIÓN TÉCNICA
-----------------------------------------------------
- No se utilizaron clases ni estructuras complejas a propósito, para facilitar el aprendizaje.
- Todas las operaciones se realizan manipulando listas de la forma [valor, izq, der].

