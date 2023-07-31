import requests
from bs4 import BeautifulSoup
req = requests.get('https://web.whatsapp.com/')
soup = BeautifulSoup(req.content,'html.parser')
print(soup.prettify())

content = soup.prettify()
with open('WhatsApp.html','w') as html:
    html.write(content)