import pandas as pd



'''
Read from csv , set col 0 as index 
df = pd.read_csv('housing.csv',index_col=0)
df.columns = ['Austin_HPI']
'''

'''
Save df to csv
df.to_csv('austin_hpi.csv')
'''


'''
Save with no headers ans read it 
df.to_csv('noheaders.csv',header=False)
df = pd.read_csv('noheaders.csv', names=['date','Austin_HPI'],index_col=0)
'''


'''
Save df as html file
df = pd.read_csv('austin_hpi.csv', index_col=0)
df.to_html('austin_hpi.html')
'''

#Rename column
df = pd.read_csv('austin_hpi.csv', index_col=0)
df.rename (columns={'Austin_HPI':'77006_HPI'},inplace=True)

print (df.head())
