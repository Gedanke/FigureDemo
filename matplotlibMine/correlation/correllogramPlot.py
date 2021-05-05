# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv("../dataset/mtcars.csv")
plt.figure(figsize=(12, 10), dpi=80)
sns.heatmap(
    df.corr(),
    xticklabels=df.corr().columns,
    yticklabels=df.corr().columns,
    cmap='Set1',
    center=0,
    annot=True,
    annot_kws={
        'size': 12,
        'weight': 'normal',
        'color': '#253D24'
    },
)

plt.savefig("../photos/correlation/correllogramPlot.png")
plt.show()
