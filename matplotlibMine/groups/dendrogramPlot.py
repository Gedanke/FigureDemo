# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc

# Import Data
df = pandas.read_csv('../dataset/USArrests.csv')

# Plot
plt.figure(figsize=(12, 8), dpi=80)
plt.title("USArrests Dendograms", fontsize=18)
dend = shc.dendrogram(shc.linkage(df[['Murder', 'Assault', 'UrbanPop',
                                      'Rape']],
                                  method='ward'),
                      labels=df.State.values,
                      color_threshold=200)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("../photos/groups/dendrogramPlot.png")
plt.show()
