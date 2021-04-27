# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# 友情提示：当matplotlib>=3.2出现报错ValueError: s must be a scalar, or the same size as x and y时
# Import Data
df = pandas.read_csv("../dataset/mpg_ggplot2.csv")
df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')
# Draw Stripplot
fig, ax = plt.subplots(figsize=(10, 6), dpi=80)
sns.stripplot(df_counts.cty,
              df_counts.hwy,
              size=10,
              ax=ax,
              palette='Set1')

# Decorations
sns.set(style="whitegrid", font_scale=1.1)
plt.title('Counts Plot - Size of circle is bigger as more points overlap')
plt.savefig("../photos/correlation/countsPlot.png")
plt.show()
