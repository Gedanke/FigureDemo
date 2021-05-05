# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as stattools

# Import Data
df = pandas.read_csv('../dataset/mortality.csv')
x = df['mdeaths']
y = df['fdeaths']

# Compute Cross Correlations
ccs = stattools.ccf(x, y)[:100]
nlags = len(ccs)

# Compute the Significance level
# ref: https://stats.stackexchange.com/questions/3115/cross-correlation-significance-in-r/3128#3128
conf_level = 2 / numpy.sqrt(nlags)

# Draw Plot
plt.figure(figsize=(12, 7), dpi=80)

plt.hlines(0, xmin=0, xmax=100, color='gray')  # 0 axis
plt.hlines(conf_level, xmin=0, xmax=100, color='gray')
plt.hlines(-conf_level, xmin=0, xmax=100, color='gray')

plt.bar(x=numpy.arange(len(ccs)), height=ccs, width=.3)

# Decoration
plt.title('$Cross\; Correlation\; Plot:\; mdeaths\; vs\; fdeaths', fontsize=18)
plt.xlim(0, len(ccs))
plt.savefig("../photos/change/crossCorrelationPlot.png")
plt.show()
