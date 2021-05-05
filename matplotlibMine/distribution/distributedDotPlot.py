# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt

# Prepare Data
df_raw = pandas.read_csv("../dataset/mpg_ggplot2.csv")
cyl_colors = {
    4: 'tab:red', 5: 'tab:green', 6: 'tab:blue', 8: 'tab:orange'
}
df_raw['cyl_color'] = df_raw.cyl.map(cyl_colors)

# Mean and Median city mileage by make
df = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
df.sort_values('cty', ascending=False, inplace=True)
df.reset_index(inplace=True)
df_median = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.median())

# Draw horizontal lines
fig, ax = plt.subplots(figsize=(11, 7), dpi=80)
ax.hlines(
    y=df.index,
    xmin=0,
    xmax=40,
    color='#01a2d9',
    alpha=0.5,
    linewidth=.5,
    linestyles='dashdot'
)

# Draw the Dots
for i, make in enumerate(df.manufacturer):
    df_make = df_raw.loc[df_raw.manufacturer == make, :]
    ax.scatter(
        y=[i] * df_make.shape[0],
        x='cty',
        data=df_make,
        s=75,
        edgecolors='#01a2d9',
        c='w',
        alpha=0.5
    )
    ax.scatter(
        y=i,
        x='cty',
        data=df_median.loc[df_median.index == make, :],
        s=75,
        c='#dc2624'
    )

# Annotate
ax.text(
    33,
    13,
    "$red \; dots \; are \; the \: median$",
    fontdict={'size': 12},
    color='#dc2624'
)

# Decorations
red_patch = plt.plot(
    [], [],
    marker="o",
    ms=10,
    ls="",
    mec=None,
    color='#dc2624',
    label="Median"
)
plt.legend(handles=red_patch)
ax.set_title('Distribution of City Mileage by Make', fontdict={'size': 18})
ax.set_xlabel('Miles Per Gallon (City)')
ax.set_yticks(df.index)
ax.set_yticklabels(df.manufacturer.str.title(), fontdict={'horizontalalignment': 'right'})
ax.set_xlim(1, 40)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_visible(False)
plt.grid(axis='both', alpha=.4, linewidth=.1)
plt.savefig("../photos/distribution/distributedDotPlot.png")
plt.show()
