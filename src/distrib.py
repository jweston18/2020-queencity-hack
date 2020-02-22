import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Globals
plt.style.use("ggplot")

# Read Data
df = pd.read_csv("../data/economy.csv")

_, ax = plt.subplots(figsize=(32,18))

sns.distplot(df.m37_2017, ax=ax)
plt.show()

