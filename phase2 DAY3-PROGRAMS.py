#ASCENDING ORDER INSERTION AND DELETION IN SLL:------

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            print("start:",end=' ')
            while temp:
                print(temp.data,end='->')
                temp=temp.next
            print(" end")
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        elif self.head.data >= new_node.data:
            new_node.next=self.head
            self.head=new_node
        else:
            #locate the node before insertion point
            temp=self.head
            while temp.next and new_node.data > temp.next.data:
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def delete(self,key):
        if self.head is None:
            print("List is empty")
        #if the key is in head
        if self.head.data==key:
            self.head=self.head.next
            return
        #find position of first occurence
        current=self.head
        while current:
            if current.data ==key:
                break
            else:
                previous = current
                current=current.next
        if current is None:
            print("key not found")
        else:
            previous.next=current.next
if __name__=='__main__':
    ll=sll() #obj creation
    print(' ')
    ll.insert(10)
    ll.insert(12)
    ll.insert(8)
    ll.insert(11)
    ll.insert(13)
    ll.display()
    print(' ')
    ll.delete(12)
    ll.delete(8)
    ll.delete(10)
    ll.display()
    print(' ')

#--------------------------------------------------------------------------------------------
#DELETION AT BEGINNING IN SLL:----

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def delete_begi(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
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
print("before deletion")
obj.display()
print('')
print("after deletion")
obj.delete_begi()
obj.display()



#--------------------------------------------------------------------------------------------------------------------
#DOUBLE LINKED LIST

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<->")
                temp=temp.next
l=dll()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
l.display()

#-------------------------------------------------------------------------------------------------------------------------------
#INSERTION AT BEGINNING IN DLL:---------

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self,data):
        new=Node(data)
        temp=self.head
        temp.prev=new
        new.next=temp
        self.head=new

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<->")
                temp=temp.next
l=dll()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
print("before insertion")
l.display()
print('')
print("after insertion")
l.insert_start(40)
l.display()


#-------------------------------------------------------------------------------------------------------------------------------
#INSERTION AT END IN DLL:----

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<->")
                temp=temp.next
l=dll()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
print("before insertion")
l.display()
print('')
print("after insertion")
l.insert_end(40)
l.display()

#-------------------------------------------------------------------------------------------------------------------------------
#INSERTION AT POSITION IN DLL:----

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_posi(self,data,pos):
        new=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new.prev=temp
        new.next=temp.next
        temp.next=new
        temp.next.prev=new
        

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<->")
                temp=temp.next
l=dll()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
print("before insertion")
l.display()
print('')
print("after insertion")
l.insert_posi(40,2)
l.display()

#----------------------------------------------------------------------------------------------------------------------
#DELETION AT BEGINNING IN DLL:----

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_begi(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<->")
                temp=temp.next
l=dll()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
print("before deletion")
l.display()
print('')
print("after deletion")
l.delete_begi()
l.display()

#----------------------------------------------------------------------------------------------------------------------
#DELETION AT END IN DLL:----

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None
        

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<->")
                temp=temp.next
l=dll()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
print("before deletion")
l.display()
print('')
print("after deletion")
l.delete_end()
l.display()

#----------------------------------------------------------------------------------------------------------------------
#DELETION AT POSITION IN DLL:----

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<->")
                temp=temp.next
l=dll()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
print("before deletion")
l.display()
print('')
print("after deletion")
l.delete_pos(1)
l.display()

#----------------------------------------------------------------------------------------------------------
#CIRCULAR LINKED LIST:------------

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Createlist:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head

    #Adding node at end of LL
    def add(self,data):
        newnode= Node(data)
        #is empty?
        if self.head.data is None:
            self.head=newnode
            self.tail=newnode
            newnode.next=self.head
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=self.head
    def display(self):
        current = self.head   
        if self.head is None:
            print("List is empty")
            return    
        else:
            print("Nodes of the circular linked list: ") 
        #Prints each node by incrementing pointer.    
            print(current.data)   
            while(current.next != self.head):
                current = current.next    
                print(current.data)    
     
     
class CircularLinkedList:    
  cl = Createlist();    
  #Adds data to the list    
  cl.add(1);    
  cl.add(2);    
  cl.add(3);    
  cl.add(4);    
  #Displays all the nodes present in the list    
  cl.display();    
        
        

    
        
            
            
            


    
        
            
            
            
