"""values = {'a':11,'b':22,'c':33}

values['a'],values['b'],values['c'] = values['c'],values['b'],values['a']

print(values)

squares = [x**2 for x in range(1,11+1) if x%2!=0]

print(squares)


#nivens/harshd no the no should be equal to 0 when it is divided by the addition of the sum of the digits of the no
n = int(input())
copy = n
s = 0
while n>0:
    d = n%10
    s+=d
    n = n//10
if copy%s==0:
    print("k")
else:
    print("n")


#Strong no or krishnamurty no the sum of the factorials of the digits of the no should be equal to the no 
n = int(input())
copy = n
s = 0
while n>0:
    d = n%10
    f = 1
    for i in range(1,d+1):
        f*= i
    s+=f
    n//=10
if s==copy:
    print("strong")
else:
    print("weak")



words = ['apple','kiwi','banana']
upp = [word.upper() for word in words]
print(upp)

#nested list comprehensions on 2d matrix to flatten
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in matrix for num in row]
print(flat)

#using logical condition,replace all the -ve no's with zero's
nums = [-2,-1,0,1,2]
nonneg = [x if x>=0 else 0  for x in nums]
print(nonneg)


#finding index
words = ['apple','kiwi','banana']
fc = [word[3] for word in words]
print(fc)

#finding length
words = ['apple','kiwi','banana']
l = [len(word) for word in words]
print(l)

#filtering None values
items = [1,None,2,None,3,4,5,]
valid = [x for x in items if x is not None]
print(valid)


names = ['Vijay','Mark']
ages = [45,69]
pair = [(name,age) for name in names for age in ages]
print(pair)

#given a string, create a list of all vowels in the string using list comprehension
text = "hello students"
v = [char for char in text if char.lower() in 'aeiou']
print(v)


#matrix
size = int(input())
for i in range(size):
    for j in range(size):
        if i==j or j==0 or i==size-1:
            print('^',end=" ")
        else:
            print(' ',end=" ")
    print()



#floyd traingle
rows = 5
num = 1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()



rows = 5
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end=" ")
    for k in range(2*i +1):
        print("!",end=' ')
    print()


#pascal's triangle
rows  =5
num = 1
for i in range(rows):
    num=1
    for j in range(rows-i-1):
        print(" ",end=' ')
    for k in range(i+1):
        print(num,end=' ')
        num = num*(i-k)//(k+1)
    print()





alpha = [chr(i) for i in range (ord('a'),ord('z')+1)]
alpha.sort()
print(" ".join(alpha))

#spiral pattern

n=4
matrix= [[0] *n for _ in range(n)]
num=1
top= 0
bottom= n-1
left= 0
right= n-1
while top<=bottom and left <=right:
    for i in range(left, right+1):
        matrix[top][i]= num
        num+=1
    top +=1
    for i in range(top, bottom+1):
        matrix[i][right]= num
        num+=1
    right -=1
    for i in range( right, left-1, -1):
        matrix[bottom][i]= num
        num+=1
    bottom -=1
    for i in range(bottom, top-1, -1):
        matrix[i][left]= num
        num+=1
    left +=1
for row in matrix:
    for val in row:
        print(f"{val:2}", end=' ')
    print()

#function with default parameters

def sample(x,y=1):
    return x*y
print(sample(2))
print(sample(2,3))



#function with keyword arguments
def result(*args):
    return sum(args)
print(result(1,2,3))
print(result(11,22,33,44))


def info(**kwargs):

    for key,value in kwargs.items():
        print(f"{key} : {value}")
info(name="Sabir",age=69,city="Vijayawada")


#lambda func
sq = lambda x:x*x
print(sq(5))
add = lambda x,y: x+y
print(add(3,6))


def allnum(n):
    return min(n),max(n), sum(n)/len(n)
min_val,max_val,avg = allnum([1,2,3,4,5])
print(f"Min: {min_val},Max:{max_val},Avg:{avg}")


def e(n):
    if n==0:
        return True
    return o(n-1)

def o(n):
    if n==0:
        return False
    return e(n-1)
print(e(4))


#power tower of hanoi

def pt(a,n):
    if n==1:
        return a
    return a**pt(a,n-1)


print(pt(2,2))
print(pt(3,3))

#python data structures array opreations
#program to construct a list arr=[10,20,30,40] and perform insert operation and division opertion with 50 and 25 at position 2 respectively delete 30 and traverse the array to fetch a number 25 is present or not.

arr = [10,20,30,40]
#insert
arr.append(50)   #adds at the last of the array 
arr.insert(2, 25)
for i in arr:
    print(i,end=" ")

#deletion
arr.remove(30)
arr.pop()   # removes te last element of the array
print(arr)

#traversal   will print all the elements which are in the array

for i in arr:
    print(i,end=" ")

#searching
print("\n 25 in array? ",25 in arr)


#program to check whether the given string is palindrome or not and count the palindromic characters which are repeated
text = 'madam'
if text == text[::-1]:
    print("True")
else:
    print("False")
 

freq = {}
for ch in text:
    freq[ch] = freq.get(ch,0)+1
print(freq)


#searchings
linear search : in sorted or unsorted arrays
1.arr of list of size n
2.key for search element
3.start with zero index
4.compare arr[i] == key
arr[i] = key return index
else not(move to next index)
5.repeat same steps till n-1
6.if no match return -1


binary search 
sentinel search
fibonaci search
interpolation search




def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
size = int(input("Enter the size: "))
arr = []
print("Enter the elements: ")
for i in range(size):
    num = int(input(f"Element {i+1}:"))
    arr.append(num)
key = int(input("Enter the key: "))
result = linear_search(arr,key)
if result != -1:
    print(f"\n element {key} found at {result}")
else:
    print("element not found")




#binary search:
1.array must be sorted
2.array is divided into two seperate equivalent halfs
set low & high 0->-1
condition low<=high
mid = low+high//2
arr[mid] == key return mid
arr[mid] <key low mid+1
arr[mid] > key high mid+1
not found return -1

def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            low = mid+1
        else:
            high = mid - 1
    return -1

size = int(input("Enter the size"))
arr = []
print("Enter the elements: ")
for i in range(size):
    num = int(input(f"Element {i+1}:"))
    arr.append(num)
key = int(input("Enter the key: "))
result = binary_search(arr,key)
if result != -1:
    print(f"\n element {key} found at {result}")
else:
    print("element not found")



#jump search
import math
def jump_search(arr,target):
    if not arr:
        return -1
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[prev]<target:
        prev +=step
    for i in range(max(0,prev-step),min(n,prev+1)):
        if arr[i] == target:
            return i
    return -1
arr = [1,3,4,7,9,11,22,25]

target = 4

result = jump_search(arr,target)
print(result)


#exponential search
def bsearch_range(arr,target,left,right):
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] <target:
            left = mid+1
        else:
            right = mid-1
    return -1
def expo_search(arr,target):
    if not arr:
        return -1
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i<n and arr[i]<=target:
        i *=2
    return bsearch_range(arr,target,i//2,min(i,n-1))
arr = [2,4,6,8,10,12,14,16]
target = 14
result = expo_search(arr,target)
print(f"Element {target} found at index:{result}")

#fibonaci search

def fibsearch(arr, target):
    if not arr:
        return -1

    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    # Find the smallest Fibonacci number >= n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    # Final check for last element
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1

# Test
arr = [2, 4, 6, 8, 10, 12, 13]
target = 10
result = fibsearch(arr, target)
print(f"Element {target} found at index: {result}")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
size = int(input())
arr = []
print("Enter the elements: ")
for _ in range(size):
    arr.append(int(input()))
print("Original list: ",arr)
bubble_sort(arr)
print("BubbleSorted: ",arr)



def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0]*(max_val+1)
    #freq
    for num in arr:
        count[num]+=1
    #count
    for i in range(1,len(count)):
        count[i]+= count[i-1]
    output = [0] * len(arr)
    #stable sort
    for num in reversed(arr):
        output[count[num]-1] = num
        count[num] -=1
    #coping sorted list
    for i in range(len(arr)):
        arr[i] = output[i]
arr = [4,2,2,8,9,3,2,1,6,5,3]
print("Before Sorting: ",arr)
counting_sort(arr)
print("After Sorting: ",arr)

def count_sort(arr,exp):
    n = len(arr)
    output = [0]*n
    count = [0] * 10 #for digits 0 to 9
    for i in range(n): #frequencies of units position of numbers
        index = (arr[i]//exp)%10
        count[index]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i = n-1
    while i>=0:
        index = (arr[i]//exp)%10
        output[count[index]-1] = arr[i]
        count[index] -=1
        i -=1
    
    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp>0:
        count_sort(arr,exp)
        exp *=10
arr = [170,45,75,90,802,24,2,66]
print("Before sort ",arr)
radix_sort(arr)
print("After sort",arr)

#pancake sort


def flip(arr,k):
    return arr[:k+1][::-1]+ arr[k+1:]
def pancake(arr):
    n = len(arr)
    for size in range(n,1,-1):
        max_index = arr.index(max(arr[:size]))
        if max_index != size-1:
            if max_index !=0:
                arr = flip(arr,max_index)
                print(f"Flip at {max_index+1}: {arr}")
            arr = flip(arr,size-1)
            print(f"Flip at {size}: {arr}")
    return arr
nums = list(map(int,input("enter").split()))
sorted_nums = pancake(nums)
print("Sorted",sorted_nums)"""











































































