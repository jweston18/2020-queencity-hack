# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 23:18:13 2020

@author: Hamez
"""

""" This file reads in the data and produces correlation values and plots

    1. Correlation of vars over time."""


# imports
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

from matplotlib import pyplot as plt
plt.style.use('ggplot')


# get data
filepath = r"C:\Users\Hamez\Desktop\HACKCITY\outdata\SchoolProficiency.csv"
df = pd.read_csv(filepath)


# step 1 - find correlations over time between two vars    
def corr_by_year(indf, var1, var2):
    
    # Get list of years
    yearlist = indf['year'].unique().tolist()
    print(yearlist)
    corrlist = []

    # Calculat corr by year
    for year in yearlist:
        yeardf = indf[indf['year'] == year]
        
        corrvalue = yeardf[[var1, var2]].corr()
        corrvalue = corrvalue.iloc[0,1]

        corrlist.append(corrvalue)
        
        print(year)
        print(corrvalue)
    
    # Save data
    outdf = pd.DataFrame({
                'year':yearlist,
                'corr':corrlist})
    
    
    # Make plot
    fig, ax = plt.subplots(figsize=(10,5))
    sns.lineplot([str(x) for x in outdf['year']], outdf['corr'])
    plt.ylabel('Correlation')
    plt.xlabel('Year')
    plt.title(f'Correlation between "{var1}" and "{var2}"')
    
    ts = '{date:%Y%m%d_%H%M_%S}'.format( date=datetime.datetime.now() )

    plt.savefig( r'''C:\Users\Hamez\Desktop\HACKCITY\plots\{}.png'''.format(tsd))
    plt.show()
    
    return outdf
    

# Calculat and cycle through the variables
plottcorr = corr_by_year(df, 'Proficiency_Elementary_School', 'Proficiency_High_School')



    