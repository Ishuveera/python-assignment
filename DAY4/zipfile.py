from zipfile import ZipFile

zipf = 'assign2.zip'
filename = 'links.txt'

with ZipFile(zipf, 'w') as z:
    z.write(filename)
