#1
arr=[13,5,8,9]
ans=sum(arr)
print('sum of array: ', ans)

def largest(arr,n):
  
    # Initialize maximum element
    max = arr[0]
  
    # Traverse array elements from second
    # and compare every element with 
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
  
# 2
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)

#3 function to rotate array 
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
 
 
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))

#4
#5 Python program to split array and move first part to end.
  
def splitArr(arr, n, k): 
    for i in range(0, k): 
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
          
        arr[n-1] = x
         
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
  
splitArr(arr, n, position)
  
for i in range(0, n): 
    print(arr[i], end = ' ')
    
#6 
from functools import reduce

def find_remainder(arr,n):

    sum1=reduce(lambda x,y: x*y,arr)

remainder= sum1 % n

print(remainder)

arr=[100,10,5,25,35,14]

n=11

find_remainder(arr,n)

#7 # Check if given array is Monotonic
def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

A = [6, 5, 4, 4]

print(isMonotonic(A))
