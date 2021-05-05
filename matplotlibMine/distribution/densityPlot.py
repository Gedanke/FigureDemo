# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
df = pandas.read_csv("../dataset/mpg_ggplot2.csv")

# Draw Plot
plt.figure(figsize=(10, 8), dpi=80)
sns.kdeplot(
    df.loc[df['cyl'] == 4, "cty"],
    shade=True,
    color="#01a2d9",
    label="Cyl=4",
    alpha=.7
)
sns.kdeplot(
    df.loc[df['cyl'] == 5, "cty"],
    shade=True,
    color="#dc2624",
    label="Cyl=5",
    alpha=.7
)
sns.kdeplot(
    df.loc[df['cyl'] == 6, "cty"],
    shade=True,
    color="#C89F91",
    label="Cyl=6",
    alpha=.7
)
sns.kdeplot(
    df.loc[df['cyl'] == 8, "cty"],
    shade=True,
    color="#649E7D",
    label="Cyl=8",
    alpha=.7
)

# Decoration
sns.set(style="whitegrid", font_scale=1.1)
plt.title('Density Plot of City Mileage by n_Cylinders', fontsize=18)
plt.legend()
plt.savefig("../photos/distribution/densityPlot.png")
plt.show()
