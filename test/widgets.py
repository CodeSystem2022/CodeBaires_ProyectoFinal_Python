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
        muffinChipsLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        muffinChocolateLabel = ttk.Label(muffinChocolateFrame, text='Muffin de Chocolate - $550',
                                         style='MenuLabel.TLabel')
        muffinChocolateLabel.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        # Sección de pedido

        # Estas etiquetas muestran los nombres en la seccion de pedido y definen su ubicación y estilo

        # Etiqueta de Pedido
        orderTitleLabel = ttk.Label(orderFrame, text='Pedido')
        orderTitleLabel.grid(row=0, column=0, sticky='EW')
        orderTitleLabel.configure(
            foreground='white',
            background='black',
            font=('Franklin Gothic', 12, 'bold'),
            anchor='center',
            padding=(5, 5, 5, 5)
        )

        # Etiqueta de Id de Pedido
        orderIDLabel = ttk.Label(orderFrame, text='Id. Pedido: ' + Order.order_id())
        orderIDLabel.grid(row=1, column=0, sticky='EW', pady=1)
        orderIDLabel.configure(
            foreground='white',
            background='black',
            font=('Franklin Gothic', 12, 'normal'),
            anchor='center',
        )

        # Etiqueta de la transacción (donde se ubican todos los items del menú seleccionados)
        orderTransactionLabel = ttk.Label(orderFrame, style='orderTransaction.TLabel')
        orderTransactionLabel.grid(row=2, column=0, sticky='NSEW')

        # # Etiqueta de Total del Pedido
        orderTotalLabel = ttk.Label(orderFrame, text='TOTAL: $0', style='orderTotal.TLabel')
        orderTotalLabel.grid(row=3, column=0, sticky='EW')

        # Sección del display (centro de la app)
        displayLabel = ttk.Label(displayFrame, image=displayImage)
        displayLabel.grid(row=0, column=0, sticky='NSEW', columnspan=2)
        displayLabel.configure(background='#0F1110')

        # Botones de la sección de Menú
        # Se define tmb su ubicación, nombre y estilo
        comboBurguerBaconButton = ttk.Button(comboBurguerBaconFrame, text='Mostrar',
                                             command=lambda: Display.displayComboBurguerBacon(comboBurguerBaconFrame,
                                                                                              comboBurguerVeggieFrame,
                                                                                              comboBurguerClasicaFrame,
                                                                                              comboBurguerEspecialFrame,
                                                                                              capuccinoFrame,
                                                                                              espressoFrame,
                                                                                              latteFrame,
                                                                                              muffinArandanoFrame,
                                                                                              muffinChipsFrame,
                                                                                              muffinChocolateFrame,
                                                                                              displayLabel, images))
        comboBurguerBaconButton.grid(row=0, column=1, padx=10)

        comboBurguerClasicaButton = ttk.Button(comboBurguerClasicaFrame, text='Mostrar',
                                               command=lambda: Display.displayComboBurguerClasica(
                                                   comboBurguerBaconFrame,
                                                   comboBurguerVeggieFrame,
                                                   comboBurguerClasicaFrame,
                                                   comboBurguerEspecialFrame,
                                                   capuccinoFrame, espressoFrame,
                                                   latteFrame,
                                                   muffinArandanoFrame,
                                                   muffinChipsFrame,
                                                   muffinChocolateFrame,
                                                   displayLabel, images))
        comboBurguerClasicaButton.grid(row=0, column=1, padx=10)

        comboBurguerEspecialButton = ttk.Button(comboBurguerEspecialFrame, text='Mostrar',
                                                command=lambda: Display.displayComboBurguerEspecial(
                                                    comboBurguerBaconFrame,
                                                    comboBurguerVeggieFrame,
                                                    comboBurguerClasicaFrame,
                                                    comboBurguerEspecialFrame,
                                                    capuccinoFrame,
                                                    espressoFrame, latteFrame,
                                                    muffinArandanoFrame,
                                                    muffinChipsFrame,
                                                    muffinChocolateFrame,
                                                    displayLabel, images))
        comboBurguerEspecialButton.grid(row=0, column=1, padx=10)

        comboBurguerVeggieButton = ttk.Button(comboBurguerVeggieFrame, text='Mostrar',
                                              command=lambda: Display.displayComboBurguerVeggie(comboBurguerBaconFrame,
                                                                                                comboBurguerVeggieFrame,
                                                                                                comboBurguerClasicaFrame,
                                                                                                comboBurguerEspecialFrame,
                                                                                                capuccinoFrame,
                                                                                                espressoFrame,
                                                                                                latteFrame,
                                                                                                muffinArandanoFrame,
                                                                                                muffinChipsFrame,
                                                                                                muffinChocolateFrame,
                                                                                                displayLabel, images))
        comboBurguerVeggieButton.grid(row=0, column=1, padx=10)

        capuccinoButton = ttk.Button(capuccinoFrame, text='Mostrar',
                                     command=lambda: Display.displayCapuccino(comboBurguerBaconFrame,
                                                                              comboBurguerVeggieFrame,
                                                                              comboBurguerClasicaFrame,
                                                                              comboBurguerEspecialFrame,
                                                                              capuccinoFrame, espressoFrame, latteFrame,
                                                                              muffinArandanoFrame, muffinChipsFrame,
                                                                              muffinChocolateFrame,
                                                                              displayLabel, images))
        capuccinoButton.grid(row=0, column=1, padx=10)

        espressoButton = ttk.Button(espressoFrame, text='Mostrar',
                                    command=lambda: Display.displayEspresso(comboBurguerBaconFrame,
                                                                            comboBurguerVeggieFrame,
                                                                            comboBurguerClasicaFrame,
                                                                            comboBurguerEspecialFrame,
                                                                            capuccinoFrame, espressoFrame, latteFrame,
                                                                            muffinArandanoFrame, muffinChipsFrame,
                                                                            muffinChocolateFrame,
                                                                            displayLabel, images))
        espressoButton.grid(row=0, column=1, padx=10)

        latteButton = ttk.Button(latteFrame, text='Mostrar',
                                 command=lambda: Display.displayLatte(comboBurguerBaconFrame, comboBurguerVeggieFrame,
                                                                      comboBurguerClasicaFrame,
                                                                      comboBurguerEspecialFrame,
                                                                      capuccinoFrame, espressoFrame, latteFrame,
                                                                      muffinArandanoFrame, muffinChipsFrame,
                                                                      muffinChocolateFrame,
                                                                      displayLabel, images))
        latteButton.grid(row=0, column=1, padx=10)

        muffinArandanoButton = ttk.Button(muffinArandanoFrame, text='Mostrar',
                                          command=lambda: Display.displayMuffinArandano(comboBurguerBaconFrame,
                                                                                        comboBurguerVeggieFrame,
                                                                                        comboBurguerClasicaFrame,
                                                                                        comboBurguerEspecialFrame,
                                                                                        capuccinoFrame, espressoFrame,
                                                                                        latteFrame, muffinArandanoFrame,
                                                                                        muffinChipsFrame,
                                                                                        muffinChocolateFrame,
                                                                                        displayLabel, images))
        muffinArandanoButton.grid(row=0, column=1, padx=10)

        muffinChipsButton = ttk.Button(muffinChipsFrame, text='Mostrar',
                                       command=lambda: Display.displayMuffinChips(comboBurguerBaconFrame,
                                                                                  comboBurguerVeggieFrame,
                                                                                  comboBurguerClasicaFrame,
                                                                                  comboBurguerEspecialFrame,
                                                                                  capuccinoFrame, espressoFrame,
                                                                                  latteFrame,
                                                                                  muffinArandanoFrame, muffinChipsFrame,
                                                                                  muffinChocolateFrame,
                                                                                  displayLabel, images))
        muffinChipsButton.grid(row=0, column=1, padx=10)

        muffinChocolateButton = ttk.Button(muffinChocolateFrame, text='Mostrar',
                                           command=lambda: Display.displayMuffinChocolate(comboBurguerBaconFrame,
                                                                                          comboBurguerVeggieFrame,
                                                                                          comboBurguerClasicaFrame,
                                                                                          comboBurguerEspecialFrame,
                                                                                          capuccinoFrame, espressoFrame,
                                                                                          latteFrame,
                                                                                          muffinArandanoFrame,
                                                                                          muffinChipsFrame,
                                                                                          muffinChocolateFrame,
                                                                                          displayLabel, images))
        muffinChocolateButton.grid(row=0, column=1, padx=10)

        # Botones de la sección de Display (Sección central de la app)
        # Se define tmb su ubicación, nombre y estilo
        # Botón para agregar un item a la orden
        addButton = ttk.Button(displayFrame, text='AGREGAR',
                               command=lambda: Order.add(orderTransactionLabel, orderTotalLabel, displayLabel))
        addButton.grid(row=1, column=0, padx=2, sticky='NSEW')
        # Botón para eliminar un item de la orden
        removeButton = ttk.Button(displayFrame, text='ELIMINAR',
                                  command=lambda: Order.remove(orderTransactionLabel, orderTotalLabel, displayLabel))
        removeButton.grid(row=1, column=1, padx=2, sticky='NSEW')

        # Boton de la sección de Pedido
        # Se define tmb su ubicación, nombre y estilo
        # Este botón sirve para generar el ticket del pedido
        orderButton = ttk.Button(orderFrame, text='PEDIR',
                                 command=lambda: Order.order(orderTransactionLabel, orderIDLabel,
                                                             orderTransactionLabel))
        orderButton.grid(row=4, column=0, sticky='EW')