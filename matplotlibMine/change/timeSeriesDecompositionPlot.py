# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse

# Import Data
df = pandas.read_csv('../dataset/AirPassengers.csv')
dates = pandas.DatetimeIndex([parse(d).strftime('%Y-%m-01') for d in df['date']])
df.set_index(dates, inplace=True)

# Decompose
result = seasonal_decompose(df['value'], model='multiplicative')

# Plot
plt.figure(figsize=(12, 7), dpi=80)
# plt.rcParams.update({'figure.figsize': (10, 10)})
result.plot().suptitle('Time Series Decomposition of Air Passengers')
plt.savefig("../photos/change/timeSeriesDecompositionPlot.png")
plt.show()
