import matplotlib.pyplot as plt

slices = [7,6,2,13]
activities = ['sleeping','eating','playing','working']
colr = ['m','r','g','b']

plt.pie (slices, labels=activities,
				colors=colr , 
				startangle=90, 
				explode=(0,0,0.1,0),
				autopct='%1.1f%%' )


# shadow=True

plt.title('matplotlib')
plt.show()