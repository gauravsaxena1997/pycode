import matplotlib.pyplot as plt
import csv
import numpy as np



'''
#By csv
q = []
w = []
with open ('file.txt','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		print (row)
		q.append(int(row[0]))
		w.append(int(row[1]))

plt.plot(q,w,label='Loaded from file')
'''

# -------By numpy

x,y  = np.loadtxt('file.txt', delimiter=',', unpack=True)
plt.plot(x,y,label='Loaded from file')

plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('matplotlib\nfirst graph')
plt.legend()
plt.show()

