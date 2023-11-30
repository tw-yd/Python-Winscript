import pynput
import os



Not_Repeating = False
while Not_Repeating == False:  #檔案是否重複
    path = str(input('請輸入存檔路徑:')) + '.txt'

    if os.path.isfile(path) == False:
        Not_Repeating = True
    else :
        print('檔案已存在，請更換名稱!')

File = open(path, 'x')
print('輸入完成')

print('滑鼠記錄開始')
with pynput.mouse.Events() as event:  #滑鼠偵測
    for i in event:
        x=i.x
        y=i.y

        if x == 0 and y == 0:  #偵測中斷
            break

        if isinstance(i, pynput.mouse.Events.Click):  #滑鼠點擊
            print('(', x, ',', y, ')', i.button, i.pressed,file=File)
            print('(', x, ',', y, ')', i.button, i.pressed)

        if isinstance(i, pynput.mouse.Events.Scroll):  #滑鼠滾輪
            print('(', x, ',', y, ')','Button.middle',i.dy,file=File)
            print('(', x, ',', y, ')','Button.middle',i.dy)

File.close()

print('')
print('滑鼠記錄結束，檔案儲存於',path)
