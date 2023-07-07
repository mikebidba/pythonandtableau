# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 12:09:03 2022

@author: Michael Romero
"""
#Import Transaction CSV data
import pandas as pd
data =pd.read_csv('transaction.csv', sep=';')

#Verify loaded data
data.info()

#Create Data Frames

#Cost Per Transaction
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales Per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Per Transaction
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup Profit vs Cost
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

data['Markup'] = round(data['Markup'],2)

#Build Date column
data['date']= data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)

#Seperate keywords
split_col = data['ClientKeywords'].str.split(',', expand=True)

data['ClientAge'] = split_col[0]

data['ClientAge'] = data['ClientAge'].str.replace('[','')


data['ClientType'] = split_col[1]

data['LengthofContract'] = split_col[2].str.replace(']','')

#Load Season data 
seasons =pd.read_csv('value_inc_seasons.csv', sep=';')

#Merge data sets
data = pd.merge(data,seasons,on = 'Month')


data = data.drop(['Day','Month','Year'], axis=1)

#Create output CSV file for dashboard
data.to_csv('ValueInc_Cleaned.csv', index = False)
