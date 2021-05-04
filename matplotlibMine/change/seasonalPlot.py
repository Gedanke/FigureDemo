# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
from dateutil.parser import parse

# Import Data
df = pandas.read_csv('../dataset/AirPassengers.csv')

# Prepare data
df['year'] = [parse(d).year for d in df.date]
df['month'] = [parse(d).strftime('%b') for d in df.date]
years = df['year'].unique()

# Draw Plot

mycolors = [
    '#dc2624', '#2b4750', '#45a0a2', '#e87a59', '#7dcaa9', '#649E7D',
    '#dc8018', '#C89F91', '#6c6d6c', '#4f6268', '#c7cccf', 'firebrick'
]
plt.figure(figsize=(10, 6), dpi=80)

for i, y in enumerate(years):
    plt.plot('month',
             'value',
             data=df.loc[df.year == y, :],
             color=mycolors[i],
             label=y)
    plt.text(df.loc[df.year == y, :].shape[0] - .9,
             df.loc[df.year == y, 'value'][-1:].values[0],
             y,
             fontsize=12,
             color=mycolors[i])

# Decoration
plt.ylim(50, 750)
plt.xlim(-0.3, 11)
plt.ylabel('$Air Traffic')
plt.yticks(fontsize=11, alpha=.7)
plt.xticks(fontsize=11, alpha=.7)
plt.title("Monthly Seasonal Plot: Air Passengers Traffic (1949 - 1969)",
          fontsize=16)
plt.grid(axis='y', alpha=.3)

# Remove borders
plt.gca().spines["top"].set_alpha(0.0)
plt.gca().spines["bottom"].set_alpha(0.5)
plt.gca().spines["right"].set_alpha(0.0)
plt.gca().spines["left"].set_alpha(0.5)
# plt.legend(loc='upper right', ncol=2, fontsize=12)
plt.savefig("../photos/change/seasonalPlot.png")
plt.show()
