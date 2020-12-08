vertices = {}
arcslist = {}

currentSelected = vertices

with open('Roget.net') as myFile:
    rogetFile = myFile.read().splitlines()
    for line in rogetFile:
        currentList = line.split(' ', 1)

        if(currentList[0] == '*Vertices'):
            currentSelected = vertices

        elif(currentList[0]== '*Arcslist'):
            currentSelected = arcslist

        else:
            currentSelected[int(currentList[0])] = currentList[1]
print('Select A Vertices Number From 1 To 1021')
print('='*30)            
n = int(input('Enter a Vertices number: '))
print('='*20)  
print(f'Vertices---> {vertices[n]} \nArcsList---> {arcslist[n]}')
print('='*25) 