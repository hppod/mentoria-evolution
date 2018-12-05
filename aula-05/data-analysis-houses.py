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

# RETORNANDO APENAS IMOVEIS COM 3 QUARTOS
threeBedrooms = dataset.loc[dataset['bedrooms']==3]
print(threeBedrooms)

# RETORNANDO IMOVEIS UNICOS
uniqueId = dataset.id.unique()
print(uniqueId)

# RETORNANDO NUMEROS DE QUARTOS DISPONIVEIS NO DATASET
uniqueBedrooms = dataset.bedrooms.unique()
print("Unique Bedrooms", uniqueBedrooms)

# RETORNANDO O NUMERO DE BANHEIROS DOS 10 PRIMEIROS IMOVEIS DO DATASET
firstTenBathrooms = dataset.bathrooms.head(10)
print("First Ten Bathrooms", firstTenBathrooms)

# RETORNANDO A MEDIA DE BANHEIROS DO DATASET
meanBathrooms = dataset.bathrooms.mean()
print("Mean Bathrooms", meanBathrooms)

# RETORNANDO A CONTAGEM DE REGISTROS DO DATASET
countDataset = dataset.count()
print(countDataset)

# RETORNANDO O NOME DAS COLUNAS DO DATASET
nameColumns = dataset.columns
print(nameColumns)