import matplotlib.pyplot as plt


x=[1,3,5,7,9]
y=[8,3,7,2,9]


x1=[2,4,6,8,10]
y1=[4,5,1,6,7]
# pop = [23,25,55,76,87,12,70,123,32,89,76,58,68,98,57,33,44,55,66,98,68,19,94,102,113,123]
# ids = [i for i in range(len(pop))]
# plt.bar (ids,pop,label='First Bar',color='#0083ff')
plt.bar (x,y,label='First Bar',color='#0083ff')
plt.bar (x1,y1,label='Second Bar',color='#ff6c00')
plt.xlabel('xlabel')
plt.ylabel('ylabel')



plt.title('matplotlib\nbar graph')
plt.legend()
plt.show()