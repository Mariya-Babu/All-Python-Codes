import pyautogui as pg
import time as t
t.sleep(1)
pg.click(1261,0)     #Point(x=1261, y=0)
t.sleep(5)
pg.click(27,747) #Point(x=27, y=747)
t.sleep(1)
pg.write('cmd')
t.sleep(1)
pg.press('enter')
t.sleep(1)
pg.write('mysql -u root -p')
t.sleep(1)
pg.press('enter')
t.sleep(1)
pg.write('N.Mariya Babu')
t.sleep(1)
pg.press('enter')
t.sleep(1)
pg.write('SHOW DATABASES;')
t.sleep(1)
pg.press('enter')
