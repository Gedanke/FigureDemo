# -*- coding:utf-8 -*-

import numpy
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
df = pandas.read_csv("../dataset/mpg_ggplot2.csv")

# Draw Plot
plt.figure(figsize=(10, 8), dpi=80)
sns.distplot(df.loc[df['class'] == 'compact', "cty"],
             color="#01a2d9",
             label="Compact",
             hist_kws={'alpha': .7},
             kde_kws={'linewidth': 3})
sns.distplot(df.loc[df['class'] == 'suv', "cty"],
             color="#dc2624",
             label="SUV",
             hist_kws={'alpha': .7},
             kde_kws={'linewidth': 3})
sns.distplot(df.loc[df['class'] == 'minivan', "cty"],
             color="g",
             label="#C89F91",
             hist_kws={'alpha': .7},
             kde_kws={'linewidth': 3})
plt.ylim(0, 0.35)

# Decoration
sns.set(style="whitegrid", font_scale=1.1)
plt.title('Density Plot of City Mileage by Vehicle Type', fontsize=18)
plt.legend()
plt.savefig("../photos/distribution/densityCurvesHistogramPlot.png")
plt.show()
