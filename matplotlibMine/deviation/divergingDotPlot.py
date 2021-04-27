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
df['colors'] = ['red' if x < 0 else 'darkgreen' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)

# Draw plot
plt.figure(figsize=(12, 10), dpi=80)
plt.scatter(df.mpg_z, df.index, s=250, alpha=.6, color=df.colors)
for x, y, tex in zip(df.mpg_z, df.index, df.mpg_z):
    t = plt.text(x,
                 y,
                 round(tex, 1),
                 horizontalalignment='center',
                 verticalalignment='center',
                 fontdict={'color': 'black', 'size': '10'})

# Decorations
# Lighten borders
plt.gca().spines["top"].set_alpha(.3)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(.3)
plt.gca().spines["left"].set_alpha(.3)

plt.yticks(df.index, df.cars, fontsize=10)
plt.xticks(fontsize=10)
plt.title('Diverging Dotplot of Car Mileage', fontdict={'size': 15})
plt.xlabel('$Mileage,fontsize=10')
plt.grid(linestyle='--', alpha=0.5)
plt.xlim(-2.5, 2.5)
plt.savefig("../photos/deviation/divergingDotPlot.png")
plt.show()
