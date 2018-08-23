import sqlite3
import pandas as pd

conn = sqlite3.connect('twitterr.db')
c = conn.cursor()

df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE '%you%' ORDER BY unix DESC LIMIT 1000", conn)
print(df)

df.sort_values('unix', inplace=True)
df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
df.dropna(inplace=True)


# df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE '%atal%' ORDER BY unix DESC LIMIT 1000", conn)

print(df)
