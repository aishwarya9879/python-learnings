def getnumber():#  declaring a method
    return 1#returing a value

result =getnumber() # storing a functions return value in temp
print(result)      #printing the value of temp


def getresult(name):           #decaring a method with arguments with variable name name
    return name       #retuning a value tothe method with argument "ashgulli"

output = getresult("ash")      #calling a function with argument value 
print(output)

#printing a value of temp variable


output = getresult("gulli")      #calling a function with argument value 
print(output) 


def getname(person1,person2):
    print(person1 ,"-----" ,person2)
    return person1+person2

out= getname("a","g")
print(out)

str =getname("prasad","ashlee")
print(str)


def getpetname(one,two):
    print(one,"---" ,two)
    returnone+two

out = getname("ash","gulli")
print(out)

out = getname("tinko","bujii")
print(out)
