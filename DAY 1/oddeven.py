start =int(input("enter start number: \t"))
end =int(input("enter last number: \t"))
for n in range(start,end + 1):
	if n % 2 ==0:
		print("even number",n , end = "\n ")
	else:
		print("odd number",n,end = " ")
