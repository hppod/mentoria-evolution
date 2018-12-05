import pandas as pd

dataset = pd.read_csv('kc_house_data.csv', sep=',')

tipoDataset = type(dataset)
print(tipoDataset)