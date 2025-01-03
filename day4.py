#///////////////////////////classess and object========================>
class Student:

    collage_name = "poornima group of institutions"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def hello(self):

        print("wellcome student")
    


s1 = Student("karan",97)
print(s1.name)

print(s1.marks)
s2 = Student("ravi",98)
print(s2.name)
print(Student.collage_name)
print(s2.marks)
s1 = [1,4,6,9]
for i in range(len(s1)):
    print(s1[i])
s1 = [1,2,3,45,6]
for i in range(len(s1)):
    print(s1[i])

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("nakul",36)

print(p1.name)
print(p1.age)

class Vehicle:
    def __init__(self, max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def name(self):
        print("Marks")
        print(self.marks)

    def get_marks(self,marks):
        self.marks = marks
        
        



modelX = Vehicle(240,19)

print(modelX.max_speed,modelX.mileage)

modelX.get_marks(123)
modelX.name()

a = " Hello, World "
print(a.split(","))

age = 36

txt = f"my name is nakul {age}"

print(txt)

thislist = ["apple", "banana", "cherry"]
del thislist


thislist = list(("apple","name","rahul"))

thislist = [4,6,8,2,6,8]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1

number = int(input("enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")   

name = "anshika"
x = name[-1:-5]
print(x)

user_input = input("Enter a list of nubers seprated by spaces: ")

numbers =list(map(int,input().split()))

even_sum = 0

for num in numbers:
    if num%2 == 0:
        even_sum += num
print(f"the sum of all even numbers in the list is: {even_sum}")

# Create student class that takes name & marks of 3 subject as argument in constructor.
# then  create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def name():
        print("jadon")

    def get_avg(self):
        sum = 0 
        for val in self.marks: 
            sum += val 
        print("hii",self.name, "your avg score is:",sum/3)   

s1 = Student("Nakul",[99,98,97])

s1.get_avg()
s1.name