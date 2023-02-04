####function without argument without return value
def sample(): #definition or description(called function)
    print("hello")
    print("good day!")
sample() #calling function
print("again")
sample()

#OUTPUT:--
hello
good day!
again
hello
good day!

def add():
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    n3=int(input("Enter n3:"))
    s=n1+n2+n3
    print(s)
add()  ##if we write the print(s) after the add() it returns nameerror: that s is not defined

#output:--
Enter n1:2
Enter n2:3
Enter n3:4
9   

####function without argument with return value
def add():
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    n3=int(input("Enter n3:"))
    s=n1+n2+n3
    return s
A=add()
print(A)

#OUTPUT:---
Enter n1:2
Enter n2:3
Enter n3:4
9

####function with argument without return value
#STATIC INPUT
def add(n1,n2,n3):
    s=n1+n2+n3
    print("sum=",s)
add(2,3,4)
#OUTPUT:--
sum= 9

#USER INPUT or DYNAMIC INPUT (same variables)
def add(n1,n2,n3):
    s=n1+n2+n3
    print("sum=",s)
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
n3=int(input("Enter n3:"))
add(n1,n2,n3)
#OUTPUT:--
Enter n1:2
Enter n2:3
Enter n3:4
sum= 9

#USER INPUT or DYNAMIC INPUT (different variables)
def add(n1,n2,n3):
    s=n1+n2+n3
    print("sum=",s)
a=int(input("Enter n1:"))
b=int(input("Enter n2:"))
c=int(input("Enter n3:"))
add(a,b,c)
#OUTPUT:---
Enter n1:2
Enter n2:23
Enter n3:34
sum= 59

####function with argument with return value
#STATIC INPUT
def add(n1,n2,n3):
    s=n1+n2+n3
    return s
A=add(2,3,4)
print("sum=",A)
#OUTPUT:--
sum= 9

#USER INPUT or DYNAMIC INPUT (same variables)
def add(n1,n2,n3):
    s=n1+n2+n3
    return s
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
n3=int(input("Enter n3:"))
A=add(n1,n2,n3)
print("sum=",A)
#OUTPUT:--
Enter n1:2
Enter n2:3
Enter n3:4
sum= 9

##program using type1: lemons excess or need more
def lemons():
    n=int(input("enter how many u have:"))
    a=int(input("enter how many lemons want:"))
    if n==a:
       print("sufficient")
    elif n>a:
        n1=n-a
        print("u have",n1,"excess lemons")
    else:
        n2=a-n
        print("u need",n2,"lemons")
lemons()'''

'''## program using type 2: factors of a number
def fac():
    n=int(input("enter a number:"))
    l=[]
    if n>=0:
        for i in range(1,n+1):
            if n%i==0:
                l.append(i)
        return l
    else:
        return "not possible"
        
fact=fac()
print(fact)

##using type 3: program to find the multiplication table of a given number
def mul(n):
    for i in range(1,11):
        print(n,"*",i,"=",(n*i))
n=int(input("enter a number:"))
mul(n)

#using type 4: to find the sum of digits of a number
def add_dig(n):
    sum=0
    while n>0:
        sum=sum+n%10
        n=n//10
    return sum
n=int(input("enter a number:"))
A=add_dig(n)
print("sum of the digits:",A)

#sum the list of numbers 
def add(l):
    sum=0
    for i in l:
        sum=sum+i
    return sum
l=list(map(int,input("enter the numbers:").split(",")))
A=add(l)
print(A)

##RECUSIVE FUNCTION EXAMPLE
def display():
    n=int(input("enter the number:"))
    if n==1:
        display()
    else:
        print("over")
display()

#FACTORIAL OF A NUMBER(with recursion)
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number:"))
print("factorial is ",fact(n))

#FACTORIAL OF A NUMBER(without recursion)
def fact(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac
n=int(input("enter a number:"))
res=fact(n)
print("factorial is ",fact(n))

##FIBONACCI SERIES
#USING WHILE LOOP
n=int(input("enter how many numbers want:"))
n1,n2=0,1
count=3
if n<0:
    print("not possible")
elif n==1 or n==0:
    print("fibonacci:",n1)
else:
    print("fibonacci:",n1,n2,end=" ")
    while count<=n:
        n3=n1+n2
        n1=n2
        n2=n3
        count=count+1
        print(n3,end=" ")

#USING FOR LOOP
n=int(input("enter how many numbers want:"))
n1,n2=0,1
if n<0:
    print("not possible")
elif n==1 or n==0:
    print("fibonacci:",n1)
else:
    print("fibonacci:",end=" ")
    for i in range(0,n):
        print(n1,end=" ")
        n3=n1+n2
        n1=n2
        n2=n3

#USING RECURSION FUNCTION
def fib(n):
    if n<=0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter how many numbers want:"))
for i in range(0,n):
    print(fib(i),end=" ")

#FUNCTION RETURNS MORE VALUES
#addition and subtraction of 2 nums in one func
def add_sub(x,y):
    add=x+y
    sub=x-y
    return add,sub
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
res1,res2=add_sub(n1,n2)
print("add=",res1)
print("sub=",res2)

    

    

        

    
    



