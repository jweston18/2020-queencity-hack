# Format economic data

import pandas as pd
import numpy as np

from itertools import compress


source = "../data/character.csv"
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


# Make lists
races = ["White", "Black", "Asian", "Hispanic", "All_Other"]
npalist = df.NPA.values.tolist()
years = []
race = []
values = []

npa = npalist.copy()

def charmelt(char):
    fdf = str_filter_col(df, char)

    for c in fdf.columns:
        cvals = df[c].values
        n = len(cvals)
        desc = column_desc(c)

        values.append(cvals)
        years.append(repeat(column_year(c), n))
        race.append(repeat(char, n))
        for v in npalist:
            npa.append(v)
    

for r in races:
    charmelt(r)

final = pd.DataFrame({
    "year": unpack(years),
    "npa": npa[:-462],
    "race": unpack(race),
    "values": unpack(values)
})