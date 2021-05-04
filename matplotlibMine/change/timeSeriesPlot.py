# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt

# Import Data
df = pandas.read_csv('../dataset/AirPassengers.csv')

# Draw Plot
plt.figure(figsize=(12, 8), dpi=80)
plt.plot(df['date'], df['value'], color='#dc2624')

# Decoration
plt.ylim(50, 750)
xtick_location = df.index.tolist()[::12]
xtick_labels = [x[-4:] for x in df.date.tolist()[::12]]
plt.xticks(ticks=xtick_location,
           labels=xtick_labels,
           rotation=0,
           fontsize=12,
           horizontalalignment='center',
           alpha=.7)
plt.yticks(fontsize=12, alpha=.7)
plt.title("Air Passengers Traffic (1949 - 1969)", fontsize=18)
plt.grid(axis='both', alpha=.3)

# Remove borders
plt.gca().spines["top"].set_alpha(0.0)
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.0)
plt.gca().spines["left"].set_alpha(0.3)
plt.savefig("../photos/change/timeSeriesPlot.png")
plt.show()
