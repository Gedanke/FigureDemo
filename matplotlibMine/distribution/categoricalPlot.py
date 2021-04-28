# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import joypy

# Load Dataset
titanic = sns.load_dataset("titanic")
# titanic = pandas.read_csv("../dataset/titanic.csv")
# Plot
g = sns.catplot(x="alive",
                col="deck",
                col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count",
                height=3.5,
                aspect=.8,
                palette='Set1')

plt.savefig("../photos/distribution/categoricalPlot1.png")
plt.show()
# Plot
sns.catplot(x="age",
            y="embark_town",
            hue="sex",
            col="class",
            data=titanic[titanic.embark_town.notnull()],
            orient="h",
            height=5,
            aspect=1,
            palette="Set1",
            kind="violin",
            dodge=True,
            cut=0,
            bw=.2)
plt.savefig("../photos/distribution/categoricalPlot2.png")
plt.show()
