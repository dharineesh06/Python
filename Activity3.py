#1 Display the powers of 2 using anonymous function
terms = int(input("How many terms? "))


result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
   
#2 Find Numbers Divisible by Another Number

my_list = [56,34,67,23,78,9,39,34,12]

result = list(filter(lambda x: (x % 13 == 0), my_list))

print("Numbers divisible by 13 are",result)

#3  Python program to convert decimal into other number systems
dec = 256

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

#4 ASCI KEY
c = 'd'
print("The ASCII value of '" + c + "' is", ord(c))

#5 find H.C.F of two numbers
def compute_hcf(x, y):


    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 72
num2 = 18

print("The H.C.F. is", compute_hcf(num1, num2))

#6 find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 18
num2 = 56

print("The L.C.M. is", compute_lcm(num1, num2))

#7 find the factors of a number

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 210

print_factors(num)

#8 Program make a simple calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")

#9 shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
   
# 10 display calendar of the given month and year

import calendar


yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))   

#11  Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 8


if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))

#12 # Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)


num = 20

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
   
#13 Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 15


if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

#14 # Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')


dec = 37

convertToBinary(dec)
print()

#15 

def name():
    return "John","Armin"
print(name())
name_1, name_2 = name()
print(name_1, name_2)