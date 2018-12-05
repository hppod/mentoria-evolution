import pandas as pd

dataset = pd.read_csv('kc_house_data.csv', sep=',')

# LISTANDO IMOVEIS COM 3 QUARTOS E COM BANHEIROS MAIOR IGUAL A 2
threeBedroomTwoOrMoreBathrooms = dataset.loc[(
    dataset['bedrooms'] == 3) & (dataset['bathrooms'] > 2)]

print(threeBedroomTwoOrMoreBathrooms)
