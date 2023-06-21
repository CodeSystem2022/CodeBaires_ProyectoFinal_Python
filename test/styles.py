
from tkinter import ttk

# --------------------------------- ESTILOS ------------------------- #
# En esta clase instanciamos los frames o marcos en los que vamos a poner cada cosa
# de nuestra app desktop como el marco del menu, el marco de imagen y el marco de la orden 

# Usamos los estilos disponibles de la librería tkinter. La opción ttk nos permite usar los nuevos widget que
# ofrece esta librería, lo que le da un estilo más moderno a la aplicación

class Styles:
    def configure_styles(self=None):

        # Creamos el objeto style (que es una instancia de la clase Style del módulo ttk de la biblioteca tkinter)
        # Nos permite acceder a los estilos predefinidos y personalizar los estilos de los widgets proporcionados por ttk

        style = ttk.Style()

        """ Explicamos cada propiedad de los estilos:
         background: color de fondo
         relief: relieve
         anchor: para controlar la posición y la alineación de un widget dentro de su celda en la cuadrícula
         font: tipo de fuente, tamaño, etc
         foreground: color del texto
         padding: para el espaciado a cada lado del widget. Es útil para mejorar la legibilidad y la apariencia de los widgets al agregar un espacio uniforme entre el contenido
         y los bordes del widget
         width: ancho
         wraplength: para especificar la longitud máxima de línea antes de que se produzca un salto de línea automático
         justify: justificado del texto 
         """

        # Configuramos el marco o frame test y le asignamos un nombre para poder utilizarlo en otra parte de nuestro código
        style.configure('MainFrame.TFrame', background='#2B2B28')
        # Configuramos el marco o frame del menú y le asignamos un nombre para poder utilizarlo en otra parte de nuestro código
        style.configure('MenuFrame.TFrame', background='#4A4A48')
        # Configuramos el marco o frame de la imagen central y le asignamos un nombre para poder utilizarlo en otra parte de nuestro código
        style.configure('DisplayFrame.TFrame', background='#0F1110')
        # Configuramos el marco o frame de la orden y le asignamos un nombre para poder utilizarlo en otra parte de nuestro código
        style.configure('OrderFrame.TFrame', background='#B7C4CF')
        # Configuramos el marco o frame de los platos disponibles del menú y le asignamos un nombre para poder utilizarlo en otra parte de nuestro código
        style.configure('DishFrame.TFrame', background='#4A4A48', relief='raised')
        # Configuramos los frames de cada opción de menú y le asignamos un nombre para poder utilizarlo en otra parte de nuestro código
        style.configure('selectedDish.TFrame', background='#7a1b0c')
        # Configuramos las labels (etiquetas) del menú y le asignamos un nombre para poder utilizarlo en otra parte de nuestro código
        style.configure('MenuLabel.TLabel',
                        background='#0F1110',
                        anchor='center',
                        font=('Franklin Gothic', 8, 'normal'),
                        foreground='white',
                        padding=(2, 2, 2, 2),
                        width=50
                        )
        # Configuramos las labels (etiquetas) de la sección de orden y le asignamos un nombre para poder utilizarlo en otra parte de nuestro código
        style.configure('orderTotal.TLabel',
                        background='#0F1110',
                        anchor='w',
                        font=('Franklin Gothic', 10, 'bold'),
                        foreground='white',
                        padding=(2, 2, 2, 2),
                        )
        style.configure('orderTransaction.TLabel',
                        background='#4A4A48',
                        anchor='nw',
                        font=('Franklin Gothic', 10),
                        foreground='white',
                        wraplength=280,  # Esto sirve para que quede el texto en la misma linea
                        justify='left',
                        padding=(3, 3, 3, 3),
                        )


