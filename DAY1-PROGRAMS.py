#writing our names in telugu format
print(chr(3108)+chr(3149)+chr(3120)+chr(3135)+chr(3125)+chr(3143)+chr(3107)+chr(3135))
print(chr(3120)+chr(3143)+chr(3127)+chr(3149)+chr(3118)+chr(3134))
print(chr(3088)+chr(3126)+chr(3149)+chr(3125)+chr(3120)+chr(3149)+chr(3119))
print(chr(3117)+chr(3120)+chr(3110)+chr(3149)+chr(3125)+chr(3134)+chr(3097)+chr(3149))

#program 1
i1=int(input("Enter first integer:"))
i2=int(input("Enter second integer:"))
i3=int(input("Enter third integer:"))
f1=float(input("Enter first float:"))
f2=float(input("Enter second float:"))
f3=float(input("Enter third float:"))
s1=str(input("Enter first string:"))
s2=str(input("Enter second string:"))
c1=complex(input("Enter complex number:"))
print()   #gives the blank line
print("First integer:",i1)
print("Second integer:",i2)
print("Third integer:",i3)
print()
print("First float:",f1)
print("Second float:",f2)
print("Third float:",f3)
print()
print("First string:",s1)
print("Second string:",s2)
print()
print("Complex number:",c1)

#program2
kc1=75
sc=kc1/2
kc2=sc/2
print("the amount of candy kumar has:",sc+kc2)
print()

#program3
n1=36.32*3
n2=n1+56.19
n3=n2-10
print("final val:",n3)
print()

#program4
num1=10
num2=-3.5
num3=num1*num2
print("final result:",num3)
print()
print(4*(-53.0))
print()

#operators example
a=10
b=2
print(a/b)
print(a//b)
print(a%b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
print()
print(10<3 and 10>4)
print(10<3 or 10>4)
print(not(10>4))
print()


#multiple inputs in single line
n1,n2=int(input("enter:")),int(input("enter:"))
print(n1)
print(n2)
s=n1+n2
print(s)

n1,n2=int(input("enter:")),int(input("enter:"))
print(n1,n2)

n1,n2=input("enter:").split()
print(n1)
print(type(n1))
print(n2)
print(n1+n2)

n1,n2=map(int,input("enter:").split())
print(n1,n2)

#swap using temp
n1,n2=input("enter:").split()
print(n1,n2)
temp=n1
n1=n2
n2=temp
print(n1,n2)

#swap without temp
n1,n2=map(int,input("enter:").split())
print(type(n1))
print(type(n2))
print(n1,n2)
n1=n1+n2
n2=n1-n2
n1=n1-n2
print(n1,n2)

n1,n2=map(int,input("enter:").split())
print(n1,n2)
n1=n1*n2
n2=n1/n2
n1=n1/n2
print(int(n1),int(n2))

#area of rectangle
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
A=l*b
print("area:",A)

#perimeter of rectangle
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
P=2*l+b
print("perimeter:",P)









                           


      



