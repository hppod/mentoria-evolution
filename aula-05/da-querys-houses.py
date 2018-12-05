import pandas as pd

dataset = pd.read_csv('kc_house_data.csv', sep=',')

# LISTANDO IMOVEIS COM 3 QUARTOS E COM BANHEIROS MAIOR IGUAL A 2
threeBedroomTwoOrMoreBathrooms = dataset.loc[(
    dataset['bedrooms'] == 3) & (dataset['bathrooms'] > 2)]

print(threeBedroomTwoOrMoreBathrooms)

# CONTANDO A QUANTIDADE DE IMOVEIS COM 4 QUARTOS
countFourBedrooms = dataset[dataset['bedrooms'] == 4].count()
print(countFourBedrooms)

# ORDENANDO O DATASET PELA COLUNA PREÇO POR ORDEM DECRESCENTE
priceAscendingFalse = dataset.sort_values(by='price', ascending=False)
print(priceAscendingFalse)

# AGRUPANDO E CONTANDO A QUANTIDADE DE IMOVEIS POR TAMANHO DE QUARTOS
groupCountBedrooms = dataset.bedrooms.value_counts()
print(groupCountBedrooms)

groupCountBathrooms = dataset.bathrooms.value_counts()
print(groupCountBathrooms)