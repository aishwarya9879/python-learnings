def div(num1,num2):
    return num1/num2

temp = div(1,2)
print(temp)

tempvalue = div(10,5)
print(tempvalue)

def operation(a,b,operation):
    
        
    if operation == "add":
            return a+b
    elif operation == "sub":
        return a-b
    elif operation == "mul":
        return a*b
    elif operation == "div":
        return a/b
    

temp = operation(1,2,"add")
print(temp)

temp1 = operation(10,5,"sub")
print(temp1)

temp2 = operation(1,2,"mul")
print(temp2)

temp3 = operation(1,2,"div")
print(temp3)





