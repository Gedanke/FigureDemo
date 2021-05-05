# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
df = pandas.read_csv("../dataset/mpg_ggplot2.csv")

# Draw Plot
plt.figure(figsize=(13, 10), dpi=80)
sns.boxplot(
    x='class',
    y='hwy',
    data=df,
    hue='cyl',
    palette="Set1",
)
plt.legend(loc=9)
sns.stripplot(
    x='class',
    y='hwy',
    data=df,
    color='#dc2624',
    size=5,
    jitter=1
)

for i in range(len(df['class'].unique()) - 1):
    plt.vlines(
        i + .5, 10, 45, linestyles='solid', colors='gray', alpha=0.2
    )

# Decoration
plt.title('Box Plot of Highway Mileage by Vehicle Class', fontsize=18)
plt.savefig("../photos/distribution/dotBoxPlot.png")
plt.show()
