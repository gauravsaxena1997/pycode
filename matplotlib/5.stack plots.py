import matplotlib.pyplot as plt


days=[1,2,3,4,5]
sleeping=[3,6,2,7,12]
eating=[2,3,1,4,2]
playing=[12,3,5,2,7]

plt.plot ([],[],color='m',label='sleeping',linewidth=5)
plt.plot ([],[],color='g',label='eating',linewidth=5)
plt.plot ([],[],color='b',label='playing',linewidth=5)
colr = ['m','g','b']


plt.stackplot (days,sleeping,eating,playing,colors=colr)
plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('matplotlib')
plt.legend()
plt.show()