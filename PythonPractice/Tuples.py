#create tuple using ()
#same as list but immutable
a = (1,2,3,4,1,2,3,4,5,6,6,4)
print(a)
print(type(a))
print(a[2])
print(a[-1])

#we cannot use append(), insert(), remove() & pop(), sort(), reverse()
for i in range(len(a)):
    print(a[i])

for e in a:
    print(e)

print (3 in a) # True
print (10 in a) # False
print(a.count(4)) # 3
print(sum(a)) #41
print(max(a)) #6
print(min(a)) #1
print(a.index(3)) #2

b =(1,2,[3,4,5],6,7,8,9)
c =(1,2,(3,4,5),6,7,8,9)
print(c[2][1])
























