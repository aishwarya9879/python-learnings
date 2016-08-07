var1=1
print("line1print value:",var1)

def test1():
        
        global var1
        var1=20
        print(var1)
       

print("line9print value:",var1)

test1()
print("line7print value:",var1)
