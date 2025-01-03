
import array as arr

a = arr.array('i', [1, 2, 3])
print (type(a), a)


a = arr.array('u', 'BAT')
print (type(a), a)


a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)


import array as arr

# creating array
a = arr.array('i', [1, 2, 3])

# iterating and printing each item
for i in range(0, 3):
    print(a[i], end=" ")

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


greet_user = lambda name : print("Hey there ," ,name)

greet_user('Nakul')