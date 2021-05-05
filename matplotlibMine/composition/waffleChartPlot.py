# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
from pywaffle import Waffle

# Import
df_raw = pandas.read_csv("../dataset/mpg_ggplot2.csv")

# Prepare Data
df = df_raw.groupby('class').size().reset_index(name='counts')
n_categories = df.shape[0]
colors = [
    plt.cm.Set1(i / float(n_categories)) for i in range(n_categories)
]

# Draw Plot and Decorate
fig = plt.figure(
    FigureClass=Waffle,
    plots={
        '111': {
            'values':
                df['counts'],
            'labels': [
                "{0} ({1})".format(n[0], n[1])
                for n in df[['class', 'counts']].itertuples()
            ],
            'legend': {
                'loc': 'upper left',
                'bbox_to_anchor': (1.05, 1),
                'fontsize': 12
            },
            'title': {
                'label': 'Vehicles by Class',
                'loc': 'center',
                'fontsize': 18
            }
        },
    },
    rows=7,
    colors=colors,
    dpi=80,
    figsize=(12, 9)
)
plt.savefig("../photos/composition/waffleChartPlot1.png")
plt.show()

"""
"""

# Prepare Data
# By Class Data
df_class = df_raw.groupby('class').size().reset_index(name='counts_class')
n_categories = df_class.shape[0]
colors_class = [
    plt.cm.Set3(i / float(n_categories)) for i in range(n_categories)
]

# By Cylinders Data
df_cyl = df_raw.groupby('cyl').size().reset_index(name='counts_cyl')
n_categories = df_cyl.shape[0]
colors_cyl = [
    plt.cm.Set1(i / float(n_categories)) for i in range(n_categories)
]

# By Make Data
df_make = df_raw.groupby('manufacturer').size().reset_index(name='counts_make')
n_categories = df_make.shape[0]
colors_make = [
    plt.cm.tab20b(i / float(n_categories)) for i in range(n_categories)
]

# Draw Plot and Decorate
fig = plt.figure(
    FigureClass=Waffle,
    plots={
        '311': {
            'values':
                df_class['counts_class'],
            'labels': [
                "{1}".format(n[0], n[1])
                for n in df_class[['class', 'counts_class']].itertuples()
            ],
            'legend': {
                'loc': 'upper left',
                'bbox_to_anchor': (1.05, 1),
                'fontsize': 12,
                'title': 'Class'
            },
            'title': {
                'label': 'Vehicles by Class',
                'loc': 'center',
                'fontsize': 18
            },
            'colors':
                colors_class
        },
        '312': {
            'values':
                df_cyl['counts_cyl'],
            'labels': [
                "{1}".format(n[0], n[1])
                for n in df_cyl[['cyl', 'counts_cyl']].itertuples()
            ],
            'legend': {
                'loc': 'upper left',
                'bbox_to_anchor': (1.05, 1),
                'fontsize': 12,
                'title': 'Cyl'
            },
            'title': {
                'label': 'Vehicles by Cyl',
                'loc': 'center',
                'fontsize': 18
            },
            'colors':
                colors_cyl
        },
        '313': {
            'values':
                df_make['counts_make'],
            'labels': [
                "{1}".format(n[0], n[1])
                for n in df_make[['manufacturer', 'counts_make']].itertuples()
            ],
            'legend': {
                'loc': 'upper left',
                'bbox_to_anchor': (1.05, 1),
                'fontsize': 12,
                'title': 'Manufacturer'
            },
            'title': {
                'label': 'Vehicles by Make',
                'loc': 'center',
                'fontsize': 18
            },
            'colors':
                colors_make
        }
    },
    rows=9,
    dpi=80,
    figsize=(12, 14)
)
plt.savefig("../photos/composition/waffleChartPlot2.png")
plt.show()
