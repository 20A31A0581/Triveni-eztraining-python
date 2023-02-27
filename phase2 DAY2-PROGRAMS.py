#PROTECTED---> variables that are declared are only accesible to that class
              #(single _ is used as protected variables)
class encap:
    _a=10
    b=20
    def encapfunc(self):
        _c=30
        print("Encap function-accessing protected")
        print(self._a+10)
        print(_c+10)
obj=encap()
print(obj._a)
obj.encapfunc()
print(obj.b)
print(obj._c)  #it will throw error bcoz function variables cannot accesed at outside

#----------------------------------------------------------------------------------------------
#PRIVATE ---> variables that are declared are accesible
             #with in the class only (double __ is used as private variables)

class encap:
    __a=10
    print(__a)
    def encapsulation(self):
        print('encap function')
        print(self.__a)
obj=encap()
obj.encapsulation()
print(obj.__a) # it will throw an error bcoz a is private only accesed within the class

#---------------------------------------------------------------------------------------------------
#PARENT AND CHILD CLASS EXAMPLE:--

class parent:
    def __init__(self):
        self.value="Inside parent"
    #parents show method
    def show(self):
        print(self.value)

#defining child class
class child(parent):
    def __init__(self):
        self.value="inside child"
    #childs show method
    def show(self):
        print(self.value)
obj1=parent()
obj2=child()
obj1.show()
obj2.show()
    
#--------------------------------------------------------------------------------------------
#METHOD OVERLOADING
class overload:
    def display(self,a=None,b=None):
        print(a,b)
obj=overload()
print("Without arguments")
obj.display()
print("With all arguments")
obj.display(10,20)
print("With one arguments")
obj.display(10)

#----------------------------------------------------------------------------------------------
#EXAMPLE:----
class vjy:
    def place(self):
        print("vijayawada")
    def stu(self):
        print("yes-vjy-student")
    def year(self):
        print("3rd year")
class hyd:
    def place(self):
        print("hyderabad")
    def stu(self):
        print("yes-hyd-student")
    def year(self):
        print("2nd year")
obj1=vjy()
obj2=hyd()
for details in (obj1,obj2):
    details.place()
    details.stu()
    details.year()

#----------------------------------------------------------------------------------------------------
#program to create a single linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
obj.display()

#---------------------------------------------------------------------------------------------------------------
#ANOTHER EXAMPLE

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="")
                temp=temp.next
obj=singlelinkedlist()
n=Node('w')
obj.head=n
n1=Node('i')
n.next=n1
n2=Node('n')
n1.next=n2
n3=Node('n')
n2.next=n3
n4=Node('e')
n3.next=n4
n5=Node('r')
n4.next=n5
obj.display()

#----------------------------------------------------------------------------------------------------------
#INSERT AT BEGINNING IN SINGLE LINKED LIST

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbegi(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=sll()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
print("Before inserting")
obj.display()
print('')
print("After inserting")
obj.insertatbegi(100)
obj.display()

#-----------------------------------------------------------------------------------------------------------------------
#INSERT AT END IN SINGLE LINKED LIST

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        new=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=sll()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
print("Before inserting")
obj.display()
print('')
print("After inserting")
obj.insertatend(100)
obj.display()

#----------------------------------------------------------------------------------------------------------------
#INSERT AT POSITION IN SLL (WITH WHILE LOOP)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatposi(self,data,pos):
        new=Node(data)
        temp=self.head
        count=1
        while temp.next:
            temp=temp.next
            count=count+1
            if count==pos:
                new.next=temp.next
                temp.next=new 
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=sll()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
print("Before inserting")
obj.display()
print('')
print("After inserting")
obj.insertatposi(100,2) #position counting starts from 0
obj.display()

#----------------------------------------------------------------------------------------------------------------------
#INSERT AT POSITION IN SLL (WITH FOR LOOP)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatposi(self,data,pos):
        new=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new.next=temp.next
        temp.next=new 
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=sll()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
print("Before inserting")
obj.display()
print('')
print("After inserting")
obj.insertatposi(100,2) #position counting starts from 0
obj.display()'''

            
    

