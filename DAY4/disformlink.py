import re
class dis:
    def __init__(Obj, name, url, time):
        Obj.name = name
        Obj.link = url
        Obj.time = time
name=[]
url=[]
time=[]
f= open('links.txt', 'r')
File = f.read()
name = re.findall("(?<=from )(.*)(?=to)", File)
url = re.findall("(https?://[^\s]+)", File)
time = re.findall("[0-1][0-2]:[0-5][0-9] AM|[0-1][0-2]:[0-5][0-9] PM", File)
lst = []
for (a,b,c) in zip(name, url, time):
    l = dis(a,b,c)
    lst.append(l)

for link in lst:
    print(f'Name: {link.name} \n Url: {link.link} \n Time: {link.time}')