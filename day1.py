
if 5 > 2:
    print("five is greater than two!")


# variables

x = 5.0
y = "hello, World"

print(type(x))
print(y)

x, y, z = "nakul","rahul","jadon"
print(x)
print(y)
print(z)

fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)


x = "awesome"

def nakul():
    print("python is " + x)
nakul()

x = str("hello world")

import random

print(random.randrange(1,10))

a = "Hello, World!"

print(a[0])

a = "hello, World!"

print(len(a))

txt = "my name is nakul"
if "rahul" not in txt:
    print("No, 'free' is present")

b = "nakulSingh"
print(b[0:5])


a = "Hello nakul singh jadon"
print(a.split("n"))

# replace()

price = 39
txt = f"my name is nakul and  {price} age"
print(txt)
# ===================================Operators======================>
a = 21
b = 10
c = 0

c = a + b
print ("a: {} b: {} a+b: {}".format(a,b,c))

c = a - b
print ("a: {} b: {} a-b: {}".format(a,b,c) )

c = a * b
print ("a: {} b: {} a*b: {}".format(a,b,c))

c = a / b
print ("a: {} b: {} a/b: {}".format(a,b,c))

c = a % b
print ("a: {} b: {} a%b: {}".format(a,b,c))

a = 2
b = 3
c = a**b 
print ("a: {} b: {} a**b: {}".format(a,b,c))

a = 10
b = 5
c = a//b 
print ("a: {} b: {} a//b: {}".format(a,b,c))



a = 21
b = 10
if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")

if ( a < b ):
   print ("Line 3 - a is less than b" )
else:
   print ("Line 3 - a is not less than b")

if ( a > b ):
   print ("Line 4 - a is greater than b")
else:
   print ("Line 4 - a is not greater than b")

a,b=b,a #values of a and b swapped. a becomes 10, b becomes 21

if ( a <= b ):
   print ("Line 5 - a is either less than or equal to  b")
else:
   print ("Line 5 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 6 - b is either greater than  or equal to b")
else:
   print ("Line 6 - b is neither greater than  nor equal to b")