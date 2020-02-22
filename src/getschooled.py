# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:51:19 2020

@author: Hamez
"""

""" This file reads in the file,
    creates the distplot dataset,
    calculate mean proficiency and,
    regresses """

# imports
import pandas as pd
import numpy as np


# Read in Dataset
#filepath = r"C:\Users\Hamez\Desktop\HACKCITY\rawdata\qol-data\QOL Data Download July 2019.xls"

# CSV of the education tab with top row removed
filepath = r"C:\Users\Hamez\Desktop\HACKCITY\outdata\clt_edu.csv"

df = pd.read_csv(filepath)

# Filter to keep vars
keepvars = ['NPA',
            'Proficiency_Elementary_School_2017',
            'Proficiency_Elementary_School_2016',
            'Proficiency_Elementary_School_2015',
            'Proficiency_Elementary_School_2014',
            'Proficiency_Middle_School_2017',
            'Proficiency_Middle_School_2016',
            'Proficiency_Middle_School_2015',
            'Proficiency_Middle_School_2014',
            'Proficiency_High_School_2017',
            'Proficiency_High_School_2016',
            'Proficiency_High_School_2015',
            'Proficiency_High_School_2014']
df = df[keepvars]


yearlist = ['2014', '2015', '2016', '2017']
outlist = []

for year in yearlist:
    tempdf = df[['NPA',
                 f'Proficiency_Elementary_School_{year}',
                 f'Proficiency_Middle_School_{year}',
                 f'Proficiency_High_School_{year}']].copy(deep=True)
    
    tempdf.rename(columns={f'Proficiency_Elementary_School_{year}' : 'Proficiency_Elementary_School',
                           f'Proficiency_Middle_School_{year}' : 'Proficiency_Middle_School',
                           f'Proficiency_High_School_{year}' : 'Proficiency_High_School'},
                inplace=True)
    
    tempdf['Proficiency_Mean'] = tempdf.mean(axis=1, skipna=True)
    tempdf['year'] = year

    outlist.append(tempdf)

outdf = pd.concat(outlist)


# Save
outdf.to_csv(r"C:\Users\Hamez\Desktop\HACKCITY\outdata\SchoolProficiency.csv", index=False)





