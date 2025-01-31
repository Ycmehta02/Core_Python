#Everything in Python is an object, with its properties and methods.
#class is blueprint for creating object

class demo: #class
    a = "Heyy"
x = demo() #object
print(x.a)

#__init__() function---------------------------------------------
#it is executed when class is being initiated
#__init__() function to assign values to object properties

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("YM", 21)

print(p1.name,p1.age)
# __str__() function-----------------------------------------------------------
#controls what should be returned when the class object is represented as a string

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

#Object Methods------------------------------------------------------------------------
#Object can also contain methods
#Methods in object are function that belong to object

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self): #method of class
    print("Hello my name is " + self.name)

p1 = Person("YM", 21)
p1.myfunc() #object method, function calling of class

#Self parameter--------------------------------------------------------------------
#a reference  to current instance of class, is used to access variables that belongs to access
#its not mandatory to name is "self", can name it anything
#first parameter of any function in class

#used myobject and abc instead of self
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name , abc.age)

p1 = Person("YM", 21)
p1.myfunc()

#Modify and delete object properties-----------------------------------------------------

p1.age = 22 #modifying age
p1.myfunc()

# del p1.age #deleting age
# p1.myfunc() # error

# del p1 #-- deleting object

#pass to class for no content

#Static and Instance variable & Methods-------------------------------
#Static -- Class and common stuff
#Instance -- Objects and changeable stuff

class Car:
    wheels = 4 #static variable
    def __init__(self,brand,model):
        self.brand = brand #instance variable
        self.model =model

    def start_car(self):
        print(self.brand+ "Model:" + self.model + "started")

    @staticmethod
    def pwheels():
        print(Car.wheels) # called by class name

s = Car("Maruti","swift")
print(Car.wheels)
Car.pwheels()



































