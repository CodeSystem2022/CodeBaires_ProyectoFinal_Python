# --------------------------------- CONFIGURACIONES GRID O GRILLA ------------------------- #
# En esta clase configuramos el grid o grilla de la interfaz gráfica
# En esta función definimos las configuraciones de las columnas y filas de los marcos
# (mainFrame, menuFrame y orderFrame).

class Grid_configurations:
    def configure_grid(mainFrame, menuFrame, orderFrame):

        #En esta parte se configura la estructura de grilla del mainFrame.
        # mainFrame.columnconfigure(2, weight=1) establece que la columna 2 (tercera columna) del mainFrame
        # debe expandirse y ocupar el total del espacio disponible en el ancho
        # mainFrame.rowconfigure(1, weight=1) configura que la fila 1 (segunda fila) del mainFrame
        # también debe expandirse y ocupar el total del espacio disponible en el alto.
        mainFrame.columnconfigure(2, weight=1)
        mainFrame.rowconfigure(1, weight=1)


        # En esta sección se configura la estructura de grilla del menuFrame.
        # Se establece que la columna 0 (primera columna) del menuFrame debe expandirse y ocupar
        # el total del espacio disponible en el ancho.
        # Luego, se configuran las filas del 1 al 10 para que se expandan y ocupen el total del espacio
        # disponible en el alto.
        menuFrame.columnconfigure(0, weight=1)
        menuFrame.rowconfigure(1, weight=1)
        menuFrame.rowconfigure(2, weight=1)
        menuFrame.rowconfigure(3, weight=1)
        menuFrame.rowconfigure(4, weight=1)
        menuFrame.rowconfigure(5, weight=1)
        menuFrame.rowconfigure(6, weight=1)
        menuFrame.rowconfigure(7, weight=1)
        menuFrame.rowconfigure(8, weight=1)
        menuFrame.rowconfigure(9, weight=1)
        menuFrame.rowconfigure(10, weight=1)


        # Aca configuramos la estructura de grilla del orderFrame.
        # La columna 0 (primera columna) del orderFrame se configura para expandirse y ocupar el total del
        # espacio disponible en el ancho.
        # La fila 2 (tercera fila) del orderFrame también se configura para expandirse y ocupar el total del
        # espacio disponible en el alto.
        orderFrame.columnconfigure(0, weight=1)
        orderFrame.rowconfigure(2, weight=1)

    # Estas configuraciones de grilla permiten que los elementos dentro de cada marco
    # se ajusten y ocupen el espacio disponible correctamente.
