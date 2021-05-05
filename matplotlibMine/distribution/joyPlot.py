# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import joypy

# Import Data
mpg = pandas.read_csv("../dataset/mpg_ggplot2.csv")

# Draw Plot
plt.figure(figsize=(10, 6), dpi=80)
fig, axes = joypy.joyplot(
    mpg,
    column=['hwy', 'cty'],
    by="class",
    ylim='own',
    colormap=plt.cm.Set1,
    figsize=(10, 6)
)

# Decoration
plt.title('Joy Plot of City and Highway Mileage by Class', fontsize=18)
plt.savefig("../photos/distribution/joyPlot.png")
plt.show()
