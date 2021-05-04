# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt

# Import Data
df = pandas.read_csv('../dataset/nightvisitors.csv')

# Decide Colors
mycolors = ['#dc2624', '#2b4750', '#45a0a2', '#e87a59', '#7dcaa9', '#649E7D', '#dc8018', '#C89F91']

# Draw Plot and Annotate
fig, ax = plt.subplots(1, 1, figsize=(12, 8), dpi=80)
columns = df.columns[1:]
labs = columns.values.tolist()

# Prepare data
x = df['yearmon'].values.tolist()
y0 = df[columns[0]].values.tolist()
y1 = df[columns[1]].values.tolist()
y2 = df[columns[2]].values.tolist()
y3 = df[columns[3]].values.tolist()
y4 = df[columns[4]].values.tolist()
y5 = df[columns[5]].values.tolist()
y6 = df[columns[6]].values.tolist()
y7 = df[columns[7]].values.tolist()
y = numpy.vstack([y0, y2, y4, y6, y7, y5, y1, y3])

# Plot for each column
labs = columns.values.tolist()
ax = plt.gca()
ax.stackplot(x, y, labels=labs, colors=mycolors, alpha=0.8)
ax.tick_params(axis='x', rotation=45, labelsize=12)
# Decorations
ax.set_title('Night Visitors in Australian Regions', fontsize=18)
ax.set(ylim=[0, 100000])
ax.legend(fontsize=10, ncol=4)
plt.xticks(x[::5], fontsize=10, horizontalalignment='center')
plt.yticks(numpy.arange(10000, 100000, 20000), fontsize=10)
plt.xlim(x[0], x[-1])

# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(.3)
plt.savefig("../photos/change/stackedAreaChartPlot.png")
plt.show()
