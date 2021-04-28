# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare Data
df_raw = pandas.read_csv("../dataset/mpg_ggplot2.csv")
df = df_raw[['cty',
             'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
df.sort_values('cty', inplace=True)
df.reset_index(inplace=True)

# Draw plot
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 8), facecolor='white', dpi=80)
ax.vlines(x=df.index,
          ymin=0,
          ymax=df.cty,
          color='#dc2624',
          alpha=0.7,
          linewidth=20)

# Annotate Text
for i, cty in enumerate(df.cty):
    ax.text(i, cty + 0.5, round(cty, 1), horizontalalignment='center')

# Title, Label, Ticks and Ylim
ax.set_title('Bar Chart for Highway Mileage', fontdict={'size': 12})
plt.xticks(df.index,
           df.manufacturer.str.upper(),
           rotation=60,
           horizontalalignment='right',
           fontsize=10)
plt.yticks(fontsize=12)
plt.ylabel('Miles Per Gallon', fontsize=12)
plt.ylim = (0, 30)

# 添加底纹
p1 = patches.Rectangle((.57, -0.005),
                       width=.33,
                       height=.13,
                       alpha=.1,
                       facecolor='green',
                       transform=fig.transFigure)
p2 = patches.Rectangle((.124, -0.005),
                       width=.446,
                       height=.13,
                       alpha=.1,
                       facecolor='red',
                       transform=fig.transFigure)
fig.add_artist(p1)
fig.add_artist(p2)
plt.savefig("../photos/ranking/orderedBarChartPlot.png")
plt.show()
