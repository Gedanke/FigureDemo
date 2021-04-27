# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare Data
df = pandas.read_csv("../dataset/mtcars.csv")
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean()) / x.std()
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)

# Draw plot
plt.figure(figsize=(10, 6), dpi=80)
plt.vlines(x=df.index,
           ymin=0,
           ymax=df.mpg_z,
           color=df.colors,
           alpha=0.8,
           linewidth=5)
for y, x, tex in zip(df.mpg_z, df.index, df.mpg_z):
    t = plt.text(x,
                 y + 0.2,
                 round(tex, 1),
                 horizontalalignment='center',
                 fontdict={
                     'color': 'black' if x < 0 else 'black',
                     'size': 8
                 })

# Decorations
plt.xticks(df.index, df.cars, fontsize=12, rotation=90)
plt.yticks(fontsize=12)
plt.title('Diverging Text Bars of Car Mileage', fontdict={'size': 12})
plt.grid(linestyle='--', alpha=0.5)
plt.savefig("../photos/deviation/divergingTextsVPlot.png")
plt.show()
