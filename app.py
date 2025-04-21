"""values = {'a':11,'b':22,'c':33}

values['a'],values['b'],values['c'] = values['c'],values['b'],values['a']

print(values)

squares = [x**2 for x in range(1,11+1) if x%2!=0]

print(squares)


#nivens/harshd no
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


#Strong no or krishnamurty no
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
    print("weak")"""































