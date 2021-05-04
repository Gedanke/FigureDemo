# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas.plotting import andrews_curves

# Import
df = pandas.read_csv("../dataset/mtcars.csv")
df.drop(['cars', 'carname'], axis=1, inplace=True)

# Plot
plt.figure(figsize=(10, 6), dpi=80)
andrews_curves(df, 'cyl', colormap='Set2_r')

# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(.3)

plt.title('Andrews Curves of mtcars', fontsize=18)
plt.xlim(-3, 3)
plt.grid(alpha=0.3)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("../photos/groups/andrewsCurvePlot.png")
plt.show()
