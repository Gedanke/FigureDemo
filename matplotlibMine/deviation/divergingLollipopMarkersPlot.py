# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv("../dataset/mtcars.csv")

# Prepare Data
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean()) / x.std()
df['colors'] = 'black'

# color fiat differently
df.loc[df.cars == 'Fiat X1-9', 'colors'] = 'darkorange'
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)

# Draw plot
import matplotlib.patches as patches

plt.figure(figsize=(10, 12), dpi=80)
plt.hlines(y=df.index,
           xmin=0,
           xmax=df.mpg_z,
           color=df.colors,
           alpha=0.4,
           linewidth=1)
plt.scatter(df.mpg_z,
            df.index,
            color=df.colors,
            s=[600 if x == 'Fiat X1-9' else 300 for x in df.cars],
            alpha=0.6)
plt.yticks(df.index, df.cars)
plt.xticks(fontsize=12)

# Annotate
plt.annotate('Mercedes Models',
             xy=(0.0, 11.0),
             xytext=(1.0, 11),
             xycoords='data',
             fontsize=15,
             ha='center',
             va='center',
             bbox=dict(boxstyle='square', fc='firebrick'),
             arrowprops=dict(arrowstyle='-[, widthB=2.0, lengthB=1.5',
                             lw=2.0,
                             color='steelblue'),
             color='white')

# Add Patches
p1 = patches.Rectangle((-2.0, -1),
                       width=.3,
                       height=3,
                       alpha=.2,
                       facecolor='red')
p2 = patches.Rectangle((1.5, 27),
                       width=.8,
                       height=5,
                       alpha=.2,
                       facecolor='green')
plt.gca().add_patch(p1)
plt.gca().add_patch(p2)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Decorate
plt.title('Diverging Bars of Car Mileage', fontdict={'size': 15})
plt.grid(linestyle='--', alpha=0.5)
plt.savefig("../photos/deviation/divergingLollipopMarkersPlot.png")
plt.show()
