#declare a method for even numbers
#declaring for loop with range from (0,25) even numbers
# if condition num==num%2 is 0
#print if above condition is True
#call above method in order to execute printing even numbers

def printingevennumbers():
    for number in range(0,25):
        if 0 == (number%2):
            print("is True",number)

printingevennumbers()

