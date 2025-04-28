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
print(e(4))"""










































































