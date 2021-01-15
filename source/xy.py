#QXV0aG9yPUZPTklBLEVtYWlsPTI2MzM1Njk1NTdAcXEuY29t
import time,os
from pyautogui import position
from tkinter import Tk,StringVar,Label,LEFT
def mouseadress():
    try:
        top = Tk()
        top.title('FONIA')
        text = StringVar()
        L1 = Label(top,textvariable=text,justify='left',anchor='w')
        L1.pack(side=LEFT)
        while True:
            x,y=position()
            if (x,y)!=(-1,-1) and (x,y)!=position():        
                text.set('X坐标：{0}\nY坐标：{1}'.format(str(x).rjust(4),str(y).rjust(4)))
                L1.update()
            else:
                (x,y)=(-1,-1)      
        top.mainloop()
    except:
        os._exit(0)
mouseadress()
