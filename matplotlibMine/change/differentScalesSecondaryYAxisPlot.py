# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib.pyplot as plt

# Import Data
df = pandas.read_csv("../dataset/economics.csv")

x = df['date']
y1 = df['psavert']
y2 = df['unemploy']

# Plot Line1 (Left Y Axis)
fig, ax1 = plt.subplots(1, 1, figsize=(12, 6), dpi=100)
ax1.plot(x, y1, color='tab:red')

# Plot Line2 (Right Y Axis)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(x, y2, color='tab:blue')

# Decorations
# ax1 (left Y axis)
ax1.set_xlabel('Year', fontsize=18)
ax1.tick_params(axis='x', rotation=70, labelsize=12)
ax1.set_ylabel('Personal Savings Rate', color='#dc2624', fontsize=16)
ax1.tick_params(axis='y', rotation=0, labelcolor='#dc2624')
ax1.grid(alpha=.4)

# ax2 (right Y axis)
ax2.set_ylabel("# Unemployed (1000's)", color='#01a2d9', fontsize=16)
ax2.tick_params(axis='y', labelcolor='#01a2d9')
ax2.set_xticks(numpy.arange(0, len(x), 60))
ax2.set_xticklabels(x[::60], rotation=90, fontdict={'fontsize': 10})
ax2.set_title(
    "Personal Savings Rate vs Unemployed: Plotting in Secondary Y Axis",
    fontsize=18
)
fig.tight_layout()
plt.savefig("../photos/change/differentScalesSecondaryYAxisPlot.png")
plt.show()
