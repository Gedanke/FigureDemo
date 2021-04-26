# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

d = pandas.read_csv("../dataset/mpg_ggplot2.csv")
data = d.loc[d.cyl.isin([4, 8]), :]


def photo1():
    """

    :return:
    """
    sns.set_style("white")
    grid = sns.lmplot(
        x="displ", y="hwy", hue="cyl", data=data,
        height=7, aspect=1.6, robust=True, palette='tab10',
        scatter_kws=dict(
            s=60, linewidths=.7, edgecolors='black'
        )
    )

    grid.set(xlim=(0.5, 7.5), ylim=(0, 50))
    plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=20)
    plt.savefig("../photos/ScatterLinePlot1.png")
    plt.show()


def photo2():
    """

    :return:
    """
    sns.set_style("white")
    grid = sns.lmplot(
        x="displ", y="hwy", data=data,
        height=7, robust=True, palette='Set1',
        col="cyl", scatter_kws=dict(
            s=60, linewidths=.7, edgecolors='black'
        )
    )

    grid.set(xlim=(0.5, 7.5), ylim=(0, 50))
    plt.savefig("../photos/ScatterLinePlot2.png")
    plt.show()


if __name__ == '__main__':
    """"""
    photo1()
    photo2()
