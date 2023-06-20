# En esta clase guardamos los métodos o funciones que se van a encargar de mostrar en el sector display 
# (sector central de la app) las imágenes y los nombres correspondientes a cada ítem del menú 

class Display:
    # Toma los parámetros: comboBurguerBaconFrame, comboBurguerVeggieFrame, comboBurguerClasicaFrame, comboBurguerEspecialFrame,
    # capuccinoFrame, espressoFrame, latteFrame, muffinArandanoFrame, muffinChipsFrame, muffinChocolateFrame,
    # displayLabel, images
    def displayComboBurguerBacon(comboBurguerBaconFrame, comboBurguerVeggieFrame, comboBurguerClasicaFrame, comboBurguerEspecialFrame,
                                capuccinoFrame, espressoFrame, latteFrame, muffinArandanoFrame, muffinChipsFrame, muffinChocolateFrame,
                                displayLabel, images):
        burguerBaconImage = images['burguerBaconImage']
        comboBurguerBaconFrame.configure(
            relief='sunken', # le asigna al marco o frame que va a contener este item un relieve hundido
            style='selectedDish.TFrame' # le asigna el estilo configurado en la clase style para selectedDish que sería el item seleccionado
        )

                                    
        #  Configuramos el estilo del resto de los otros marcos
        #  para asegurarnos de que solo el marco correspondiente esté distinto
        comboBurguerVeggieFrame.configure(style='DishFrame.TFrame')
        comboBurguerClasicaFrame.configure(style='DishFrame.TFrame')
        comboBurguerEspecialFrame.configure(style='DishFrame.TFrame')
        capuccinoFrame.configure(style='DishFrame.TFrame')
        espressoFrame.configure(style='DishFrame.TFrame')
        latteFrame.configure(style='DishFrame.TFrame')
        muffinArandanoFrame.configure(style='DishFrame.TFrame')
        muffinChipsFrame.configure(style='DishFrame.TFrame')
        muffinChocolateFrame.configure(style='DishFrame.TFrame')

        # Configuramos el estilo para la imagen y el nombre que se va a ver en el sector display
        # en el centro de nuestra aplicación
        displayLabel.configure(
            image= burguerBaconImage,
            text='Combo Bacon Burguer',
            font=('Franklin Gothic', 10, 'bold'),
            foreground='white',
            compound='bottom',
            padding=(2, 2, 2, 2)
        )


        comboBurguerBaconFrame.configure(style='DishFrame.TFrame')
        comboBurguerClasicaFrame.configure(style='DishFrame.TFrame')
        comboBurguerEspecialFrame.configure(style='DishFrame.TFrame')
        capuccinoFrame.configure(style='DishFrame.TFrame')
        espressoFrame.configure(style='DishFrame.TFrame')
        latteFrame.configure(style='DishFrame.TFrame')
        muffinArandanoFrame.configure(style='DishFrame.TFrame')
        muffinChipsFrame.configure(style='DishFrame.TFrame')
        muffinChocolateFrame.configure(style='DishFrame.TFrame')



        ##
        displayLabel.configure(
            image=burguerVeggieImage,
            text='Combo Veggie Burguer',
            font=('Franklin Gothic', 10, 'bold'),
            foreground='white',
            compound='bottom',
            padding=(2, 2, 2, 2)
        )


        ##
        def displayComboBurguerClasica(comboBurguerBaconFrame, comboBurguerVeggieFrame, comboBurguerClasicaFrame, comboBurguerEspecialFrame,
                                capuccinoFrame, espressoFrame, latteFrame, muffinArandanoFrame, muffinChipsFrame, muffinChocolateFrame,
                                displayLabel, images):
        # Instanciamos la imagen correspondiente al item del menú, la traemos de images.py
        burguerClasicaImage = images['burguerClasicaImage']

        comboBurguerClasicaFrame.configure(
            relief='sunken',  # le asigna al marco o frame que va a contener este item un relieve hundido
            style='selectedDish.TFrame' # le asigna el estilo configurado en la clase style para selectedDish que sería el item seleccionado
        )


