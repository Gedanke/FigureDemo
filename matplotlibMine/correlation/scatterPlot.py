# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib.pyplot as plt

# Import dataset
midwest = pandas.read_csv("../dataset/midwest_filter.csv")

# Prepare Data
# Create as many colors as there are unique midwest['category']
categories = numpy.unique(midwest['category'])
colors = [
    plt.cm.Set1(i / float(len(categories) - 1)) for i in range(len(categories))
]

# Draw Plot for Each Category
plt.figure(figsize=(10, 6), dpi=100, facecolor='w', edgecolor='k')

for i, category in enumerate(categories):
    plt.scatter(
        'area',
        'poptotal',
        data=midwest.loc[midwest.category == category, :],
        s=20,
        c=[colors[i]],
        label=str(category)
    )

# Decorations
plt.gca().set(
    xlim=(0.0, 0.1),
    ylim=(0, 90000),
)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Area', fontdict={'fontsize': 10})
plt.ylabel('Population', fontdict={'fontsize': 10})
plt.title("Scatterplot of Midwest Area vs Population", fontsize=12)
plt.legend(fontsize=10)
plt.savefig("../photos/correlation/scatterPlot.png")
plt.show()
