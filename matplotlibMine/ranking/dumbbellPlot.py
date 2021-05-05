# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# Import Data
df = pandas.read_csv("../dataset/health.csv")
df.sort_values('pct_2014', inplace=True)
df.reset_index(inplace=True)


# Func to draw line segment
def newline(p1, p2, color='black'):
    ax = plt.gca()
    l = mlines.Line2D([p1[0], p2[0]], [p1[1], p2[1]], color='#d5695d')
    ax.add_line(l)
    return l


# Figure and Axes
fig, ax = plt.subplots(
    1, 1, figsize=(10, 8), facecolor='#f8f2e4', dpi=80
)

# Vertical Lines
ax.vlines(
    x=.05,
    ymin=0,
    ymax=26,
    color='black',
    alpha=1,
    linewidth=1,
    linestyles='dotted'
)
ax.vlines(
    x=.10,
    ymin=0,
    ymax=26,
    color='black',
    alpha=1,
    linewidth=1,
    linestyles='dotted'
)
ax.vlines(
    x=.15,
    ymin=0,
    ymax=26,
    color='black',
    alpha=1,
    linewidth=1,
    linestyles='dotted'
)
ax.vlines(
    x=.20,
    ymin=0,
    ymax=26,
    color='black',
    alpha=1,
    linewidth=1,
    linestyles='dotted'
)

# Points
ax.scatter(y=df['index'], x=df['pct_2013'], s=50, color='#dc2624')
ax.scatter(y=df['index'], x=df['pct_2014'], s=50, color='#e87a59')

# Line Segments
for i, p1, p2 in zip(df['index'], df['pct_2013'], df['pct_2014']):
    newline([p1, i], [p2, i])

# Decoration
ax.set_facecolor('#f8f2e4')
ax.set_title("Dumbell Chart: Pct Change - 2013 vs 2014", fontdict={'size': 18})
ax.set(xlim=(0, .25), ylim=(-1, 27), ylabel='Mean GDP Per Capita')
plt.ylabel('Mean GDP Per Capita', fontsize=15)
plt.yticks(fontsize=15)
ax.set_xticks([.05, .1, .15, .20])
ax.set_xticklabels(['5%', '15%', '20%', '25%'], fontdict={'size': 15})
plt.savefig("../photos/ranking/dumbbellPlot.png")
plt.show()
