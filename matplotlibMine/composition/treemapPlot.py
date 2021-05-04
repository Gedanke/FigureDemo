# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib.pyplot as plt
import squarify

# Import Data
df_raw = pandas.read_csv("../dataset/mpg_ggplot2.csv")

# Prepare Data
df = df_raw.groupby('class').size().reset_index(name='counts')
labels = df.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
sizes = df['counts'].values.tolist()
colors = [plt.cm.Set2(i / float(len(labels))) for i in range(len(labels))]

# Draw Plot
plt.figure(figsize=(10, 8), dpi=100)
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)

# Decorate
plt.title('Treemap of Vechile Class')
plt.axis('off')
plt.savefig("../photos/composition/treemapPlot.png")
plt.show()
