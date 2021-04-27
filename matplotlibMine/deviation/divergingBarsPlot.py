# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv("../dataset/mtcars.csv")
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean()) / x.std()
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)

# Draw plot
plt.figure(figsize=(10, 6), dpi=80)
plt.hlines(y=df.index,
           xmin=0,
           xmax=df.mpg_z,
           color=df.colors,
           alpha=0.8,
           linewidth=5)

# Decorations
plt.gca().set(ylabel='$Model', xlabel='$Mileage')
plt.yticks(df.index, df.cars, fontsize=12)
plt.xticks(fontsize=12)
plt.title('Diverging Bars of Car Mileage')
plt.grid(linestyle='--', alpha=0.5)
plt.savefig("../photos/deviation/deviationBarsPlot.png")
plt.show()
