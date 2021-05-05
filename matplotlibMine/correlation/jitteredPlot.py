# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

data = pandas.read_csv("../dataset/mpg_ggplot2.csv")

fig, ax = plt.subplots(figsize=(16, 10), dpi=100)
sns.stripplot(
    x=data.cty, y=data.hwy, jitter=0.25, size=8, ax=ax, linewidth=.5
)

plt.title('Use jittered plots to avoid overlapping of points', fontsize=22)
plt.savefig("../photos/correlation/jitteredPlot.png")
plt.show()
