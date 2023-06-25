# importamos random para generar un nombre aleatorio para nuestro pedido
import random
# Importamos datetime para la fecha y hora
from datetime import datetime

# En este archivo guardamos las funciones relacionadas con el procesamiento de pedidos
# de nuestra aplicación


class Order:
    # Agregamos un diccionario con los precios correspondientes a cada plato del menú
    prices = {
            'Combo Bacon Burguer': 1200,
            'Combo Burguer Clasica': 1000,
            'Combo Burguer Especial': 1500,
            'Combo Veggie Burguer': 1000,
            'Mc Capuccino': 950,
            'Mc Espresso': 600,
            'Mc Latte': 700,
            'Muffin de Arandanos': 550,
            'Muffin de Vainilla con chips': 550,
            'Muffin de Chocolate': 550
    }

    # El nuestras funciones utilizamos el método cget() que es propio de tkinter
    # para obtener el valor actual de una opción o configuración de un widget.
    # El nombre "cget" proviene de "get configuration".

    # Función para agregar ítems del menú en la orden
    def add(orderTransactionLabel, orderTotalLabel, displayLabel):
        #Actualizamos el detalle de la orden añadiendo el ítem seleccionado y su precio
        current_order = orderTransactionLabel.cget('text')
        # Concatenamos el nombre del ítem con el precio correspondiente en formato string,
        # para formar la variable added_menu_item. Esto los hacemos para tener una representación
        # completa del ítem a agregar en el formato "nombre - $precio".
        added_menu_item = displayLabel.cget('text') + "  - $" + str(Order.prices[displayLabel.cget('text')]) + '.-\n'
        updated_order = current_order + added_menu_item
        orderTransactionLabel.configure(text=updated_order)

        # Actualizamos el total de la orden sumando el precio del ítem seleccionado
        order_total = orderTotalLabel.cget('text').replace('TOTAL: ', '')
        order_total = order_total.replace('$','')
        updated_total = int(order_total) + Order.prices[displayLabel.cget('text')]
        orderTotalLabel.configure(text='TOTAL: $' + str(updated_total))

    # Función para eliminar ítems del menú en la orden
    def remove(orderTransactionLabel, orderTotalLabel, displayLabel):

        # Concatenamos el nombre del ítem con el precio correspondiente en formato string,
        # para formar la variable menu_item_to_remove. Esto los hacemos para tener una representación
        # completa del ítem a eliminar en el formato "nombre - $precio".
        menu_item_to_remove = displayLabel.cget('text') + "  - $" + str(Order.prices[displayLabel.cget('text')])
        # Creo una lista y hago un split desde lo último que está escrito en cada item de la orden
        # orderTransactionLabel representa la lista actual de ítems en la orden.
        transaction_list = orderTransactionLabel.cget('text').split('.-\n')
        # El método pop realiza dos acciones:
        #
        # Elimina el elemento de la lista.
        # Devuelve el elemento eliminado.
        # Al utilizar pop con un índice específico, se puede eliminar y obtener un elemento en una posición
        # específica de la lista. Si no se proporciona un índice, pop eliminará y devolverá el último elemento
        # de la lista. Nos permite modificar la lista original y obtener el elemento eliminado al mismo tiempo
        # Utilizamos pop para que no nos quede ('.- ') después de hacer la eliminación del elemento
        # así no nos queda un último elemento vacío de la lista
        transaction_list.pop(len(transaction_list) - 1)

        # Verificamos que menu_item_to_remove esté presente en la lista transaction_list
        if menu_item_to_remove in  transaction_list:
            # Actualizamos la lista de los pedidos cuando lo eliminamos
            transaction_list.remove(menu_item_to_remove)
            # Creamos la variable updated_order
            updated_order = ''
            # recorremos la lista transaction_list para construir nuevamente el texto de la orden actualizada.
            # Cada ítem se concatena con '.-\n' para mantener el formato original.
            for item in transaction_list:
                updated_order += item + '.-\n'
            # Utilizamos el método configure en orderTransactionLabel para actualizar
            # su texto con updated_order, que representa la lista de ítems actualizada.
            orderTransactionLabel.configure(text=updated_order)

            # Actualizamos el monto total al eliminar el plato
            order_total = orderTotalLabel.cget('text').replace('TOTAL: ', '')
            order_total = order_total.replace('$', '')
            # Calculamos el nuevo monto total restando el precio del ítem eliminado
            # utilizando prices[displayLabel.cget('text')], y los guardamos en la variable updated_total.
            updated_total = int(order_total) - Order.prices[displayLabel.cget('text')]
            orderTotalLabel.configure(text='TOTAL: $' + str(updated_total))

    # Función para generar un id único para el pedido
    # Genera un ID único para el pedido al combinar letras y números aleatorios y agregar un prefijo específico
    # Este ID se utilizará para identificar de manera única cada pedido realizado.
    def order_id(self=None):
        # Creamos una lista con numeros y otra con letras
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                   'V', 'W', 'X', 'Y', 'Z']

        # Inicializamos la variable order_id_name con el valor inicial "McUTN_".
        # Esta variable almacenará el ID del pedido generado
        order_id_name = 'McUTN_'

        # Inicializamos las variables random_letters y random_numbers con valores vacíos.
        # Estas variables se utilizarán para almacenar letras y números aleatorios
        random_letters = ''
        random_numbers = ''

        for i in range(0, 3): # Elegimos 3 letras y 3 números, podría ser la extensión que quisiéramos
            # Se selecciona aleatoriamente una letra de la lista letters
            # utilizando la función random.choice(letters)
            # La letra seleccionada se agrega a la variable random_letters utilizando el operador +=
            random_letters += random.choice(letters)
            # Se selecciona aleatoriamente un número de la lista numbers
            # utilizando la función random.choice(numbers).
            # El número seleccionado se convierte a string y se agrega a la variable random_numbers
            # utilizando también el operador +=
            random_numbers += str(random.choice(numbers))

        # Después del ciclo, se concatenan las variables random_letters y random_numbers con la variable order_id_name
        # para formar el ID completo del pedido.
        order_id_name += random_letters + random_numbers
        # Finalmente, retornamos el valor de order_id_name
        return order_id_name

    # Función para generar la orden y el recibo de la misma
    # Tiene como objetivo generar y guardar el recibo del pedido en un archivo de texto.
    # Toma los datos del pedido, crea un archivo de texto con el recibo del pedido,
    # guarda la información del pedido en el archivo y actualiza la interfaz de usuario
    # para mostrar un mensaje de confirmación.
    def order(orderIDLabel, orderTransactionLabel, orderTotalLabel):
        # Obtenemos el texto actual del widget orderIDLabel y lo asignamos a la variable new_ticket.
        new_ticket = orderIDLabel.cget('text')

        # Eliminamos el prefijo "Id. Pedido: " del texto de new_ticket utilizando el método replace.
        new_ticket = new_ticket. replace('Id. Pedido: ','')
        # Creo una lista y hago un split desde lo último que está escrito en cada item de la orden
        transaction_list = orderTransactionLabel.cget('text').split('.-\n')
        # Utilizamos pop para que no nos quede ('.- ') después de hacer la eliminación del elemento
        # así no nos queda un último elemento vacío de la lista
        transaction_list.pop(len(transaction_list) - 1)
        # Obtengo la fecha y hora actual
        order_day = datetime.today()
        order_time = datetime.now()

        # Iteramos sobre los elementos de la lista transaction_list y
        # agregamos y punto y un salto de línea al final de cada elemento.
        for item in transaction_list:
            item += '.-\n'

        # Ruta donde voy a guardar mi archivo ticket
        file_path = f'./ticket_order/{new_ticket}.txt'
        # Utilizamos with para abrir y escribir en el archivo que vamos a generar para guardar nuestro ticket
        with open(file_path, 'w') as file: # Le paso el nombre que va a tener el recibo
            file.write('----------------------------------------------------------')
            file.write('\n')  # Salto de línea
            file.write('                          Mc UTN                          ')
            file.write('\n') # Salto de línea
            file.write('----------------------------------------------------------')
            file.write('\n') # Salto de línea
            file.write(order_day.strftime('%d/%m/%Y')) # Lo formateamos para que quede dd/mm/YYYY
            file.write('\n') # Salto de línea
            file.write(order_time.strftime('%H:%M:%S')) # Lo formateamos para que quede HH/MM/SS
            file.write('\n\n') # Doble salto de línea
            for item in transaction_list: # Agregamos todos los items del pedido
                file.write(item + '\n')
            file.write('\n\n')  # Doble salto de línea
            file.write('----------------------------------------------------------')
            file.write('\n')  # Salto de línea
            file.write(orderTotalLabel.cget('text'))
            file.write('\n')  # Salto de línea
            file.write('----------------------------------------------------------')

        # Actualizamos el mensaje de generación de archivo
        orderTransactionLabel.configure(text=f'Se generó tu ticket\n Id: {new_ticket}',
                                        font=('Franklin Gothic', 12, 'bold'),
                                        anchor='center')
