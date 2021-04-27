# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare Data
df = pandas.read_csv("../dataset/mtcars.csv")
# df['Species'] =
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean()) / x.std()
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)

# Draw plot
plt.figure(figsize=(10, 8), dpi=80)
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.8, linewidth=5)
for x, y, tex in zip(df.mpg_z, df.index, df.mpg_z):
    t = plt.text(x, y, round(tex, 2), horizontalalignment='right' if x < 0 else 'left',
                 verticalalignment='center', fontdict={'color': 'black' if x < 0 else 'black', 'size': 10})

# Decorations
plt.yticks(df.index, df.cars, fontsize=12)
plt.xticks(fontsize=10)
plt.title('Diverging Text Bars of Car Mileage', fontdict={'size': 15})
plt.grid(linestyle='--', alpha=0.5)
plt.xlim(-2.5, 2.5)
plt.savefig("../photos/deviation/divergingTextsHPlot.png")
plt.show()
# 垂直版感兴趣可以改改就可以了
