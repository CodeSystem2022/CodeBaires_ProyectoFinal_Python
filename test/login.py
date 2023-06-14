# Importamos las clases y funciones necesarias de los módulos tkinter, messagebox,
# sqlite3 y PIL (Pillow).
# Estas bibliotecas se utilizan para:
# crear la interfaz gráfica,
from tkinter import *
# mostrar mensajes de error
from tkinter import messagebox
# acceder a una base de datos SQLite
import sqlite3
# trabajar con imágenes
from PIL import ImageTk, Image

class Login:
    # Esta variable la utilizaremos para almacenar la ventana de inicio de sesión más adelante
    login_window = None  # Definimos la variable login_window como global y le agregamos el valor None

    # La función verify_credentials se utiliza para verificar las credenciales de inicio de sesión
    # en una base de datos SQLite que previamente creamos y se encuentra en nuestro proyecto como database.sql
    def verify_credentials(username, password):

        # Establecemose una conexión con la base de datos,
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Verificar las credenciales en la base de datos
        # Ejecutamos una consulta para buscar las credenciales proporcionadas en la tabla de usuarios
        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
        # Obtenemos el resultado y se lo asignamos a la variable result
        result = cursor.fetchone()

        # Si las credenciales son válidas, se destruye la ventana de inicio de sesión
        # y se importa y muestra el módulo main (que contiene nuestra aplicación)
        if result:
            login_window.destroy()
            import main
            main.show_app()
        # Si las credenciales son incorrectas, se muestra un mensaje de error
        # utilizando messagebox.showerror()
        else:
            messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")
        # Cerramos la conexión con la base de datos
        conn.close()


    def show_login(self=None):
        # Declaramos la variable login_window como global para que pueda ser accedida y modificada dentro de la función
        global login_window  # Acceder a la variable login_window global
        def iniciar_sesion():
            # Instanciamos el username y el password y se lo pasamos a la función verify_credentials()
            username = entry_username.get()
            password = entry_password.get()
            Login.verify_credentials(username, password)
        # Creamos una instancia de la clase Tk() para crear la ventana de inicio de sesión
        login_window = Tk()
        # Establecemos el título de la ventana
        login_window.title("Mc UTN - Inicio de sesión")
        # Establecemos el tamaño de esa ventana
        login_window.geometry("400x300+500+300")
        # Cargamos una imagen para el fondo utilizando Pillow (PIL)
        background_image = Image.open('images/display_default.png').resize((400, 300))
        # la convertimos en un objeto PhotoImage compatible con Tkinter
        background_photo = ImageTk.PhotoImage(background_image)

        # Creamos un widget Label para mostrar la imagen de fondo
        background_label = Label(login_window, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # En el label le asignamos los estilos
        # text: le asigna el texto
        # font: le asigna el tipo de fuente, tamaño y estilo al texto
        # fg: es el color que va a tener el texto
        # bg: es el color que va a tener de fondo
        # padx: se agrega un relleno de 10 píxeles a la izquierda y a la derecha del texto
        # pady: se agrega un relleno de 2 píxeles encima y debajo del texto
        # Lo mismo para el resto de las label
        label_username = Label(login_window,
                               text="Nombre de usuario",
                               font=('Franklin Gothic', 10, 'bold'),
                               bg='#F0F0F0',
                               fg='#333333',
                               padx=10,
                               pady=2
                               )
        # Utilizamos el método pack() para colocar el widget Label dentro de la ventana de inicio de sesión

        label_username.pack(pady=(50, 10))
        entry_username = Entry(login_window, font=('Franklin Gothic', 10))
        entry_username.pack(pady=10)

        label_password = Label(login_window,
                               text="Contraseña",
                               font=('Franklin Gothic', 10, 'bold'),
                               bg='#F0F0F0',
                               fg='#333333',
                               padx=10,
                               pady=2
                               )

        label_password.pack(pady=10)
        entry_password = Entry(login_window, show="*", font=('Franklin Gothic', 10))
        entry_password.pack(pady=10)

        button_login = Button(login_window, text="Iniciar sesión", font=('Franklin Gothic', 10, 'bold'), command=iniciar_sesion)
        button_login.configure(bg='#952616', fg='#FFFFFF', activebackground='#0056b3', activeforeground='#FFFFFF')
        button_login.pack(pady=30)

        # Cuando llamamos a login_window.mainloop(), la ventana de inicio de sesión se muestra en
        # la pantalla y espera a que el usuario interactúe con ella.
        # Durante este tiempo, el método mainloop() procesa los eventos de la ventana, como clics de botones,
        # entradas de teclado, etc. Esto permite que la ventana responda a las acciones del usuario
        # y actualice su contenido en consecuencia.
        # El bucle mainloop() continúa ejecutándose hasta que se cierre la ventana de inicio de sesión
        # o se llame explícitamente al método destroy() en la ventana.
        # Una vez que la ventana se cierra, el control retorna desde mainloop()
        # y el programa puede continuar ejecutando otras instrucciones que en este caso se las pasamos desde
        # el archivo main.py (abre nuestra aplicación principal).
        login_window.mainloop()