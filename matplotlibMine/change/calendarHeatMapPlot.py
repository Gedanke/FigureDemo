# -*- coding:utf-8 -*-

import numpy
import pandas

numpy.random.seed(sum(map(ord, 'calmap')))
import calmap

events = pandas.read_csv('../dataset/AirPassengers.csv')
calmap.calendarplot(events,
                    monthticks=3,
                    daylabels='MTWTFSS',
                    dayticks=[0, 2, 4, 6],
                    cmap='YlGn',
                    fillcolor='grey',
                    linewidth=0,
                    fig_kws=dict(figsize=(8, 4)))
# calendarHeatMapPlot
