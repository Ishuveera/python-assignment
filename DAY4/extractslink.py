import re
url=[]
f= open('links.txt', 'r')
File = f.read()
url = re.findall("(https?://[^\s]+)", File)
for link in url:
    print(link)