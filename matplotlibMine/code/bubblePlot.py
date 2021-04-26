# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

data = pandas.read_csv("../dataset/midwest_filter.csv")
categories = numpy.unique(data["category"])
num = len(categories)
colors = [
    plt.cm.tab10(i / float(num - 1)) for i in range(num)
]
fig = plt.figure(figsize=(16, 10), dpi=100, facecolor='w', edgecolor='k')
for i, category in enumerate(categories):
    plt.scatter(
        "area", "poptotal", data=data.loc[data.category == category, :],
        s='dot_size', c=[colors[i]], label=str(category),
        edgecolors="black", linewidths=0.5
    )


def encircle(x, y, ax=None, **kwargs):
    """

    :param x:
    :param y:
    :param ax:
    :param kwargs:
    :return:
    """
    if not ax:
        ax = plt.gca()
    p = numpy.c_[x, y]
    hull = ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices, :], **kwargs)
    ax.add_patch(poly)


data_encircle = data.loc[data.state == "IN", :]

encircle(data_encircle.area, data_encircle.poptotal, ec="k", fc="gold", alpha=0.1)
encircle(data_encircle.area, data_encircle.poptotal, ec="firebrick", fc="none", alpha=1.5)
plt.gca().set(
    xlim=(0.0, 0.1), ylim=(0, 90000),
    xlabel="Area", ylabel="Population"
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("Bubble Plot with Encircling", fontsize=22)
plt.legend(fontsize=12)
plt.savefig("../photos/bubblePlot.png")
plt.show()
