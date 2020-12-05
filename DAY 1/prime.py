start =int(input("enter start number: \t"))
for n in range(start,start+100):
	if n > 1:
		for i in range(2,n):
			if(n % i) == 0:
				break
		else:
			print(n)
