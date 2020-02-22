import pandas as pd

from pathlib import Path

parent = Path("../data/")
glob = ["rental", "jobdense", "racepop", "SchoolProficiency"]
fpaths = [parent.joinpath(f"{x}.csv") for x in glob]

data = {x: pd.read_csv(y) for x,y in zip(glob, fpaths)}

comb = data["racepop"].merge(data["rental"], on=["npa", "year"])
comb = comb.merge(data["SchoolProficiency"], on=["npa", "year"])


comb.to_csv("bigtable.csv", index=False)