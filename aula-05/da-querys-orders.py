# CONSULTANDO DADOS EM MAIS DE UM DATASET

import pandas as pd

# CARREGANDO O DATASET DE PEDIDOS
orders = pd.read_csv('olist_orders_dataset.csv')

headOrders = orders.head()
print(headOrders)

# CARREGANDO O DATASET DE ITENS PEDIDOS
orders_items = pd.read_csv('olist_order_items_dataset.csv')

headOrderItems = orders_items.head()
print(headOrderItems)