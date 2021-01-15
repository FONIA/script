#QXV0aG9yPUZPTklBLEVtYWlsPTI2MzM1Njk1NTdAcXEuY29t
import json,os,time
from pyautogui import click,alert
def openfile():
    try:
        f=open("config.json",'r')
        data = json.load(f)
    except:
        alert('config数据缺失！',title='FONIA-错误提示')
        os._exit(0)
    return data
dt=openfile()
tarr=[0]
for v in range(len(dt)-1):
    tarr.append(round(dt[v+1]['l']-dt[v]['l'],1))
for i in range(len(dt)):
    click(dt[i]['x'],dt[i]['y'],button=dt[i]['b'])
    if i<len(dt)-1:
        time.sleep(tarr[i+1])

