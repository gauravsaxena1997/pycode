import matplotlib.pyplot as plt
import matplotlib.animation as anime
from matplotlib import style
import random
import time

style.use('mystyle')

fig = plt.figure()
ax1 = fig.add_subplot (1,1,1)

def create_plots():
	graph_data = open ('live.txt','a')
	for i in range(10):
		x = i
		y = random.randrange(10)
		cord = str(x)+","+str(y)+"\n"
		graph_data.write(cord)
	graph_data.close()

def animate (i):
	create_plots()
	graph_data = open ('live.txt','r').read()
	lines = graph_data.split ('\n')
	xs = []
	ys = []
	for line in lines:
		if (len(line) > 1):
			 x,y = line.split (',')
			 xs.append (x)
			 ys.append (y)

	ax1.clear()
	ax1.plot (xs,ys)
	time.sleep(3)
	open('live.txt','w').close()

ani = anime.FuncAnimation (fig, animate, interval=1000)
plt.show()