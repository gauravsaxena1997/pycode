import urllib.request, urllib.parse, urllib.error

url = input ("Enter URL: ")

fhand = urllib.request.urlopen('http://'+url)

counts = dict()
total_count = 0
print ( counts )

for line in fhand:
	words = line.decode().split()
	print (words)

	for word in words:
	# 	total_count = total_count + 1
	# 	if words not in counts:
	# 		counts[words] = 1
	# 	else:
	# 		counts[words] = counts[words] + 1
		counts[word] = counts.get(word,0)+1

print ( '\n')
print ( "Total words are: "+ str(total_count) )
print ( counts )