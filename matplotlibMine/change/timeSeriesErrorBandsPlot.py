# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
from scipy.stats import sem

# Import Data
df_raw = pandas.read_csv('../dataset/orders_45d.csv', parse_dates=['purchase_time', 'purchase_date'])

# Prepare Data: Daily Mean and SE Bands
df_mean = df_raw.groupby('purchase_date').quantity.mean()
df_se = df_raw.groupby('purchase_date').quantity.apply(sem).mul(1.96)

# Plot
plt.figure(figsize=(10, 6), dpi=80)
plt.ylabel("# Daily Orders", fontsize=12)
x = [
    d.date().strftime('%Y-%m-%d') for d in df_mean.index
]
plt.plot(x, df_mean, color="#c72e29", lw=2)
plt.fill_between(
    x, df_mean - df_se, df_mean + df_se, color="#f8f2e4"
)

# Decorations
# Lighten borders
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(1)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(1)
plt.xticks(x[::6], [str(d) for d in x[::6]], fontsize=12)
plt.title(
    "Daily Order Quantity of Brazilian Retail with Error Bands (95% confidence)",
    fontsize=14
)

# Axis limits
s, e = plt.gca().get_xlim()
plt.xlim(s, e - 2)
plt.ylim(4, 10)

# Draw Horizontal Tick lines
for y in range(5, 10, 1):
    plt.hlines(
        y,
        xmin=s,
        xmax=e,
        colors='black',
        alpha=0.5,
        linestyles="--",
        lw=0.5
    )

plt.savefig("../photos/change/timeSeriesErrorBandsPlot.png")
plt.show()
