'''#Exception prog 1:----
a=100
b=0
try:
    print(a/b)
except Exception as e:
    print("please note: number cant be divided by zero:",e)
print("End of the code")

#Exception prog 2:---
a=100
b=0
try:
    print(a/b)
except ZeroDivisionError as e:
    print("please note: number cant be divided by zero:",e)

#finally prog:---
a=100
b=0
try:
    print(a/b)
except Exception as e:
    print("please note: number cant be divided by zero:",e)
finally:
    print("end of the block")

#muliple except blocks
a=int(input("enter a:"))
try:
    b=int(input("enter b:"))
    print(a/b)
except ZeroDivisionError as e:
    print("please note: number cant be divided by zero:",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:# other errors
    print("other error",e)
finally:
    print("end of the code")

#user defined exception--->raise
x=int(input("enter a number:"))
if x%2!=0:
    raise Exception("x should be even number")
else:
    print("x is even number...correct")

##class and object example:---
class laptop:
    def config(self):  ##func inside the class called as "method"
        print("yes")
lenova=laptop()  ##object 1
lenova.config() 
dell=laptop()  ##object 2
dell.config()

##init example:--
##init function is constructor
class employee():
    def __init__(self,name,id):  ##func inside the class called as "method"
        self.name=name
        self.id=id
    def display(self):
        print("id:",self.id,"\nname:",self.name)
emp1=employee("ram",101)  ##object 1
emp1.display() 
emp2=employee("raju",102)  ##object 2
emp2.display() '''

#--------------------------------------------------------------------------------------------------
class computer():
    a=100 ##here a and b are instance variables
    b=200
    print("the variable inside the class:",a,b)
    def config(self):
        c=300
        print("the variable inside the method:",c)
        print("the variable inside the class:",self.b)
lenova=computer()
dell=computer()
print(lenova.a)
dell.config()


        
    

