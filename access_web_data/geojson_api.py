import urllib.parse as up
import urllib.request as ur
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break
    url = serviceurl + up.urlencode({'address': address})
    print (url)

    data = ur.urlopen(url).read().decode()
    js = json.loads(str(data))
    place_id = js["results"][0]['place_id']
    print (place_id)