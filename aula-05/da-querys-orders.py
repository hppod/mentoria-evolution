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

# CONSULTANDO DADOS NOS DOIS DATASETS E JUNTANDO-OS ATRAVÉS DA CHAVER ORDER_ID
df_query = pd.merge(orders[['order_id', 'order_status', 'order_approved_at']], orders_items[[
                    'order_id', 'product_id', 'seller_id', 'price', 'freight_value']], on='order_id')

headDfQuery = df_query.head()
print(headDfQuery)