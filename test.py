import pyautogui as pg
import time
time.sleep(5)
pg.hotkey('super','d')
time.sleep(1)
pg.hotkey('super','9')
pg.click(917,313)
for i in range(5):
    time.sleep(1)
    pg.press('right')
    time.sleep(1)
