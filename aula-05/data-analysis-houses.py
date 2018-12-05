# IMPORTANDO A BIBLIOTECA PANDAS
import pandas as pd

# DEFININDO O DATASET
dataset = pd.read_csv('kc_house_data.csv', sep=',')

# VERIFICANDO O TIPO DO DATASET
tipoDataset = type(dataset)
print(tipoDataset)

# VERIFICANDO INFORMAÇÕES DO DATASET
dataset.info()

# IMPRIMINDO O DATASET
print(dataset)

# IMPRIMINDO APENAS OS 10 PRIMEIROS REGISTROS DO DATASET
firstTen = dataset.head(10)
print(firstTen)