#===============================================Abstraction==================================>

class Car:
    def __init__(self):
        self.acc =  False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch   = True
        self.acc =  True
         
        print("car started")
        
        
car1 = Car()
car1.start()
===========================debit credit and total balance example=================>

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self , ammount):
        self.balance -= ammount
        print("Rs",ammount,"was debited")
        print("total balance = ", self.get_balance())

    def credited(self , ammount):
        self.balance += ammount
        print("Rs",ammount,"was credited") 
        print("total balance = ", self.get_balance()) 

    def get_balance(self):
        return self.balance     


acc1 = Account(10000,1234)
acc1.debit(1000)
acc1.credited(2000) 

class Person:
    __name = "anonymous"
    def __Hello(self):
        print("Nakul")

    def welcome(self):
        self.__Hello() 
p1 = Person()
print(p1.welcome())

====================================Inheritance==================>\
====================Single Inheritance
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("Car stop..") 

class ToyotaCar(Car): 
    def __init__(self,name):
        self.name = name        


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("Prius")

print(car1.start())

=================Multilevel Inheritance

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("Car stop..") 

class ToyotaCar(Car): 
    def __init__(self,brand):
        self.brand = brand 

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel") 
car1.stop()        

====================Multiple Inheritance 
  

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B" 

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varB)
print(c1.varC)
print(c1.varA)    

===================================Practice Questions==========================>

a = 33
b = 33

if a > b:
    print("yes")
else:
    print("No")

for i in range(1,11):
    print(i)
for i in range(1,21,2):
    print(i)  

for i in range(20,0,-2):
    print(i)

num = int(input("Enter any number"))
for i in range(1,11):
   print(num*i) 

x ="nakul singh ...."
y=x.replace("....", ".1..")
print(y)
x.append(y)
print(x)