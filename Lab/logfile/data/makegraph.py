#!/usr/bin/env python3
# -*- cording: utf-8 -*-
# makegraph.py: ログ用のグラフを作成する
# %%
import os
from random import sample
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import datetime
import sys, os
# %%
# ログ用グラフを描写
def makegraph(csv_path = 'data.csv', out_path = '../img/log_graph.jpg', datacolumn='data1', scope=10, title=None):
    df = pd.read_csv(csv_path)

    for i, _ in enumerate(df['year']):
        df.loc[i, 'TIME'] = datetime.datetime(
        df.loc[i, 'year'], df.loc[i, 'month'], df.loc[i, 'day'], df.loc[i, 'hour'], df.loc[i, 'minute'])

    fig, ax = plt.subplots(1,1, figsize=(10,4))
    time = df['TIME'].values[-1*scope:]
    data1 = df[datacolumn].values[-1*scope:]
    ax.plot(time, data1)
    ax.scatter(time, data1)
    ax.grid()
    ax.set_title(title, fontsize=20)
    fig.savefig(out_path)

# %%
if __name__=='__main__':
    now_dir = os.path.dirname(__file__)
    makegraph(f'{now_dir}/data.csv', f'{now_dir}/../img/log_graph.jpg', 'data1', 10, 'sample')
    print(datetime.datetime.now())
# %%
