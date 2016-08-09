#called method and callingmethod

#formatting

#colon after loop/condition

#while loops untill condition is true and in condition we use variable and inside the loop we write a businesslogic to break the condition
    #and increment or decrement the variable used in the while condition

#stepbystep incremental programing

def callfun():
    print("ash")
    i=1
    while(i<=10):
        i=i+1
        print(i)


callfun()
    
def forloop():
    print("ashlee")
    for num in range(0,10):
        print(num)
    

forloop()

def list():
    print("tinko")
    list=["ash","ash1","ash3","ash4"]
    for abc in list:
        print(abc)
    

list()

variable=1

def global1():
    #global variable
    variable=2
print(variable ," is also a value")
print("variable")
print(variable ,"is a value")

global1()


temp="ash"

def Test():
    print(temp)
Test()

def test2():
    global temp
    temp="gulli"
    print(temp)
test2()
print(temp)

