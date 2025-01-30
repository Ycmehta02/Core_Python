#create using {}
#unordered, unchangeable and unindexed (Random order)
#duplicates are ignored

a = {9,5,6,8}
print(a)
print(type(a))
print(len(a))

a.add(3)
print(a)
a.update([0,1])
print(a)
#sorted

#remove

a.pop()
print(a)

print(7 not in a) #True
 #set can only nest with Tuple
b = {1,2,3,(4,5,6),7,8}

#converting list to set
c= [1,3,4,5]
d= set(c)
print(type(d))

#union
print(a.union(b))
print(a | b)
#intersection
print(a.intersection(b))
print(a&b)
#difference
print(a.difference(b))
print(a - b)

















