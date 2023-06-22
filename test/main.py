# Utilizamos la librería tkinter que sirve para desarrollar la interfaz gráfica de
# nuestra aplicación
from tkinter import *

# Importamos las clases creadas previamente y sus métodos
from frames import Frames
from grid_configurations import Grid_configurations
from styles import Styles
from widgets import Widgets
from images import Images
# Importamos el módulo login para mostrar la ventana de inicio de sesión.
from login import Login

# La clase main configura y muestra la ventana principal de la aplicación,
# crea los elementos de la interfaz gráfica y establece la interacción con el usuario
# a través del ciclo de eventos de la ventana.
def show_app():
    # Creamos instancia de la clase Tk() que representa la ventana principal de la aplicación
    # le asignamos el nombre root.
    root = Tk()
    # Le asignamos el título a nuestra ventana de la aplicación
    root.title("Mc UTN -- By CodeBaires")
    root.resizable(False, False)

    # Instanciamos el diccionario de imágenes utilizando la función load_images() del archivo images.py
    images = Images.load_images()

    # Creación de frames o marcos
    # Utilizamos la función create_frames() del archivo frames.py para crearlos
    frames = Frames.create_frames(root)
    # Asignamos cada frame o marco a una variable
    mainFrame = frames['mainFrame']
    topBannerFrame = frames['topBannerFrame']
    menuFrame = frames['menuFrame']
    displayFrame = frames['displayFrame']
    orderFrame = frames['orderFrame']
    comboBurguerBaconFrame = frames['comboBurgerBaconFrame']
    comboBurguerClasicaFrame = frames['comboBurguerClasicaFrame']
    comboBurguerEspecialFrame = frames['comboBurguerEspecialFrame']
    comboBurguerVeggieFrame = frames['comboBurguerVeggieFrame']
    capuccinoFrame = frames['capuccinoFrame']
    espressoFrame = frames['espressoFrame']
    latteFrame = frames['latteFrame']
    muffinArandanoFrame = frames['muffinArandanoFrame']
    muffinChipsFrame = frames['muffinChipsFrame']
    muffinChocolateFrame = frames['muffinChocolateFrame']

    # Configuramos grid o grilla
    # Así podemos establecer el diseño de los frames o marcos en nuestra ventana de la aplicación.
    # utilizamos la función configure_grid() del archivo grid_configurations.py
    Grid_configurations.configure_grid(mainFrame, menuFrame, orderFrame)

    # Configuramos estilos de los widgets (fuente, color, etc)
    # # utilizamos la función configure_styles() del archivo styles.py
    Styles.configure_styles()

    # Creamos los widgets
    # Cada uno se ubica en el frame o marco correspondiente utilizando la función create_widgets()
    # del archivo widgets.py
    # También le pasamos el diccionario de imágenes que instanciamos previamente.

    Widgets.create_widgets(topBannerFrame, menuFrame, displayFrame, orderFrame,
                   comboBurguerBaconFrame, comboBurguerVeggieFrame, comboBurguerClasicaFrame,
                   comboBurguerEspecialFrame, capuccinoFrame, espressoFrame, latteFrame,
                   muffinArandanoFrame, muffinChipsFrame, muffinChocolateFrame, images)
    # Se llama al método mainloop() para iniciar el ciclo de eventos
    # y mantener la ventana de la aplicación en ejecución.
    root.mainloop()


if __name__ == "__main__":
    # Llamamos a la función show_login() del archivo login.py,
    # lo que significa que cuando ejecutemos el archivo main.py directamente,
    # se mostrará la ventana de inicio de sesión.
    Login.show_login()