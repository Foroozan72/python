fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

f = "awesome"
print("Python is " + f)

g = "awesome"

def myfunc():
  print("Python is " + g)

myfunc()

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


l = "Hello, World! , phngf"
print(l.split(","))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#---------------------------------
thislist = ["ss", "dd", "ttt"]
[print(x) for x in thislist]
#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)