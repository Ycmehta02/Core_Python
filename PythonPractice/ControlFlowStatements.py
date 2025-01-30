
"""
> Selection/Decision))
-if
-if...else
-if---elif---else

>Repetition/Loop
-while
-for

>Transfer/Jump
-break
-continue
-return
-try & except

"""

#***Decision Control***------------------------

#if..elif..else
a=2
b=3
if a>b:
    print("a is greater")
elif b>a:
    print("b is greater")
elif a==b:
    print("equal")
else:
    print("invalid")

# ***Loops***-----------------------------------

# While Loop
i=5
while i>=1:
    print(i)
    i-=1
print("Done")

#while using else
i=5
while i>=1:
    print(i)
    i-=1
else:
    print("---")
print("Done")


# For Loop

#range
for i in range(10): #start with 0 to 9
    print (i)

for i in range(1,11): #1 to 10
    print(i)

for i in range(1,15,3): # +3
    print(i)

for i in range(10,2,-2): # -1
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# break : stop the loop in between
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Continue : we can stop the current iteration in loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)



















