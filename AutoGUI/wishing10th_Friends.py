import pyautogui as pg
import time
time.sleep(1)
pg.hotkey('win','7')
time.sleep(0.5)
pg.press('enter')
time.sleep(2)
# Point(x=301, y=181)
pg.click(x=301,y=181)
time.sleep(0.5)
pg.write('Nothing')
time.sleep(0.5)
# మన జిందగీ 2018-19 😇
pg.press('enter')
# Point(x=958, y=692)
time.sleep(0.5)
pg.click(x=958,y=692)
time.sleep(0.5)
pg.write('Hello World!')
time.sleep(0.5)
pg.press('enter')

friends = ['Uday Kiran','Gayathri Vemula','M Yesu Babu','MAHESHWARI MISHU','Nagaraju V','Narendra','Parimi Lajar','Purna Miriyala','CALL ME SIVA','SHALEM RAJU','Ch Hemanth','Gopi pedapudi','i want to see your smile','parellaleela977','SKP','Sravanthi Jakkula','Sri Archana','Sukanya Ganugapanta','Vineetha Orsu','Smile Too','K Gopi K Gopi','R Sirisha','Gopi Gude','Vaishu Monaboti','Pedapudi Kumar','Venkatesh Velpula']

friends = sorted(friends)

for friend in friends:
    time.sleep(0.2)
    pg.write(f'Hello {friend}')
    time.sleep(0.2)
    pg.press('enter')
time.sleep(0.2)
pg.write('code return status 1')
pg.press('enter')
time.sleep(0.3)