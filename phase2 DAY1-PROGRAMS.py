#prog1
l=[1,2,3]
r=list(map(lambda x:x+x,l))
print(r)

#prog2
l=[1,2,3]
r=list(map(lambda n:pow(n,2),l))
print(r)

#prog3
name="Mouni"
(lambda name:print(name))(name)

import math
l=[]
for i in range (1,15):
    if i%2==0:
        l.append(i)
r=list(map(lambda n:math.sqrt(n),l))
print(r)

#--------------------------------------------------------------------------------------
#sample prog for abstraction
from abc import ABC,abstractmethod
class abstractdemo(ABC):
    @abstractmethod #decorator to make the method abstract
    def display(self):
        None
    @abstractmethod
    def show(self):
        None

#----------------------------------------------------------------------------------------
#changing abstract to concrete
class demo(abstractdemo):
    def display(self):
        print("Abstraction method")
    def show(self):
        print("second function")
obj=demo()
obj.display()
obj.show()

#-------------------------------------------------------------------------------------
#sample prog for inheritance
class parent:
    def display(self):
        print("Parent class")
class child(parent):
    def show(self):
        print("Child class")
obj=child()
obj.display()
obj.show()

#-----------------------------------------------------------------------------------------
#sample prog for single inheritance
class A:
    n=30
class B(A):
    def calc(self):
        c=self.n*self.n
        print(c)
obj=B()
obj.calc()

#------------------------------------------------------------------------------------------------------
#sample prog for multiple inheritance 
class mom:
    def mdisplay(self):
        print("Mom class")
class daddy:
    def ddisplay(self):
        print("Daddy class")
class child(mom,daddy):
    def cdisplay(self):
        print("Child class")
obj=child()
obj.mdisplay()
obj.ddisplay()
obj.cdisplay()

#------------------------------------------------------------------------------------------
#Happy Number--> returns single digit that is 1.
               # 97=9^2+7^2=130=1^2+3^2+0^2=10=1^2+0^2=1
def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
            r=n%10
            s=s+r**2
            n=n//10
        return s
n=int(input("Enter a number:"))
res=n
while (res!=1 and res!=4):
    res=happy(res)
if res==1:
    print("Happy Number")
else:
    print("Not a happy number")



    










