#1 Check if positve, negatvie 0r zero

num = 0

if num > 0:
    print('this number is positve')
elif num < 0:
    print('This number is negative')
else:
    print('It is equal to zero')

#2 even or odd

num2=int(input('Enter the number: '))
if num2 %2 == 0:
    print('This is even')
else:
    print('This is odd')

#3 leap year
year= int(input('Enter the year: '))
if year % 4 == 0 and year %100 != 0:
    print('This is a leap year')
elif year % 400 == 0 and year %100 == 0:
    print('This is a leap year')
else:
    print('This is not a leap year')
    
#4 lsrgest in 3 nos

num1=int(input('Enter the number1: '))
num2=int(input('Enter the number2: '))
num3=int(input('Enter the number3: '))

if num1>=num2 and num1>=num3:
    print(f' {num1} is the largest among these')
elif num2>=num1 and num2>=num3:
    print(f' {num2} is the largest among these')   
else:
    print(f'{num3} is the largest among these')
    
#5 prime number
num=11
if num>1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,'Is not a prime')
            break
    else:
        print('it is a prime number')

else:
    print(num,'It is not a prime')
    
#6 prime numbers in display
lower = 90
upper = 180

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#7 factorial
num = 17

factorial = 1
if num<0:
    print('it is negative number')
elif num == 0:
    print('The factorial is 1 for 1')
else:    
    for i in range(1, num+1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
    
#8
num = 12
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

#9Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

#10check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   order = len(str(num))  
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

#11Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):


   order = len(str(num))

   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)       
               
#12 Sum of natural numbers up to num

num = 24

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
   
#13 
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
    
#14
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)

#15
num = 6789
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

#16 power of a number
base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))