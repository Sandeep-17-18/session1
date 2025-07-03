a=10
b=8
c=6
#arithmetic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print("--------")
#relational operators
print(a>b)
print(a<b)
print(a!=b)
print(a==b)
print(a>=b)
print(a<=b)
print("--------")
#logical operators
print(a>b and b==a)
print(a>=b or a<=c)
print(not a>b)
print("--------")
print(bin(7))
print("--------")
#bitwise operators
print(a & b)
print(a | b)
print(a ^ b)
print("--------")
#assignment operator
b+=4
c-=2
a*=3
print(a)
print(b)
print(c)
print("--------")
#conditional statements
a=57
if(a%2==0):
    print("even")
else:
    print("odd")
print("--------")
d=90
if(d%5==0 and d%3==0):
      print(d ,"is multiple of 5 and 3")
elif(d%5==0):
    print(d ,"is multiple of 5")
elif(d%3==0):
    print(d, "is multiple of 3")
else:
    print("no multiple")
print("--------")
#iterative statements
for i in range(10,-1,-2):
    print(i)
    

