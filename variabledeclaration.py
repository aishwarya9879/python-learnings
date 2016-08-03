""" A Functional Breakfast """

num ='2345'
name='aishwaryaadsfasdfasdfasdf'
fruits = ['banana', 'apple',  'mango', 'strawberry']

def test():
    print('2')
    print('3')
    print('4')
    print('5')
    print(num)

def getname():
    print(name)

def getcity():
    print('fremont')

def forloopsample():
    for letter in name:
        print(letter)

def array():
    print(fruits)
    print ('fruit',fruits[0])
    print('fruit',fruits[1])
    print('fruit',fruits[2])

def accessnameindex():
    print(name[0])

def forloopoverarrayfruits():
    for letter in fruits:
          print(letter)

    for letter in fruits[0]:
          print(letter)
    for letter in fruits[1]:
          print(letter)
    for letter in fruits[2]:
          print(letter)
    for letter in fruits[3]:
          print(letter)

          
for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print ('%d equals %d * %d'               % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print( num, 'is a prime number')




#Creating a variable to start the count
count = 0

#Creating while loop
while count < 6:
    print (count)
    count += 1



                    
    


   
               


    
#test()
#getname()
#getcity()
#forloopsample()
#array()
#accessnameindex()

forloopoverarrayfruits()




       

    
                                

        
    
