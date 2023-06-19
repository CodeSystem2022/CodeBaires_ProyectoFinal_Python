
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

        # Explicamos cada propiedad de los estilos:
        # background: color de fondo
        # relief: relieve
        # anchor: para controlar la posición y la alineación de un widget dentro de su celda en la cuadrícula
        # font: tipo de fuente, tamaño, etc
        # foreground: color del texto
        # padding: para el espaciado a cada lado del widget. Es útil para mejorar la legibilidad y la apariencia de los widgets al agregar un espacio uniforme entre el contenido
        # y los bordes del widget
        # width: ancho
        # wraplength: para especificar la longitud máxima de línea antes de que se produzca un salto de línea automático
        # justify: justificado del texto