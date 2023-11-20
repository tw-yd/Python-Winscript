import pyautogui
import time
import re
import os

Exist = False
while Exist == False :  #判斷檔案是否存在
    path = str(input('請輸入讀檔路徑:')) + '.txt'

    if os.path.isfile(path) == True:
        Exist = True
    else :
        print('檔案不存在，請更換名稱!')
File=(open(path, 'r').readlines())  #仔入檔案

for i in range(3, -1, -1):
    print('倒數',i,'秒開始執行【',path,'】')
    time.sleep(1)

#主程式
for i in File:  #判定腳本
    print(i,end = '')
    x = re.search('\((.+?)\,', i).group(1)
    y = re.search('\,(.+?)\)', i).group(1)

    x = re.sub(r"\s+", "", x)
    y = re.sub(r"\s+", "", y)

    x = int(x)
    y = int(y)

    pyautogui.moveTo(x, y,)

    if 'Button'in i :
        if 'left' in i :
            if 'True' in i :
                pyautogui.mouseDown(button='left')
                print(x,y,'do')
            elif 'False' in i:
                pyautogui.mouseUp(button='left')
                print(x,y,'up')
        
        if 'middle' in i :
            print(x,y)

        if 'right' in i :
            print(x,y)
    
    time.sleep(0.5)