# Importamos ttk desde tkinter
# El módulo ttk (Templated Tkinter) es un módulo complementario de la biblioteca tkinter.
# Proporciona una interfaz para crear interfaces gráficas de usuario (GUI)
# Este módulo agrega widgets adicionales y estilos a tkinter, lo que nos permite crear
# interfaces gráficas más modernas

from tkinter import ttk


# En esta clase creamos los Frames o marcos
# Utilizaremos el método grid (método de grilla) para acomodar nuestros elementos
# La opción sticky se puede utilizar con: "n" (norte), "s" (sur), "e" (este) o "w" (oeste)
# Cada uno de estos marcos se coloca en una posición específica utilizando las funciones grid:
# - row (fila)
# - column (columna)
# - stycky (orientacion)
# - columnspan (la cantidad de columnas que va a ocupar)

class Frames:
    # Toma el parámetro root que es la raiz, en donde declaramos nuestra ventana principal
    def create_frames(root):
        # Marco o Frame Principal
        # Es el marco principal que ocupa la totalidad el espacio disponible
        #  Le asignamos un ancho de 800 y una altura de 600 píxeles.
        #  Desde styles.py utilizamos el estilo 'MainFrame.TFrame' para darle una apariencia específica.
        mainFrame = ttk.Frame(root, width=800, height=600, style='MainFrame.TFrame')
        mainFrame.grid(row=0, column=0, sticky='NSEW', columnspan=3)

        # Marco o Frame del Banner
        # Este marco se encuentra dentro del mainFrame (marco principal) y se ubica en la parte superior
        # No especificamos dimensiones, por lo que se ajustará automáticamente al contenido.
        topBannerFrame = ttk.Frame(mainFrame)
        topBannerFrame.grid(row=0, column=0, sticky='NSEW', columnspan=3)

        # Marco o Frame del menú
        # Es el marco que contiene el menú de opciones. Se encuentra dentro del mainFrame (marco principal)
        # utiliza el estilo 'MenuFrame.TFrame' que está en styles.py
        # Con la opción padx establecemos un relleno de 3 píxeles en los bordes izquierdo y derecho
        # Con la opción pady establecemos un relleno de 3 píxeles en los bordes superior e inferior.
        menuFrame = ttk.Frame(mainFrame, style='MenuFrame.TFrame')
        menuFrame.grid(row=1, column=0, padx=3, pady=3, sticky='NSEW')

        # Marco o Frame de las imágenes de los productos
        # Es el marco que se utiliza para mostrar las imágenes de los productos.
        # También se encuentra dentro del mainFrame (marco principal)
        # Utiliza el estilo 'DisplayFrame.TFrame' que está en styles.py.
        # Con la opción padx establecemos un relleno de 3 píxeles en los bordes izquierdo y derecho
        # Con la opción pady establecemos un relleno de 3 píxeles en los bordes superior e inferior.
        displayFrame = ttk.Frame(mainFrame, style='DisplayFrame.TFrame')
        displayFrame.grid(row=1, column=1, padx=3, pady=3, sticky='NSEW')

        # Marco o Frame de la orden
        # Es el marco que se utiliza para mostrar la orden del usuario.
        # Al igual que los anteriores, se encuentra dentro del mainFrame (marco principal)
        # Utiliza el estilo 'OrderFrame.TFrame' que está en styles.py
        # Con la opción padx establecemos un relleno de 3 píxeles en los bordes izquierdo y derecho
        # Con la opción pady establecemos un relleno de 3 píxeles en los bordes superior e inferior.
        orderFrame = ttk.Frame(mainFrame, style='OrderFrame.TFrame')
        orderFrame.grid(row=1, column=2, padx=3, pady=3, sticky='NSEW')

        # Marcos o frames de las opciones disponibles del menú
        # Los siguientes marcos se utilizan para mostrar las opciones disponibles en el menú
        # Se encuentran dentro del menuFrame y utilizan el estilo 'DishFrame.TFrame' que está en styles.py
        # Cada uno de estos marcos se coloca en una posición específica utilizando las funciones grid que mencionamos arribas

        comboBurguerBaconFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        comboBurguerBaconFrame.grid(row=1, column=0, sticky='NSEW')

        comboBurguerClasicaFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        comboBurguerClasicaFrame.grid(row=2, column=0, sticky='NSEW')

        comboBurguerEspecialFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        comboBurguerEspecialFrame.grid(row=3, column=0, sticky='NSEW')

        comboBurguerVeggieFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        comboBurguerVeggieFrame.grid(row=4, column=0, sticky='NSEW')

        capuccinoFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        capuccinoFrame.grid(row=5, column=0, sticky='NSEW')

        espressoFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        espressoFrame.grid(row=6, column=0, sticky='NSEW')

        latteFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        latteFrame.grid(row=7, column=0, sticky='NSEW')

        muffinArandanoFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        muffinArandanoFrame.grid(row=8, column=0, sticky='NSEW')

        muffinChipsFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        muffinChipsFrame.grid(row=9, column=0, sticky='NSEW')

        muffinChocolateFrame = ttk.Frame(menuFrame, style='DishFrame.TFrame')
        muffinChocolateFrame.grid(row=10, column=0, sticky='NSEW')

        # Finalmente le agregamos un return a nuestra función create_frames
        # este nos devuelve un diccionario que contiene todos los marcos creados.
        # Esto nos sirve para acceder a los marcos desde otras partes del código.
        # Por ejemplo, podemos acceder al marco principal como frames['mainFrame'].
        return {
            # Marco o Frame Principal
            'mainFrame': mainFrame,
            'topBannerFrame': topBannerFrame,
            'menuFrame': menuFrame,
            'displayFrame': displayFrame,
            'orderFrame': orderFrame,
            'comboBurgerBaconFrame': comboBurguerBaconFrame,
            'comboBurguerClasicaFrame': comboBurguerClasicaFrame,
            'comboBurguerEspecialFrame': comboBurguerEspecialFrame,
            'comboBurguerVeggieFrame': comboBurguerVeggieFrame,
            'capuccinoFrame': capuccinoFrame,
            'espressoFrame':espressoFrame,
            'latteFrame': latteFrame,
            'muffinArandanoFrame': muffinArandanoFrame,
            'muffinChipsFrame': muffinChipsFrame,
            'muffinChocolateFrame': muffinChocolateFrame
        }