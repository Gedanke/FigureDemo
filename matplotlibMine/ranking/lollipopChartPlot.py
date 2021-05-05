# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt

# 棒棒糖图(Lollipop Chart)
# Prepare Data
df_raw = pandas.read_csv("../dataset/mpg_ggplot2.csv")
df = df_raw[['cty',
             'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
df.sort_values('cty', inplace=True)
df.reset_index(inplace=True)

# Draw plot
fig, ax = plt.subplots(figsize=(10, 8), dpi=80)
ax.vlines(
    x=df.index,
    ymin=0,
    ymax=df.cty,
    color='#dc2624',
    alpha=0.7,
    linewidth=4
)
ax.scatter(
    x=df.index, y=df.cty, s=85, color='#dc2624', alpha=0.7
)

# Title, Label, Ticks and Ylim
ax.set_title('Lollipop Chart for Highway Mileage', fontdict={'size': 12})

plt.ylabel('Miles Per Gallon', fontsize=12)
ax.set_xticks(df.index)
ax.set_xticklabels(
    df.manufacturer.str.upper(),
    rotation=60,
    fontdict={
        'horizontalalignment': 'right',
        'size': 11
    }
)
ax.set_ylim(0, 30)
plt.yticks(fontsize=12)

# Annotate
for row in df.itertuples():
    ax.text(
        row.Index,
        row.cty + .5,
        s=round(row.cty, 2),
        horizontalalignment='center',
        verticalalignment='bottom',
        fontsize=12
    )

plt.savefig("../photos/ranking/lollipopChartPlot.png")
plt.show()
