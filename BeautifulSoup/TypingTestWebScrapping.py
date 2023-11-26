# Programme to Scrape the RataType Website 
from bs4 import BeautifulSoup
import requests
import pyautogui as pg
import time
time.sleep(2)
# pg.hotkey('super','d')
# time.sleep(2)
# pg.press('super')
# pg.write('chrome')
# time.sleep(1)
# pg.press('enter')
# time.sleep(2)
# pg.click()
# pg.hotkey('super','up')
# pg.hotkey('ctrl','l')
# time.sleep(1)
# pg.write('https://www.ratatype.com/typing-test/test/')
# pg.press('enter')
# time.sleep(1)
# pg.click()
# pg.hotkey('super','up')
# time.sleep(1)
# pg.click(750,521)
# time.sleep(10)



# requests.get('https://www.ratatype.com/typing-test/test/')
html_text = requests.get('https://www.amazon.in/s?k=t-shirts+for+men&ref=nb_sb_noss').text
print(html_text)