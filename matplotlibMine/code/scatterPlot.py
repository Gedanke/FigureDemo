# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("dataset/midwest_filter.csv")
categories = numpy.unique(data["category"])
num = len(categories)
colors = [
    plt.cm.tab10(i / float(num - 1)) for i in range(num)
]
plt.figure(figsize=(16, 10), dpi=100, facecolor='w', edgecolor='k')
for i, category in enumerate(categories):
    plt.scatter(
        "area", "poptotal", data=data.loc[data.category == category, :],
        s=20, c=[colors[i]], label=str(category)
    )

plt.gca().set(
    xlim=(0.0, 0.1), ylim=(0, 90000),
    xlabel="Area", ylabel="Population"
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
plt.legend(fontsize=12)
plt.savefig("photos/scatterPlot.png")
plt.show()
