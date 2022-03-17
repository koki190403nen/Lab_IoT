#! /usr/bin/env python3
# -*- cording: utf-8 -*-

# %%
import datetime, time
# センサーからデータを取得する
def GetData(observe=None):
    now = datetime.datetime.now()
    return observe, now

if __name__=='__main__':
    data, now = GetData()
    
    print(now.year)
# %%
