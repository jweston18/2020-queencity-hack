# Format economic data

import pandas as pd
import numpy as np

source = "../data/economy.csv"

df = pd.read_csv(source)

def unpack(x):
    return [item for sublist in x for item in sublist]

def repeat(x, n):
    return [x for _ in range(n)]

# jdense = [df[f"m75_200{x}"].values for x in range(4,10)] + [df[f"m75_20{x}"].values for x in range(10,16)]
# jdense = [item for sublist in jdense for item in sublist]

years = [2002+x for x in range(13)]
# years = years * len(df)

npalist = df.NPA.tolist()
npa = []
npa.append(repeat(npalist, 13))

cvals, cyears = [], []
for y in years:
    vals = df[f"m75_{y}"].values
    
    cvals.append(vals)
    cyears.append([y for _ in range(len(vals))])


# Unpack 
cvals = unpack(cvals)
cyears = unpack(cyears)
npa = unpack(unpack(npa))

# merge
f = pd.DataFrame({
    "npa": npa,
    "jobDensity": cvals,
    "year": cyears
})

f.to_csv("jobdense.csv", index=False)