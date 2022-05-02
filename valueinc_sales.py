# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 12:09:03 2022

@author: Michael
"""
import pandas as pd
data =pd.read_csv('transaction.csv', sep=';')

data.info()





data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']


data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

data['Markup'] = round(data['Markup'],2)

data['date']= data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)

split_col = data['ClientKeywords'].str.split(',', expand=True)

data['ClientAge'] = split_col[0]

data['ClientAge'] = data['ClientAge'].str.replace('[','')


data['ClientType'] = split_col[1]

data['LengthofContract'] = split_col[2].str.replace(']','')


seasons =pd.read_csv('value_inc_seasons.csv', sep=';')

data = pd.merge(data,seasons,on = 'Month')


data = data.drop(['Day','Month','Year'], axis=1)

data.to_csv('ValueInc_Cleaned.csv', index = False)