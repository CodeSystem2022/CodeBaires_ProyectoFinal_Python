# Importamos ttk que nos permite utilizar los widgets de tkinter
from tkinter import ttk
# Importamos display y order que creamos previamente
from display import *
from order import *


# --------------------------------- WIDGETS ------------------------- #

# En esta clase archivo utilizamos los widgets como los labels, buttons, etc.

class Widgets:
    def create_widgets(topBannerFrame, menuFrame, displayFrame, orderFrame,
                       comboBurguerBaconFrame, comboBurguerVeggieFrame, comboBurguerClasicaFrame,
                       comboBurguerEspecialFrame, capuccinoFrame, espressoFrame, latteFrame,
                       muffinArandanoFrame, muffinChipsFrame, muffinChocolateFrame, images):
        # Traemos las imagenes creadas en el archivo images.py para poder utilizarlas
        # en nuestros widgets
        logoImage = images['logoImage']
        topBannerImage = images['topBannerImage']
        displayImage = images['displayImage']

        # Explicamos las distinas opciones:
        # image = se le asigna la imagen que instanciamos previamente
        # background: color de fondo
        # row: fila en la que está ubicada
        # column: columna en la está ubicada
        # sticky: es para la orientación. Se puede utilizar con: "n" (norte), "s" (sur), "e" (este) o "w" (oeste)
        # text: texto del widget
        # style: le asigna el estilo relacionado con ese nombre en el archivo styles.py
        # padx: se agrega un relleno a la izquierda y a la derecha del texto
        # pady: se agrega un relleno  encima y debajo del texto
        # anchor: para controlar la posición y la alineación de un widget dentro de su celda en la cuadrícula
        # font: tipo de fuente, tamaño, etc
        # foreground: color del texto
        # padding: para el espaciado a cada lado del widget. Es útil para mejorar la legibilidad y
        # la apariencia de los widgets al agregar un espacio uniforme entre el contenido
        # y los bordes del widget

        # Utilización de command=lambda()
        # El uso de lambda permite crear una función pequeña y anónima directamente en el lugar donde se necesita,
        # en lugar de definir una función separada. Esto nos puede ser útil cuando la función es simple y no se necesita
        # en otros lugares de código.
        # Al utilizar lambda junto con command, se puede asignar una función personalizada a un evento específico del widget.
        # Por ejemplo, al presionar un botón, se llamará a la función lambda definida y se ejecutará el código que contiene.
        # Los parámetros opcionales pueden ser utilizados para pasar información relevante a la función.
        # Esta función es muy utilizada actualmente en Python

        # Establecemos el lugar en el que posicionaremos el logo de Codebaires
        # Los logos irán a los costados del banner de las hamburguesas que están en el header
        logoLabel = ttk.Label(topBannerFrame, image=logoImage, background='#0F1110')
        logoLabel.grid(row=0, column=0, sticky='NSEW')

        logoLabel = ttk.Label(topBannerFrame, image=logoImage, background='#0F1110')
        logoLabel.grid(row=0, column=2, sticky='NSEW')

        # Establecemos el lugar en el que posicionaremos el banner de las hamburguesas
        restaurantBannerLabel = ttk.Label(topBannerFrame, image=topBannerImage, background='#0F1110')
        restaurantBannerLabel.grid(row=0, column=1, sticky='NSEW')

        # Sección del Menú
        # Esta etiqueta muestra el título del menú en el marco (menuFrame) y define su ubicación y estilo
        mainMenuLabel = ttk.Label(menuFrame, text='Menú Mc UTN', style='MenuLabel.TLabel')
        mainMenuLabel.grid(row=0, column=0, sticky='WE')

        # Estas etiquetas muestran los nombres de los ítems del menú y definen su ubicación y estilo
        comboBurguerBaconLabel = ttk.Label(comboBurguerBaconFrame, text='Combo Bacon Burguer - $1200',
                                           style='MenuLabel.TLabel')
        comboBurguerBaconLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        comboBurguerClasicaLabel = ttk.Label(comboBurguerClasicaFrame,
                                             text='Combo Burguer Clasica - $1000',
                                             style='MenuLabel.TLabel')
        comboBurguerClasicaLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        comboBurguerEspecialLabel = ttk.Label(comboBurguerEspecialFrame,
                                              text='Combo Burguer Especial - $1500',
                                              style='MenuLabel.TLabel')
        comboBurguerEspecialLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        comboBurguerVeggieLabel = ttk.Label(comboBurguerVeggieFrame,
                                            text='Combo Veggie Burguer - $1000',
                                            style='MenuLabel.TLabel')
        comboBurguerVeggieLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        capuccinoLabel = ttk.Label(capuccinoFrame, text='Mc Capuccino - $950', style='MenuLabel.TLabel')
        capuccinoLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        espressoLabel = ttk.Label(espressoFrame, text='Mc Espresso - $600', style='MenuLabel.TLabel')
        espressoLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        latteLabel = ttk.Label(latteFrame, text='Mc Latte - $700', style='MenuLabel.TLabel')
        latteLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        muffinArandanoLabel = ttk.Label(muffinArandanoFrame, text='Muffin de Arandanos - $550',
                                        style='MenuLabel.TLabel')
        muffinArandanoLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        muffinChipsLabel = ttk.Label(muffinChipsFrame, text='Muffin de Vainilla con chips - $550',
                                     style='MenuLabel.TLabel')