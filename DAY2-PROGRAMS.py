#bitwise example program
n1,n2=map(int,input("enter:").split())
if n1 and n2 < 15:
    print(n1&n2)
    print(n1|n2)
    print(n1^n2)
else:
    print("input exceeds 15")

#multiple inputs in single line
n=int(input("size:"))
a=list(map(int,input("enter:").strip().split()))[:n]
print(a)

#product of 10 no's
n=int(input("size:"))
a=list(map(int,input("enter:").split()))[:n]
res=1
for i in a:
    res=res*i
print(res)

#example
print("its","a" ,"good","day")
print("its" ,"good","day")

#END example  
print("its","a" ,"good","day",end=' ')
print("its" ,"good","day")

#SEP example
print("its","a" ,"good","day",sep='')

print("its","a" ,"good","day",sep=' ')

print("its","a" ,"good","day",sep='*')

#upside down filled triangle
print(" * * * * *")
print("  * * * *")
print("   * * *")
print("    * *")
print("     *")

#heart
print("    *   *")
print("  *   *   *")
print("*           *")
print("  *       *")
print("    *   *")
print("      *")

#conditional statements example
# program to find the tempereature
temp=int(input("enter the temperature:"))
if(temp>45):
    print("Hottesr")
elif(temp>40 and temp<=45):
    print("Hot")
elif(temp>25 and temp<=40):
    print("Moderate")
elif(temp>10 and temp<=25):
    print("cold")
else:
    print("Chill")

#check whether 500 or not
n=int(input("enter a number:"))
if n==500:
    print("n is 500")
else:
    print("n is not 500")

#find even positive,even negative,odd positive and odd negative
n=int(input("enter a number:"))
if n%2==0:
    if n>0:
        print(n,"is Even-Positive")
    else:
        print(n," is Even-Negative")
else:
    if n>0:
        print(n,"is Odd-Positive")
    else:
        print(n,"is Odd-Negative")

#greatest number among 2 numbers 
n1,n2=map(int,input("enter the two numbers:").split())
if n1==n2:
    print(n1,"and",n2,"are same")
elif n1>n2:
    print(n1,"is biggest number")
else:
    print(n2,"is biggest number")

#find float or integer
#1
n=12.7
if isinstance(n,int)==True:
    print(n,"is integer")
else:
    print(n,"is float")
#2
n=input("enter a number:")
if "." in n:
    print(n,"is float")
else:
    print(n,"is integer")
    
#greatest number among 3 numbers 
n1,n2,n3=map(int,input("enter the three numbers:").split())
if n1>n2 and n1>n3:
    print(n1," is greatest number")
elif n2>n1 and n2>n3:
    print(n2,"is greatest number")
else:
    print(n3,"is greatest number")

#check whether divisible by 11 or not 
n=int(input("enter a number:"))
if n%11==0:
     print(n,"is  divisible by 11")
else:
    print(n,"is not divisible by 11")

#check whether divisible by both 2 and 5 
n=int(input("enter a number:"))
if n%2==0 and n%5==0:
     print(n,"is  divisible by both 2 and 5")
else:
    print(n,"is not divisible by both 2 and 5")
#----------------------------------------------------------------
#WHILE LOOP EXAMPLE
n=1
while n<=10:
    print(n,end=' ')
    n+=1

#print even numbers btw 2 to 20
n=2
while n<=20:
    if n%2==0:
        print(n,end=' ')
    n+=1

#print odd numbers btw 1 to 30
n=1
while n<=30:
    if n%2!=0:
        print(n,end=' ')
    n+=1

#first 20 even numbers
n=20
i=1
while i<=2*n:
    if i%2==0:
        print(i,end=' ')
    i+=1
    
#------------------------------------------------------------------------
#FOR LOOP EXAMPLE
for i in range(1,11):
    print(i,end=' ')
print()

#print even numbers btw 2 to 20
for i in range(2,21,2):
    print(i,end=' ')
print()
for i in range(2,21):
    if i%2==0:
        print(i,end=' ')

#first 20 even numbers
n=20
for i in range(1,2*n+1):
    if i%2==0:
        print(i,end=' ')

#------------------------------------------------------------------------------
#GUESS THE RANDOM NUMBER
import random
n=random.randrange(1,10)
guess=int(input("enter the number:"))
while n!=guess:
    if n>guess:
        print("too low!")
        guess=int(input("enter the number:"))
    else:
        print("too high")
        guess=int(input("enter the number:"))
while n==guess:
    print("guess correctly")
    break
        

    


    
    
    

    
    

