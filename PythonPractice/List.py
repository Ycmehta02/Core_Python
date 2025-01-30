#list :store multiple item in single variable
#created using [ ]
#items are indexed like array
#lists are ordered, changeable & allow duplicate values

l=["hy",2,"birds"]
print(l)

l=["hy",2,"birds","hy"]
print(l)
#can have same value and any datatype

print(len(l)) #length of list
print(type(l)) #list are objects with list datatype

# list() - list constructor can be used to create list
l = list(("hy","aster","wallflower","cherry",9,2,"flower"))
print(l)

# Accessing List---------------------------------------------------------
print(l[1]) #access with index
print(l[-1]) #negative indexing starts from end

print(l[2:5]) #returns 3rd to 5th item by index
print(l[-4:-1])

#check if item exist
if 2 in l:
    print("y")

#Change list items--------------------------------------------------------
l[0] = "hello"
print(l[0])

#change a range of items
l[4:6]= [1,2]
print(l)

l[0:1]= ["hii", "hyy"] #replace 1 value with 2
print(l)
#viceversa can replace 3 value with 1

#Add Items----------------------------------------------------------------

#append(): here items will be added to end
m= ["one",1,"two",2,"three"]
m.append(3)
print(m)

#insert(): items in between
l.insert(1, "ym")
print(l)

#extend(): append items from another list to current list
l.extend(m)
print(len(l))
print(l)

#add any iterables -> from tuple to list / set to list

#Remove Items---------------------------------------------------------------

#remove()
l.remove(2) #remove first occurrence
print(l)

#pop() - removes specified index
l.pop(2)
print(l)
#if index not specified, removes last item

#del - removes specified index
del l[0]
print(l)
#if index not defined, list is deleted

#clear() - empties the list, list remains without data

#Loop List-------------------------------------------------------------------
#can loop through list

for i in range(len(l)):
    print(l[i])

i=0
while i < len(l):
    print(l[i])
    i+=1

#comprehension
[print(x) for x in l]

#Comprehension----------------------------------------------------------------

#newlist = [expression for item in iterable if condition == True]
m = ["Orange", "mango", "kiwi", "Pineapple", "banana"]
l1 = [x for x in m if "a" in x]
print(l1)

#Sort--------------------------------------------------------------------------
#alphanumerically, ascending, by default
m.sort(reverse = True)
print(m)

m.sort(key = str.lower)
m.reverse()
print(m)

#Copy---------------------------------------------------------------------------

#copy()
l1 = l.copy()
print(l1)

#list()
l1 = list(m)
print(l1)

# ":" (slice) operator
a = ["spades","heart","club","diamond"]
b = ["Joker","king","queen"]
c= a[:]
print(c)

#Join-----------------------------------------------------------------------------
c = a + b
print(c)

for i in b:
    a.append(i)
print(a)

m.extend(c)
print(m)

