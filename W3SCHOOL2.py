x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#pass
a = 33
b = 200

if b > a:
  pass

#CONTINUE

ruits = ["apple", "banana", "cherry"]

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)



for x in range(6):
  print(x)

#-----------------------

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.

def my_fun(asd,dfg):
    print(asd+" "+dfg)

my_fun("foroozan","kashani")