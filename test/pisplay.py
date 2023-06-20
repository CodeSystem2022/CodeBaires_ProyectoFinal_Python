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

        ##
        comboBurguerVeggieFrame.configure(style='DishFrame.TFrame')
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
            image= burguerBaconImage,
            text='Combo Bacon Burguer',
            font=('Franklin Gothic', 10, 'bold'),
            foreground='white',
            compound='bottom',
            padding=(2, 2, 2, 2)
        )


