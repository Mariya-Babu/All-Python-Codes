import pyautogui as pg
import time
time.sleep(5)
pg.hotkey('super','d')
k = 0
time.sleep(1)
for i in range(12):
    time.sleep(2)
    pg.hotkey('super','d')
    time.sleep(2)
    pg.hotkey('super','1')
    pg.press('enter')
    time.sleep(2)
    pg.click(143, 161)
    for j in range(k):
        pg.press('down')
    pg.press('enter')
    time.sleep(1)
    pg.click(917,313)
    time.sleep(1)
    pg.hotkey('ctrl','a')
    time.sleep(1)
    pg.hotkey('ctrl','c')
    time.sleep(1)
    pg.hotkey('super','d')
    time.sleep(1)
    pg.hotkey('super','7')
    time.sleep(1)
    pg.hotkey('ctrl','a')
    time.sleep(1)
    pg.press('backspace')
    time.sleep(1)
    pg.hotkey('ctrl','v')
    time.sleep(1)
    pg.hotkey('ctrl','a')
    time.sleep(1)
    pg.hotkey('ctrl','c')
    time.sleep(1)
    pg.hotkey('super','d')
    time.sleep(1)
    pg.hotkey('super','6')
    time.sleep(3)
    for n in range(3):
        pg.press('enter')
        time.sleep(1)
    pg.hotkey('ctrl','v')
    time.sleep(1)
    pg.hotkey('super','d')
    time.sleep(1)
    pg.hotkey('super','8')
    time.sleep(2)
    pg.click(917,313)
    pg.hotkey('ctrl','c')
    time.sleep(1)
    pg.click(1347,390)  #right
    time.sleep(1)
    pg.hotkey('super','d')
    time.sleep(1)
    pg.hotkey('super','6')
    time.sleep(3)
    for m in range(3):
        pg.press('enter')
        time.sleep(1)
    pg.hotkey('ctrl','v')
    time.sleep(1)
    pg.hotkey('super','d')
    time.sleep(1)
    k += 1
    time.sleep(3)