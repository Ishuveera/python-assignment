import re

file_one = open('regex.html', 'r')
f = file_one.read()

f2 = re.sub('<.*?>','',f)
file_two = open('regex.txt', 'x')
file_two.write(f2)

file_one.close()
file_two.close()
