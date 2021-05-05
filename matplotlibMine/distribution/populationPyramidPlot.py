# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pandas.read_csv("../dataset/email_campaign_funnel.csv")

# Draw Plot
plt.figure(figsize=(12, 8), dpi=80)
group_col = 'Gender'
order_of_bars = df.Stage.unique()[::-1]
colors = [
    plt.cm.Set1(i / float(len(df[group_col].unique()) - 1))
    for i in range(len(df[group_col].unique()))
]

for c, group in zip(colors, df[group_col].unique()):
    sns.barplot(
        x='Users',
        y='Stage',
        data=df.loc[df[group_col] == group, :],
        order=order_of_bars,
        color=c,
        label=group
    )

# Decorations
plt.xlabel("$Users$")
plt.ylabel("Stage of Purchase")
plt.yticks(fontsize=12)
plt.title("Population Pyramid of the Marketing Funnel", fontsize=18)
plt.legend()
plt.savefig("../photos/distribution/populationPyramidPlot.png")
plt.show()
