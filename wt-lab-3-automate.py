import pyautogui as pg
import time
time.sleep(5)
k = 11
for i in range(1):
    pg.hotkey('super','d')
    time.sleep(2)
    pg.hotkey('super','1')
    pg.press('enter')
    time.sleep(2)
    pg.click(143, 161)
    for j in range(k):
        pg.press('down')
    pg.hotkey('alt', 'shift', 'c')
    pg.hotkey('super','8')
    pg.hotkey('ctrl','t')
    pg.hotkey('ctrl', 'l')
    pg.hotkey('ctrl', 'v')
    pg.press('enter')
    time.sleep(2)
    pg.hotkey('super','prtsc')
    time.sleep(1)
    pg.hotkey('ctrl','w')
    k += 1
    time.sleep(3)
