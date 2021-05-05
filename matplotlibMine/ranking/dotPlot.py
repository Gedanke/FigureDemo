# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt

# Prepare Data
df_raw = pandas.read_csv("../dataset/mpg_ggplot2.csv")
df = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
df.sort_values('cty', inplace=True)
df.reset_index(inplace=True)

# Draw plot
fig, ax = plt.subplots(figsize=(10, 8), dpi=80)
ax.hlines(
    y=df.index,
    xmin=11,
    xmax=26,
    color='gray',
    alpha=0.7,
    linewidth=1,
    linestyles='dashdot'
)
ax.scatter(
    y=df.index, x=df.cty, s=75, color='#dc2624', alpha=0.7
)

# Title, Label, Ticks and Ylim
ax.set_title('Dot Plot for Highway Mileage', fontdict={'size': 12})

plt.xlabel('Miles Per Gallon', fontsize=12)

ax.set_yticks(df.index)
ax.set_yticklabels(
    df.manufacturer.str.title(),
    fontdict={
        'horizontalalignment': 'right',
        'fontsize': 12
    }
)

plt.xticks(fontsize=12)
ax.set_xlim(10, 27)
plt.savefig("../photos/ranking/dotPlot.png")
plt.show()
