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
print(bin(7))
#bitwise operators
print(a&b)
print(a|b)
print(a^b)
#assignment operators
a+=3
b-=6
c*=2
print(a)
print(b)
print(c)
#conditional statements
a=int(input("enter a num:"))
if(a%5==0 & a%3==0):
    print(a," is multiples of both 3 and 5")
elif(a%5==0):
    print(a ,"is multiple of 5")
elif(a%3==0):
    print(a,"is multiple of 3")
else:
    print(a,"is not multiple of 3 & 5") 