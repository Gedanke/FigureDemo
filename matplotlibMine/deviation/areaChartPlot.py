# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib.pyplot as plt

# Prepare Data
df = pandas.read_csv("../dataset/economics.csv", parse_dates=['date']).head(100)
x = numpy.arange(df.shape[0])
y_returns = (df.psavert.diff().fillna(0) / df.psavert.shift(1)).fillna(0) * 100

# Plot使用plt.fill_between
plt.figure(figsize=(10, 8), dpi=80)
plt.fill_between(
    x[1:],
    y_returns[1:],
    0,
    where=y_returns[1:] >= 0,
    facecolor='green',
    interpolate=True,
    alpha=0.7
)
plt.fill_between(
    x[1:],
    y_returns[1:],
    0,
    where=y_returns[1:] <= 0,
    facecolor='red',
    interpolate=True,
    alpha=0.7
)

# Annotate
plt.annotate(
    'Peak \n1975',
    xy=(94.0, 21.0),
    xytext=(88.0, 28),
    bbox=dict(boxstyle='square', fc='firebrick'),
    arrowprops=dict(facecolor='steelblue', shrink=0.05),
    fontsize=12,
    color='white'
)

# Decorations
xtickvals = [
    str(m)[:3].upper() + "-" + str(y)
    for y, m in zip(df.date.dt.year, df.date.dt.month_name())
]
plt.gca().set_xticks(x[::6])
plt.gca().set_xticklabels(
    xtickvals[::6],
    rotation=90,
    fontdict={
        'horizontalalignment': 'center',
        'verticalalignment': 'center_baseline',
        'size': 12
    }
)
plt.ylim(-20, 32)
plt.xlim(1, 100)
plt.yticks(fontsize=12)
plt.title("Month Economics Return %", fontsize=12)
plt.ylabel('Monthly returns %', fontsize=12)
plt.grid(alpha=0.5)
plt.savefig("../photos/deviation/areaChartPlot.png")
plt.show()
