import urllib.request, urllib.error, urllib.parse


url = input ("Enter the URL: ")

fhand = urllib.request.urlopen('http://'+url)

for line in fhand:
	print ( line.decode().strip() )


