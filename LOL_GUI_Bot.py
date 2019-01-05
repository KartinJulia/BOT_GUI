import pyautogui
import random

# mini map mid lane middle location
x_m = 1812
y_m = 934

# mini map top lane middle location
x_t = 1747
y_t = 868

# mini map bot lane middle location
x_b = 1878
y_b = 1003

# shop location
x_s = 756
y_s = 221
x_close_s = 1660

# buying the first and second items at the beginning location
x_b1 = 446
y_b1 = 240
x_b2 = 523
y_b2 = 250


# go into the game
pyautogui.moveTo(x_m, y_m,2)
pyautogui.click(x=x_m,y=y_m)
pyautogui.PAUSE = 2

# upgrade Q
##pyautogui.moveTo(830,935,3)
##pyautogui.mouseDown()
##pyautogui.mouseUp()
##pyautogui.PAUSE = 2

# upgrade E
pyautogui.moveTo(916,935,1)
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.PAUSE = 1

# use E
pyautogui.moveTo(917,968,1)
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.moveRel(0, -50,1)
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.PAUSE = 1

##pyautogui.moveTo(x=830,y=935)
##pyautogui.click(x=830,y=935,clicks = 2)
##pyautogui.moveTo(x=870,y=935)
##pyautogui.PAUSE = 2
##pyautogui.click(x=x_m,y=y_m,button='right')
##pyautogui.PAUSE = 5
##pyautogui.keyDown('a')
##pyautogui.click(x=x_m,y=y_m)
##pyautogui.keyUp('a')


# buy item

pyautogui.moveTo(x_s,y_s,1)
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.moveTo(x_b1, y_b1,1)
pyautogui.mouseDown(button='right')
pyautogui.mouseUp(button='right')
pyautogui.moveTo(x_b2, y_b2,1)
pyautogui.mouseDown(button='right')
pyautogui.mouseUp(button='right')
pyautogui.moveTo(x_close_s, y_close_s,1)
pyautogui.mouseDown()
pyautogui.mouseUp()

# go to mid lane middle
pyautogui.click(x=x_m,y=y_m,button='right',duration = 2)
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.PAUSE = 35

# use E
pyautogui.moveTo(917,968,1)
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.moveRel(0, -50,1)
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.PAUSE = 20


while True:
    pyautogui.moveTo(x_t,y_t,1)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
##a = 1
##while a > 0:
##    x1 = random.randint(10,1800)
##    y1 = random.randint(10,900)
##    pyautogui.moveTo(x1, y1, 5)
##    pyautogui.click(button='right')
##    x2 = random.randint(10,1800)
##    y2 = random.randint(10,900)
##    pyautogui.moveTo(x2, y2, 5)
##    pyautogui.click(button='right')

##x1 = random.randint(10,1800)
##y1 = random.randint(10,900)
##pyautogui.moveTo(x1, y1, 5)
##pyautogui.click(button='right')
##x2 = random.randint(10,1800)
##y2 = random.randint(10,900)
##pyautogui.moveTo(x2, y2, 5)
##pyautogui.click(button='right')


