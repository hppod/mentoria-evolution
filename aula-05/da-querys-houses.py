import pandas as pd

dataset = pd.read_csv('kc_house_data.csv', sep=',')

# LISTANDO IMOVEIS COM 3 QUARTOS E COM BANHEIROS MAIOR IGUAL A 2
threeBedroomTwoOrMoreBathrooms = dataset.loc[(
    dataset['bedrooms'] == 3) & (dataset['bathrooms'] > 2)]

print(threeBedroomTwoOrMoreBathrooms)

# CONTANDO A QUANTIDADE DE IMOVEIS COM 4 QUARTOS
countFourBedrooms = dataset[dataset['bedrooms']==4].count()
print(countFourBedrooms)