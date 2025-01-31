a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#multi line string

#string are arrays
a= "Hello, Hyy"
print(a[1])

#looping with string
for x in a:
    print(x)
print(len(a)) #length

print ("Hyy" in a) #check not in for negation

if "Hyy" in a:
    print("Present")

#Slicing--------------------------------------------
#You can return a range of characters by using the slice syntax.

b = "Hello, Good Morning!"
print(b[2:9])
print(b[:9])
print(b[9:])
print(b[-5:-2])

#Modify String------------------------------------------------
print(a.upper()) #uppercase
print(b.lower()) #lowercase

#The strip() method removes any whitespace from the beginning or the end
print(a.replace("!", "#"))

#The split() method returns a list where the text between
# the specified separator becomes the list items.
print(a.split(",")) #splits by ,

#Concatenation--------------------------------------------------
c = a + b
print(c)

c = a + " " + b
print(c)

#Format String--------------------------------------------------
#as we cannot combine string and no. with +
#So use f-string or format()

name = "YM"
age = 21
msg= f"Name : {name}, Age: {age}"
print(msg)

#placeholder {}  Modifier :
msg= f"Name : {name}, Age: {age:.2f}" # add 2 decimals
print(msg)

#A placeholder can include a modifier to format the value &
# can contain variables, operations, functions, and modifiers to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type





























