def recursion(num):
	if num<=10:
		print(f'{num}',end= ' ')
		recursion(num+1)
		print(f'{num}',end= ' ')
recursion(1)