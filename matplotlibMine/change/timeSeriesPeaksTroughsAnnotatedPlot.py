# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt

# Import Data
df = pandas.read_csv('../dataset/AirPassengers.csv')

# Get the Peaks and Troughs
data = df['value'].values
doublediff = numpy.diff(numpy.sign(numpy.diff(data)))
peak_locations = numpy.where(doublediff == -2)[0] + 1

doublediff2 = numpy.diff(numpy.sign(numpy.diff(-1 * data)))
trough_locations = numpy.where(doublediff2 == -2)[0] + 1

# Draw Plot
plt.figure(figsize=(12, 8), dpi=80)
plt.plot('date', 'value', data=df, color='tab:blue', label='Air Traffic')
plt.scatter(df.date[peak_locations],
            df.value[peak_locations],
            marker=mpl.markers.CARETUPBASE,
            color='tab:green',
            s=100,
            label='Peaks')
plt.scatter(df.date[trough_locations],
            df.value[trough_locations],
            marker=mpl.markers.CARETDOWNBASE,
            color='tab:red',
            s=100,
            label='Troughs')

# Annotate
for t, p in zip(trough_locations[1::5], peak_locations[::3]):
    plt.text(df.date[p],
             df.value[p] + 15,
             df.date[p],
             horizontalalignment='center',
             color='darkgreen')
    plt.text(df.date[t],
             df.value[t] - 35,
             df.date[t],
             horizontalalignment='center',
             color='darkred')

# Decoration
plt.ylim(50, 750)
xtick_location = df.index.tolist()[::6]
xtick_labels = df.date.tolist()[::6]
plt.xticks(ticks=xtick_location,
           labels=xtick_labels,
           rotation=45,
           fontsize=12,
           alpha=.7)
plt.title("Peak and Troughs of Air Passengers Traffic (1949 - 1969)",
          fontsize=18)
plt.yticks(fontsize=12, alpha=.7)

# Lighten borders
plt.gca().spines["top"].set_alpha(.0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(.0)
plt.gca().spines["left"].set_alpha(.3)

plt.legend(loc='upper left')
plt.grid(axis='y', alpha=.3)
plt.savefig("../photos/change/timeSeriesPeaksTroughsAnnotatedPlot.png")
plt.show()
