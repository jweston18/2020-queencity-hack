# Format economic data

import pandas as pd
import numpy as np

from itertools import compress


source = "../data/housing.csv"
df = pd.read_csv(source)

def unpack(x):
    return [item for sublist in x for item in sublist]

def column_year(x):
    return int(x[-4:])

def column_desc(x):
    return x[:-5]

def str_filter_col(df, key):
    c = df.columns.tolist()
    cbools = [x.startswith(key) for x in c]
    cols = list(compress(c, cbools))

    return df[cols]

def repeat(x, n):
    return [x for _ in range(n)]

cvals = []
year = []
npa = []
npalist = df.NPA.tolist()

fdf = str_filter_col(df, "Rental_Houses_2")
for c in fdf.columns:
    n = len(df[c])
    cvals.append(df[c].values)
    year.append(repeat(column_year(c), n))
    for v in npalist:
        npa.append(v)

# npa = npa[:-len(df)]
year = unpack(year)
cvals = unpack(cvals)

final = pd.DataFrame({
    "npa": npa,
    "year": year,
    "percentRented": cvals,
})

final.to_csv("rental.csv", index=False)