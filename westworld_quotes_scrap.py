import bs4 as bs
import pickle
import requests
import time


resp = requests.get('https://quotecatalog.com/quotes/tv/westworld/')
soup = bs.BeautifulSoup(resp.text, 'lxml')
fhand = open ('westworld_qoutes.txt','a')


for  cards in soup.findAll('div', {'class': 'quote--card bg-white mb2 p2 relative'}):
	for a in cards.findAll('a', {'class': 'quote__text'}):
		fhand.write (a.text+'\n')

fhand.close()