# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt

# Import Data
df = pandas.read_csv("../dataset/economics.csv")

# Prepare Data
x = df['date'].values.tolist()
y1 = df['psavert'].values.tolist()
y2 = df['uempmed'].values.tolist()
columns = ['psavert', 'uempmed']

# Draw Plot
fig, ax = plt.subplots(1, 1, figsize=(12, 6), dpi=80)
ax.fill_between(x,
                y1=y1,
                y2=0,
                label=columns[1],
                alpha=0.5,
                color='#dc2624',
                linewidth=2)
ax.fill_between(x,
                y1=y2,
                y2=0,
                label=columns[0],
                alpha=0.5,
                color='#649E7D',
                linewidth=2)

# Decorations
ax.set_title('Personal Savings Rate vs Median Duration of Unemployment',
             fontsize=18)
ax.set(ylim=[0, 30])
ax.legend(loc='best', fontsize=12)
plt.xticks(x[::50], fontsize=10, horizontalalignment='center')
plt.yticks(numpy.arange(2.5, 30.0, 2.5), fontsize=10)
plt.xlim(-10, x[-1])
plt.tick_params(axis='x', rotation=45, labelsize=12)

# Draw Tick lines
for y in numpy.arange(2.5, 30.0, 2.5):
    plt.hlines(y,
               xmin=0,
               xmax=len(x),
               colors='black',
               alpha=0.3,
               linestyles="--",
               lw=0.5)

# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(.3)
plt.savefig("../photos/change/areaChartUnStackedPlot.png")
plt.show()
