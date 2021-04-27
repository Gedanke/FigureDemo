# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns


def show1():
    """

    :return:
    """
    df = pandas.read_csv("../dataset/iris_test.csv")

    # Plot

    sns.pairplot(df)
    plt.savefig("../photos/correlation/pairwisePlot1.png")
    plt.show()


def show2():
    """

    :return:
    """
    df = sns.load_dataset('iris')

    # Plot
    plt.figure(figsize=(10, 8), dpi=80)
    sns.pairplot(df,
                 kind="scatter",
                 hue="species",
                 palette='Set1',
                 plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
    plt.savefig("../photos/correlation/pairwisePlot2.png")
    plt.show()


if __name__ == '__main__':
    """"""
    # show1()
    # show2()
