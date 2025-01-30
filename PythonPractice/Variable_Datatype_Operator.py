# ***Variables***---------------------------------------
x = 9
z = True
print(x)

#prints latest value & case sensitive
y = "python"
y = 10
print(y)
print(z)
print(2)

#multiple variable initialization
a,b,c=1,2,3
A=B=C=7
print(c,C)

# ***Datatypes***-----------------------------------------
"""
Int,Float,String,Boolean
Dictionary,Tuple,List
"""
print(type(z))
#Typecast
a = int(9.1)
print(type(a))
print(a) #9

a = int("9")
print(type(a))
print(a+2) #11

a = str(2.5)
print(type(a))
print(a + " 2.5") #2.5 2.5

#***Operators*** ----------------------------------------------

# Arithmetic: +, -, *, /, %, **(exponential), //(Floor Division- round of int)
# Logical: and, or, not
# Assignment: =, +=, -+, *=, /+, %=, //=, **=
# Relational: ==, !=, >, <, >=, <=

print(False and True)
print(True or False)

#precedence: () > ** >  * / % //  > + - >
#left to right (same precedence)

#-----------------------------------------------------------------

del a #delete

# '+' -- concatenation
print("YM" + str(2))

# """ xyz """ --multiline preformatted text

#formatting print statement:
# +  str() ,
# {index}- .format(x,y)
# %s  %d























