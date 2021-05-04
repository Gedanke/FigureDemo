# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib.pyplot as plt

# Import
df_raw = pandas.read_csv("../dataset/mpg_ggplot2.csv")
plt.figure(dpi=140)
# Prepare Data
df = df_raw.groupby('class').size()

# Make the plot with pandas
df.plot(kind='pie', subplots=True, figsize=(10, 10))
plt.title("Pie Chart of Vehicle Class - Bad")
plt.ylabel("")
plt.savefig("../photos/composition/pieChartPlot1.png")
plt.show()
# Import
df_raw = pandas.read_csv("../dataset/mpg_ggplot2.csv")

# Prepare Data
df = df_raw.groupby('class').size().reset_index(name='counts')

# Draw Plot
fig, ax = plt.subplots(figsize=(12, 7),
                       subplot_kw=dict(aspect="equal"),
                       dpi=80)

data = df['counts']
categories = df['class']
explode = [0, 0, 0, 0, 0, 0.1, 0]


def func(pct, allvals):
    absolute = int(pct / 100. * numpy.sum(allvals))
    return "{:.1f}% ({:d} )".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data,
                                  autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"),
                                  colors=plt.cm.Paired.colors,
                                  startangle=140,
                                  explode=explode)

# Decoration
ax.legend(wedges,
          categories,
          title="Vehicle Class",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=10, weight=700)
ax.set_title("Class of Vehicles: Pie Chart")
plt.savefig("../photos/composition/pieChartPlot2.png")
plt.show()
