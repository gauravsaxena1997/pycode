import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime.now()

print (start)
print (end)

df = web.DataReader("XOM", "morningstar", start, end)

#it reset index show the numeric indics
df.reset_index(inplace=True) 


#set date as our index
df.set_index("Date",inplace=True)

df = df.drop("Symbol",axis=1)

print(df)

df['High'].plot()
plt.show()