# -*- coding: utf-8 -*-
"""
Created on Sun May  1 11:58:02 2022

@author: Michael
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

json_file = open('loan_data_json.json')
data = json.load(json_file)

with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

loandata = pd.DataFrame(data)

loandata['purpose'].unique()

loandata.describe()

loandata['dti'].describe()

income = np.exp(loandata['log.annual.inc'])

loandata['annualincome'] = income

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Error - Unknown'
    ficocat.append(cat)    
        
ficocat = pd.Series(ficocat)   


loandata['fico.category'] = ficocat


loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'   
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'   


catplot = loandata.groupby(['fico.category']).size()

purposecount = loandata.groupby(['purpose']).size()

catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecount.plot.bar(color = 'red', width = 0.1)
plt.show()


ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'green')
plt.show


loandata.to_csv('loan_cleaned.csv', index = True)