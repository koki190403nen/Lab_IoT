#! /usr/bin/env python3
# -*- cording: utf-8 -*-

# %%
#from getdata import GetData
from cProfile import label
import schedule, datetime, time



class mainjob:
    def __init__(self):
        self.ob_now = None  # 観測時刻
        self.observe = None  # 観測値

    # 実行関数
    def main_func(self):
        self.GetData_()  # データの取得
        self.GetNow()  # 時刻の取得
        print(self.ob_now)  # 時刻の表示

    # スケジューリングして実行
    def do_schedule(self, hour:set, min:set, sec:set):
        # 予約
        for h in range(*hour):
            for m in range(*min):
                for s in range(*sec):
                    str_h, str_m, str_s = str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)
                    schedule.every().day.at(f'{str_h}:{str_m}:{str_s}').do(self.main_func)

        # 実行
        while True:
            schedule.run_pending()
            time.sleep(1)

    # データの取得
    def GetData_(self, observe=None):
        self.observe = observe

    # 時刻の取得
    def GetNow(self):
        self.ob_now = datetime.datetime.now()

    # データの保存
    def Savedata(self):
        pass



# 実行関数
if __name__=='__main__':
    mj = mainjob()
    mj.do_schedule(hour=(0, 24, 1), min=(0, 60, 1), sec=(10, 50, 10))

# %%
lambda:None
# %%
