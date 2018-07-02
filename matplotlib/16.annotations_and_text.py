import matplotlib.pyplot as plt
import csv
from matplotlib import style
import numpy as np

style.use('mystyle')

x,y  = np.loadtxt('file.txt', delimiter=',', unpack=True)
plt.plot(x,y,label='Loaded from file')



# -------------------Text---------------------
font_dict = {
	'family':'serif',
	'color':'darkred',
	'size':10
}

plt.text(9,6,'Text',fontdict=font_dict)
# -------------------------------------------




# -----------------Annotation----------------
plt.annotate('Annotation',(10,8),
				xytext=(0.4,0.9), textcoords='axes fraction',
				arrowprops= dict(facecolor='w',color='m')	)

# ------------------------------------------

plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('matplotlib\nfirst graph')
plt.legend()
plt.show()

