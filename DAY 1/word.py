nummap = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "ten" : 10,
    "eleven" : 11,
    "twelve" : 12,
    "thirteen" : 13,
    "fourteen" : 14,
    "fifteen" : 15,
    "sixteen" : 16,
    "seventeen" : 17,
    "eighteen" : 18,
    "nineteen" : 19,
    "twenty" : 20,
    "thirty" : 30,
    "forty" : 40,
    "fifty" : 50,
    "sixty" : 60,
    "seventy" : 70,
    "eighty" : 80,
    "ninety" : 90,
    "hundred" : 100,
    "thousand" : 1000,
    "lakh" : 100000,
    "crore" : 10000000
} 

print('enter a number in words')
string = input()
string = string.lower()
words = string.split()
numbers = []
amount = 0

for w in words:
    if w in nummap:
        numbers.append(nummap[w])

temp = 0
for itr in range(0,len(numbers)):
    if(numbers[itr] < 20):
        if(temp):
            temp = temp + numbers[itr]
        else:
            temp = numbers[itr]

    
    elif(numbers[itr]%10 == 0 and numbers[itr] >= 100):
        temp = temp * numbers[itr]
        amount = amount + temp
        temp = 0
    
    else:
        temp = numbers[itr]

amount = amount + temp
    
print(amount)

         
