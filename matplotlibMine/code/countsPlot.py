# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

d = pandas.read_csv("../dataset/mpg_ggplot2.csv")
# d = pandas.read_csv("https://github.com/selva86/datasets/blob/master/mpg_ggplot2.csv")
data = d.groupby(["hwy", "cty"]).size().reset_index(name="counts")
fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
sns.stripplot(x=d.cty, y=d.hwy, size=data.counts * 2, ax=ax)
plt.title('Counts Plot - Size of circle is bigger as more points overlap', fontsize=22)
plt.savefig("../photos/countsPlot.png")
plt.show()
