# -*- coding:utf-8 -*-

import pandas
import numpy
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial import ConvexHull

# Import Data
df = pandas.read_csv('../dataset/USArrests.csv')

# Agglomerative Clustering
cluster = AgglomerativeClustering(
    n_clusters=5,
    affinity='euclidean',
    linkage='ward'
)
cluster.fit_predict(df[['Murder', 'Assault', 'UrbanPop', 'Rape']])

# Plot
plt.figure(figsize=(12, 8), dpi=80)
plt.scatter(
    df.iloc[:, 0], df.iloc[:, 1], c=cluster.labels_, cmap='tab10'
)


# Encircle
def encircle(x, y, ax=None, **kw):
    if not ax: ax = plt.gca()
    p = numpy.c_[x, y]
    hull = ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices, :], **kw)
    ax.add_patch(poly)


# Draw polygon surrounding vertices
encircle(
    df.loc[cluster.labels_ == 0, 'Murder'],
    df.loc[cluster.labels_ == 0, 'Assault'],
    ec="k",
    fc="#dc2624",
    linewidth=0
)
encircle(
    df.loc[cluster.labels_ == 1, 'Murder'],
    df.loc[cluster.labels_ == 1, 'Assault'],
    ec="k",
    fc="#2b4750",
    linewidth=0
)
encircle(
    df.loc[cluster.labels_ == 2, 'Murder'],
    df.loc[cluster.labels_ == 2, 'Assault'],
    ec="k",
    fc="#649E7D",
    linewidth=0
)
encircle(
    df.loc[cluster.labels_ == 3, 'Murder'],
    df.loc[cluster.labels_ == 3, 'Assault'],
    ec="k",
    fc="#C89F91",
    linewidth=0
)
encircle(
    df.loc[cluster.labels_ == 4, 'Murder'],
    df.loc[cluster.labels_ == 4, 'Assault'],
    ec="k",
    fc="#c7cccf",
    linewidth=0
)

# Decorations
plt.xlabel('Murder')
plt.xticks(fontsize=12)
plt.ylabel('Assault')
plt.yticks(fontsize=12)
plt.title('Agglomerative Clustering of USArrests (5 Groups)', fontsize=18)
plt.savefig("../photos/groups/clusterPlot.png")
plt.show()
