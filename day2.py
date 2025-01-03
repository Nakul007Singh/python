name = ["nakul","rahul","yash","nipun","harsh"]

name[1:3] = ["mohit", "ram"]

print(name)

name = ["nakul","rahul","yash","nipun","harsh"]

name.insert(2,"chal")

print(name);

name = ["nakul","rahul","yash","nipun","harsh"]

name.append("orange")
print(name);

name = ["nakul","rahul","yash","nipun","harsh"]
sirname = ["jadon","nagla","singh"]

name.extend(sirname)
print(name)

name = ["naku","singh","jadon"]
for  x in name:
    print(x)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)  

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]  

thislist.sort(reverse=True)

print(thislist)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
if "aam" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
  print("not")

x = ("apple","banana","mango")
y = list(x)

y[1] = "kiwi"

x = tuple(y)

print(x)


x = ("nakul","nipun","yash","ram")
y = list(x)

y[1] = "laxman"

x = tuple(y)

print(x)
x = ("nakul","nipun","yash","ram")
y = list(x)
y.remove("nipun")
x = tuple(y)
print(x)

x = ("nakul","nipun","yash","ram")

del x

print(x)

fruits = ("apple","banana","cherry","ncdjvd","jcede","huehfuef")
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i+1


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(4)

print(x)

x = {"apple","banana","cherry","apple"}

for y in x:
  print(y)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = { "banana", "cherry"}
thisset.discard("apple")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

set1 = {"apple", "banana", "cherry"}
set2 = ["google", "microsoft", "apple"]

set3 = set1.intersection(set2)
print(set3)

ages = {
   "nakul":23,
   "nipun":21,
   "rahul" : 20
}

x = ages.keys()

print(x)

ages["harsh"] = "white"
print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["color"] = "red"

print(thisdict)

a = 33
b = 32

if b < a:
    print("b is greater then a")

elif a == b :
    print("a and b are equal") 

i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i = i+1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  if x == "banana":
    break

for x in range(6):
    print(x)

def my_name(fname):
    print(fname)

my_name("Email")
my_name("Tobias")
my_name("Linus")

def name(first,sec,th):
    print("the name is : " + sec)
x = ["nakul","Singh","jadoun","ram","sita"]
for i in range(2):
    print(x[i])

set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "mango", "papaya"}

set3 = set1.union(set2)
print(set3)
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)