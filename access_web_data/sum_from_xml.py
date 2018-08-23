import urllib.request as ur
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_31276.xml'
data = ur.urlopen(url).read()
tree = ET.fromstring(data)

counts = tree.findall('comments/comment/count')
total = 0
for count in counts:
	total += int(count.text)
print ('total: ', total)