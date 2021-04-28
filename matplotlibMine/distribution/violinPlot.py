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
plt.figure(figsize=(13, 10), dpi=80)
sns.violinplot(x='class',
               y='hwy',
               data=df,
               scale='width',
               palette='Set1',
               inner='quartile')

# Decoration
plt.title('Violin Plot of Highway Mileage by Vehicle Class', fontsize=18)
plt.savefig("../photos/distribution/violinPlot.png")
plt.show()
