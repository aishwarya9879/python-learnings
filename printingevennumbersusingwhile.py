
#declare a method for even numbers
# initialize number with 0
#write a while loop and check the condition 25 >number
#if condition num==num%2 is 0
#when the condition is true iterate the sequence and print the incremented number
#increment the number using c
#while should execute until false number==25(see number 3 point)
#call above method in order to execute printing even numbers

def printingevennumber():
    number=0

    while  (number<25):
        number= number+1
        if 0==number%2:
            print("even number",number)

            
 

printingevennumber()


#Indentation
# What is Indentation?
# Indentation is to make statements belong to a method or if condition or loops

# How to delcare indentation?
# Use a tab right after next line in the same column and start the line of instruction. So, that the
#instruction belongs to above line loop/method/ifcondition.


# What are advantages of indentation in PYTHON?
# In programming like C, Java, C++ ..developers use { , } (curly braces) to start a method and end a method or to
#start a if condition, end if condition or to start a loop(while,dowhile, for) or end the loop.
# But, here in python we will give indentation....instead of CURLY braces..So python executor will identify
# if the instrctions belong to method/loop/if conditions......


