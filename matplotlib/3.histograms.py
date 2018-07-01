import matplotlib.pyplot as plt


pop = [23,25,55,76,87,12,70,123,32,89,76,58,68,98,57,33,44,55,66,98,68,19,94,102,113,123]
# ids = [i for i in range(len(pop))]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]


plt.hist (pop,bins,histtype='bar',rwidth=0.8,label='First Bar',color='#0083ff')
plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('matplotlib\nhistograms graph')
plt.legend()
plt.show()