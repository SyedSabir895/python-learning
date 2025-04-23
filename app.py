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
print(pair)"""































