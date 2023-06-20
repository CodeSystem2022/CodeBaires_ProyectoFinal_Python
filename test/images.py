# Utilizamos Pillow (PIL) que es una librería que sirve para abrir, manipular y guardar
# distintos formatos de imágenes
# Importamos las clases Image y ImageTk del módulo Pillow.
# Image se utiliza para abrir y manipular imágenes
# ImageTk se utiliza para convertir las imágenes en un formato compatible con la biblioteca Tkinter.
from PIL import Image, ImageTk

# --------------------------------- IMAGENES ------------------------- #
# En esta clase instanciamos las imagenes con las que vamos a trabajar
# y establecemos su ancho y alto. Generamos un método que se llamará load_images que
# nos devuelve las imágenes que cargamos desde nuestra carpeta images

class Images:
    def load_images(self=None):

        # En esta parte se carga la imagen del logo desde el archivo 'images/logo_codebaires.png'.
        # Luego, se redimensiona la imagen a un tamaño de 200x200 píxeles utilizando el método resize().
        # El objeto de imagen resultante se asigna a logoImageObject.
        # A continuación, se convierte logoImageObject a un formato compatible con Tkinter
        # utilizando ImageTk.PhotoImage(), y se asigna a logoImage.
        # Este proceso lo repetimos para cada una de las imágenes que se cargan en nuestra aplicación,
        # ajustando el tamaño y convirtiéndolas en objetos PhotoImage.

        # Imagen del logo de la aplicación
        logoImageObject = Image.open('images/logo_codebaires.png').resize((200, 200))
        logoImage = ImageTk.PhotoImage(logoImageObject)

        # Imagen del banner de arriba de la aplicación
        topBannerImageObject = Image.open('images/mcUTN_top_banner.png').resize((800, 200))
        topBannerImage = ImageTk.PhotoImage(topBannerImageObject)

        # Imagen central de la aplicación
        displayImageObject = Image.open('images/display_default.png').resize((380, 420))
        displayImage = ImageTk.PhotoImage(displayImageObject)

        # Imagenes del menú

        burguerBaconImageObject = Image.open('images/menu/burguer_bacon.png')
        burguerBaconImage = ImageTk.PhotoImage(burguerBaconImageObject)

        burguerClasicaImageObject = Image.open('images/menu/burguer_clasica.png')
        burguerClasicaImage = ImageTk.PhotoImage(burguerClasicaImageObject)

        burguerEspecialImageObject = Image.open('images/menu/burguer_especial.png')
        burguerEspecialImage = ImageTk.PhotoImage(burguerEspecialImageObject)

        burguerVeggieImageObject = Image.open('images/menu/burguer_veggie.png')
        burguerVeggieImage = ImageTk.PhotoImage(burguerVeggieImageObject)

        capuccinoImageObject = Image.open('images/menu/capuccino.png')
        capuccinoImage = ImageTk.PhotoImage(capuccinoImageObject)

        espressoImageObject = Image.open('images/menu/espresso.png')
        espressoImage = ImageTk.PhotoImage(espressoImageObject)

        latteImageObject = Image.open('images/menu/latte.png')
        latteImage = ImageTk.PhotoImage(latteImageObject)

        muffinArandanoImageObject = Image.open('images/menu/muffin_arandano.png')
        muffinArandanoImage = ImageTk.PhotoImage(muffinArandanoImageObject)

        muffinChipsImageObject = Image.open('images/menu/muffin_chips.png')
        muffinChipsImage = ImageTk.PhotoImage(muffinChipsImageObject)

        muffinChocolateImageObject = Image.open('images/menu/muffin_choco.png')
        muffinChocolateImage = ImageTk.PhotoImage(muffinChocolateImageObject)

        # Agregamos un return a nuestra función load_images() para que nos
        # retorne un diccionario que contiene todos los objetos PhotoImage correspondientes a cada imagen cargada.
        # Estos objetos los utilizaremos para mostrar las imágenes en la interfaz gráfica de nuestra aplicación
        return {
            'logoImage': logoImage,
            'topBannerImage': topBannerImage,
            'displayImage':displayImage,
            'burguerBaconImage': burguerBaconImage,
            'burguerClasicaImage': burguerClasicaImage,
            'burguerEspecialImage': burguerEspecialImage,
            'burguerVeggieImage': burguerVeggieImage,
            'capuccinoImage': capuccinoImage,
            'espressoImage': espressoImage,
            'latteImage': latteImage,
            'muffinArandanoImage': muffinArandanoImage,
            'muffinChipsImage': muffinChipsImage,
            'muffinChocolateImage': muffinChocolateImage
        }