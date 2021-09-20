import time
import os
import notify2
import requests
from bs4 import BeautifulSoup

URL = "https://gadgets.ndtv.com/finance/crypto-currency-price-in-india-inr-compare-bitcoin-ether-dogecoin-ripple-litecoin"
r = requests.get(URL)


def get_coin_price(): 
	coin = {}  
	soup = BeautifulSoup(r.content, 'html5lib')
	table = soup.find('div', class_='story_detail row margin_b20') 
	for i,j in zip(table.findAll('div', class_='_flx crynm'), table.findAll('td', class_='_rft _cpr')):
	  coin[i.text.strip()] = j.text.strip()
	return coin
 
ICON_PATH = os.getcwd()+'/crypto.ico'

notify2.init("Crypto Price Notifier")   

n = notify2.Notification(None,icon=ICON_PATH)
  
n.set_urgency(notify2.URGENCY_NORMAL)
  
n.set_timeout(10000)   #Show notification for 10s
while(1):       
	coin = get_coin_price()
	for i,j in coin.items():
		
		n.update(i, j)
	 
		n.show()
	 
		time.sleep(5)		
