import urllib.request as ur 
import json

url =  input('Enter url: ')
data = ur.urlopen(url).read().decode()
data_parsed = json.loads(data)
total = 0

for item in data_parsed['comments']:
  total += int(item['count'])

print ('Total: ', total)