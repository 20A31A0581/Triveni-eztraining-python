import time
def timer(t):
    while t:
        mins,secs=divmod(t,60)
        tim=("{:02d}:{:02d}".format(mins,secs))
        print(tim)
        time.sleep(1)
        t=t-1
    print("finished")
t=int(input("Enter the time in seconds:"))
timer(t)
    
