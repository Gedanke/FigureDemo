# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import joypy

# Import Data
df = pandas.read_csv("../dataset/mpg_ggplot2.csv")

# Draw Plot
plt.figure(figsize=(10, 6), dpi=80)
sns.boxplot(
    x='class',
    y='hwy',
    data=df,
    notch=False,
    palette="Set1",
)


# Add N Obs inside boxplot (optional)
def add_n_obs(df, group_col, y):
    medians_dict = {
        grp[0]: grp[1][y].median()
        for grp in df.groupby(group_col)
    }
    xticklabels = [x.get_text() for x in plt.gca().get_xticklabels()]
    n_obs = df.groupby(group_col)[y].size().values
    for (x, xticklabel), n_ob in zip(enumerate(xticklabels), n_obs):
        plt.text(x,
                 medians_dict[xticklabel] * 1.01,
                 "#obs : " + str(n_ob),
                 horizontalalignment='center',
                 fontdict={'size': 12},
                 color='black')


add_n_obs(df, group_col='class', y='hwy')

# Decoration
sns.set(style="whitegrid", font_scale=1.1)
plt.title('Box Plot of Highway Mileage by Vehicle Class', fontsize=16)
plt.ylim(10, 40)
plt.savefig("../photos/distribution/boxPlot.png")
plt.show()
