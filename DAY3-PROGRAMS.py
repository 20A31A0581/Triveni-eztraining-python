#print the list elements one by one
l=list(input("Enter the 10 elements:").split(","))
print(l)
for i in l:
    print(i)

l=list(map(int,input("Enter the 10 elements:").split(",")))
print(l)
for i in l:
    print(i)

#print sum and avg of 5 float no's
l=list(map(float,input("Enter the 5 numbers:").split(",")))
print(l)
sum=0
for i in l:
    sum=sum+i
print(sum)
print(round(sum/len(l),2))

#extract even elements from the list
l=list(map(int,input("Enter the 6 numbers:").split(",")))
print(l)
l1=[]
for i in l:
    if(i%2==0):
        l1.append(i)
        i=i+1
print(l1)

#program to print the prod and sum based on given condition
l=list(map(int,input("Enter the numbers:").split(",")))
sum=0
prod=1
for i in l:
    sum=sum+i
    prod=prod*i
if prod<750:
    print("product=",prod)
else:
    print("sum=",sum)

#LIST COMPREHENSION
s=["water","werty","qwedfr","vbjh","sfcb"]
l=[]
for i in s:
    if "w" in i:
        l.append(i)
print(l)

s=["water","werty","qwedfr","vbjh","sfcb"]
l=[i for i in s if "w" in i]
print(l)
