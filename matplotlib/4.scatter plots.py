import matplotlib.pyplot as plt


x=[1,2,3]
y=[8,3,7]


x1=[3,6,2]
y1=[3,5,7]

plt.scatter (x,y,label='First Line',marker='+',s=100)
plt.scatter (x1,y1,label='Second Line',marker='*',s=100)
plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('matplotlib\nfirst graph')
plt.legend()
plt.show()