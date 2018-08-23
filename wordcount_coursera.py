import urllib.request as ur
from bs4 import *
url = input('Enter the url to scrape - ')
html = ur.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
count = 0
sum = 0
spans = soup('span')
for span in spans:
	print (span.contents)
	sum += int(span.contents[0])
	count += 1

print('Count ',count)
print('Sum ',sum)