# CONSULTANDO DADOS EM MAIS DE UM DATASET

import pandas as pd

# CARREGANDO O DATASET DE PEDIDOS
orders = pd.read_csv('olist_orders_dataset.csv')

headDataset = orders.head()
print(headDataset)