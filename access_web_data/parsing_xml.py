import xml.etree.ElementTree as et

data='''
<person>
<name>Gaurav</name>
<phone type='intl'>
	+91 954 999 2949
</phone>
<email hide='yes'/>
</person>
'''

tree = et.fromstring(data)

print (tree)
print ( 'Name: ', tree.find('name').text )
print ( 'Attr: ', tree.find('email').get('hide') )
