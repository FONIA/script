from pynput import mouse
import json,time,os
def trans(k):
    if k.value==(4,2):
        return ['left','左键']
    if k.value==(16,8):
        return ['right','右键']
    if k.value==(64,32):
        return ['middle','滚轮']
def press():
    global xtime
    xtime=time.time()
def up():
    return [time.time(),time.time()-xtime]
arr=[]    
def on_click(x,y,button,pressed):   
    if (x,y)==(0,0):
        with open("config.json","w") as f:
            json.dump(arr,f)
        os._exit(0)
    if pressed==True:
        press()
    if pressed==False:
        list={}
        list['x'],list['y'],list['b'],list['t'],list['l']=x,y,trans(button)[0],round(up()[1],2),up()[0]
        arr.append(list)
while 1:
     with mouse.Listener(on_move='',on_click=on_click,on_scroll='') as listener2:
        listener2.join()
       
