# import pyatuogui as pg
# import time

# time.sleep(2)
# pg.hotkey('super','d')
# time.sleep(1)
# pg.hotkey('super')
# time.sleep(1)
# pg.write('whatsapp')
# time.sleep(1)
# pg.press('enter')
# time.sleep(1)

# Programme to Scrape the RataType Website 
import pyautogui as pg
import time

friends = ['Durga Prasad','Lakshmi Babu','John','Siri Venkat','Yashwanth Vanapalli']
time.sleep(2)
pg.hotkey('super','d')
time.sleep(1)
pg.hotkey('super')
time.sleep(1)
pg.write('whatsapp')
time.sleep(1)
pg.press('enter')
time.sleep(10)
pg.write('room mates')
# pg.press('enter')
time.sleep(1)
pg.press('down')
pg.press('enter')
time.sleep(1)
pg.click(822,711)
pg.write('Hello Friends!')
pg.press('enter')
time.sleep(1)
for friend in friends:
    time.sleep(1)
    pg.write(f'Hello {friend}')
    pg.press('enter')