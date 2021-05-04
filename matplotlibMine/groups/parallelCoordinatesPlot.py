# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Import Data
df_final = pandas.read_csv("../dataset/diamonds_filter.csv")

# Plot
plt.figure(figsize=(11, 7), dpi=80)
parallel_coordinates(df_final, 'cut', colormap='Set2_r')

# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(.3)

plt.title('Parallel Coordinated of Diamonds', fontsize=18)
plt.grid(alpha=0.3)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("../photos/groups/parallelCoordinatesPlot.png")
plt.show()
