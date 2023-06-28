import pyautogui as pg
import time
time.sleep(5)
pg.click(1208,10)
time.sleep(5)
pg.click(39,512)
pg.click(39,512)
time.sleep(3)
pg.hotkey('ctrl','n')
pg.write("#include<stdio.h")
pg.press('end')
pg.press('enter')
pg.write("int main(){")
pg.press('enter')
pg.write("printf(\"Hello User")
pg.press('end')
pg.press(';')

