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