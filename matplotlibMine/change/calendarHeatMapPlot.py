# -*- coding:utf-8 -*-

import pandas
import calmap
import matplotlib.pyplot as plt

df = pandas.read_csv("../dataset/yahoo.csv", parse_dates=['date'])
df.set_index('date', inplace=True)
# Plot
plt.figure(figsize=(16, 10), dpi=80)
calmap.calendarplot(
    df.loc['2014']['VIX.Close'],
    fig_kws={'figsize': (16, 10)},
    yearlabel_kws={
        'color': 'black',
        'fontsize': 14
    },
    subplot_kws={
        'title': 'Yahoo Stock Prices'
    }
)
plt.savefig("../photos/change/calendarHeatMapPlot.png")
plt.show()
