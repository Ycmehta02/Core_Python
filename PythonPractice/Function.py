#Function calling to execute block of code
#here repetition of code is resolved
#Syntax: def fun_name():

def fun_try():
    print("function")

fun_try() #Function call

#------------------------------
#parameter
#data passing to the function --> argument
def fun1(name):
    print ("Name:" +name)

fun1("YM")
fun1("HB")
#-------------------------------------
#default arguments
def fun1(name="YM"):
    print ("Name:" +name)

fun1("HB")
fun1()
#----------------------------------------
#function with multiple parameters
def sum(a,b,c):
    print(a+b+c)

sum(2,3,3)
#-----------------------------------------
#function return data
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
print(sum(5,5))
print(sub(2,9))
#------------------------------------------
print("Enter no.")
num = input()
print(int(num))
#max() & min() function

#--------------------------------------------
#Local & Global Variable
name = "HB"
def fun2():
    global name
    name = "YM"
    print(name)

fun2()
print(name)


#----------------------------------------------------

def fun1(msg):
    def fun2():
        # Using the outer function's message
        return f"Message: {msg}"
    return fun2

# Getting the inner function
fun3 = fun1("Hello, World!")

# Calling the inner function
print(fun3())




























