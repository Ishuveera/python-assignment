def  fibonacci(num):
	if num<=1:
		return num
	else:
		return(fibonacci(num-1)+fibonacci(num-2))
num1=int(input("enter number of terms"))
print("fibonacci series:")
for i in range(num1):
	print(fibonacci(i))