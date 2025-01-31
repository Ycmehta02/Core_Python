#nameless function and can intake any no of arguments and one expression in Lambda function
#reduces no. of lines of code to be written

sum = lambda a,b : a+b+30*2
sum(5,3)
print(sum)
print(sum(8,2))


def myfunc(n):
  return lambda a : a * n  #return statement

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


#Return types--------------------------------------------------

def fun(n):
  return [n ** 2, n ** 3] #return statement

res = fun(3)
print(res)

























