import urllib
import re
url=raw_input("enter url here:")
html=urllib.urlopen(url)
b=html.read()
pattern=re.compile('img src=["](.*?)"')
a=re.findall(pattern,b)

notepad=open("output.txt","w")
for i in a:
	notepad.write(url+i+"\n")

	
notepad.close()
