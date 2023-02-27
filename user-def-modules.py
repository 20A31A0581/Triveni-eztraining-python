'''import function
function.printing()
print(__name__)'''

#-------------------------------------------------------------------------------------
print("before function")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
if __name__=='__main__':
    f1()
    f2()
    f3()
print("name:",__name__)
    
