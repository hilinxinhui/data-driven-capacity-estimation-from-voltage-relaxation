import pandas as pd
import os
import re
import numpy as np

df_res = pd.DataFrame(columns=['cycle', 'Voltages', 'rate', 'Tem', 'Capacity'])
files = os.listdir('./Dataset_1_NCA_battery/')
for file in range(len(files)):
    # 读取一块电池数据对应的csv文件
    data_r = pd.read_csv(os.path.join('./Dataset_1_NCA_battery/', files[file]))
    # 一块电池的循环数据
    min_cycle_number = int(np.min(data_r['cycle number'].values))
    max_cycle_number = int(np.max(data_r['cycle number'].values)) + 1
    total_rul = max_cycle_number - min_cycle_number
    Tem = int(files[file][2:4]) # 设定的恒温室的温度，不是电池表面温度
    for i in range(int(np.min(data_r['cycle number'].values)), int(np.max(data_r['cycle number'].values))+1):
        data_i = data_r[data_r['cycle number'] == i] # 第i个循环的数据
        time = np.array(data_i['time/s']) # 距离开始时间点的时间（序列）
        Ecell = np.array(data_i['Ecell/V']) # 电压序列
        Q_dis = np.array(data_i['Q discharge/mA.h']) # 放电容量序列，最大放电容量是capacity标签
        # Q_ch = np.array(data_i['Q charge/mA.h']) # 充电容量序列，可以结合Q_dis计算电荷量序列
        Current = np.array(data_i['<I>/mA']) # 电流序列
        control = np.array(data_i['control/V/mA']) # 控制字段，3500表示CC充电，4.x的值指示CV充电，-3500表示CC放电
        cr = np.array(data_i['control/mA'])[1]/3500 # 充电倍率，cr和上一行的control字段完全一致
        if np.max(Q_dis) < 2500 or np.max(Q_dis) > 3500:
            continue
        index = np.where(np.abs(control) == 0)
        start = index[0][0]
        end = 13
        for j in range(3):
            if control[start+3] == 0:
                break
            else:
                start = index[0][j+1]
        if Current[start] > 1:
            start = start + 1
            if control[start + 13] != 0:
                end = 12
        if control[start + end] == 0 and Ecell[start + end] > 4.0:
            df_res = df_res._append({'cycle': i, 'Voltages': Ecell[start:start+14], 'rate': cr, 'Tem': Tem,
                                    'Capacity': np.max(Q_dis)}, ignore_index=True) # https://zhuanlan.zhihu.com/p/655528474

    break # 先读取第一块电池的数据

# Save to excel file
# df_res.to_excel('Dataset_1_NCA_battery.xlsx', index=False)
# Or save to csv file
# df_res.to_csv('Dataset_1_NCA_battery.csv', index=False)
print('Features extraction is done')
