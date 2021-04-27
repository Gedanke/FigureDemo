# -*- coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv("../dataset/mpg_ggplot2.csv")
sns.set(style="whitegrid", font_scale=1.5)  # 设置主题，文本大小
g = sns.jointplot(
    x='displ',
    y='hwy',
    data=df,  # 输入两个绘图变量
    color='#098154',  # 修改颜色
)
g.fig.set_size_inches(10, 8)  # 设置图尺寸
plt.savefig("../photos/correlation/marginalHistogramSnsPlot.png")
