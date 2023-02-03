#print 5 random numbers
import random
l1=[]
for i in range(0,5):
    n=random.randrange(1,100)
    l1.append(n)
print(l1)

#creating a dict from the list with random nos to the customer
import random
l=["sam","tri","dep","tubu","mouni"]
cust={names:random.randint(1,100) for names in l}
print(cust)

#ZIP FUNCTION---->creating a dictionary from 2 lists
l1=['a','b','c']
l2=[1,2,3]
d={a:b for (a,b) in zip(l1,l2)}
print(d)

###EXAMPLES###

#METHOD 1:-----
l1=["sam","tri","dep","tubu","mouni"]
l2=[149,312,378,449,500]
d={names:round((marks/500)*100,2) for (names,marks) in zip(l1,l2)}
print(d)

#METHOD 2:---
import random
l1=list(input("Enter the 5 student names:").split(","))
perc=[]
marks=[]
for i in range(len(l1)):
    n=random.randrange(300,500)
    marks.append(n)
    a=round((n/500)*100,2)
    perc.append(a)
print(marks)
print(perc)
d={names:percentage for (names,percentage) in zip(l1,perc)}
print(d)

####check the character is present in string or not
#METHOD 1:--
s=input("Enter the string:")
ch=input("Enter the character:")
if ch in s:
    print("yes")
else:
    print("no")

#METHOD 2:---
s=input("Enter the string:")
ch=input("Enter the character:")
a="yes" if ch in s else "no"
print(a)

#### check whether the given string is palindrome or not
s=input("enter the string:")
a=[x for x in s]
print(a)
print(a[::-1])
if a==a[::-1]:
    print("yes")
else:
    print("no")

### count the number of spaces
s=input("enter the string:")
count=0
if " " in s:
    print("yes")
else:
    print("no")
for i in s:
    if " " in i:
        count=count+1
print(count)

###Count the vowels in string
l=['a','e','i','o','u','A','E','I','O','U']
s=input("enter the string:")
count=0
for i in s:
    if i in l:
        count=count+1
print(count)

### print the neon numbers from the list----> 9*9=81-->8+1=9-->i.e., given number==sum of sq of that no.
import math
l=list(map(int,input("enter the number:").split(",")))
for i in l:
    sq=math.pow(i,2)
    sum=0
    while(sq>0):
        n=sq%10
        sum=sum+n
        sq=sq//10
    if sum==i:
        print(i,end=" ")
    


    
        
      
    
