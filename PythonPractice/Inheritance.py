#It allows a class (child/derived class) to inherit attributes and methods from another class (parent/base class).
#This helps in code reusability and establishing relationships between classes.

#key conepts********************************************************************

#super() method----------------------------------------------------------------
#The super() method is used to call the parent class's constructor or methods.
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling Parent Constructor
        self.age = age

child = Child("Yashvi", 22)
print(child.name)  # Output: Yashvi
print(child.age)   # Output: 22
#----------------------------------
class Parent:
    def show(self):
        print("This is the Parent class method.")

class Child(Parent):
    def show(self):
        super().show()  # Calls the Parent class method
        print("This is the Child class method.")

obj = Child()
obj.show()


#Method Overriding--------------------------------------------------------------
#When the child class provides its own implementation of a method that already exists in the parent class.
class Parent:
    def show(self):
        return "This is Parent class"

class Child(Parent):
    def show(self):  # Overriding Parent Method
        return "This is Child class"

obj = Child()
print(obj.show())  # Output: This is Child class

#isinstance() & issubclass()-------------------------------------------------
#isinstance(obj, Class): Checks if obj is an instance of Class or its subclass.
#issubclass(Class1, Class2): Checks if Class1 is a subclass of Class2.
class A:
    pass

class B(A):
    pass

obj = B()
print(isinstance(obj, B))  # True
print(isinstance(obj, A))  # True (Because B is a subclass of A)
print(issubclass(B, A))    # True
print(issubclass(A, B))    # False

# Private & Protected member--------------------------------------------------
#_protected: Can be accessed in derived classes.
#__private: Cannot be accessed directly in derived classes.
class Parent:
    def __init__(self):
        self._protected = "Protected Attribute"
        self.__private = "Private Attribute"

class Child(Parent):
    def show(self):
        print(self._protected)  # Accessible
        # print(self.__private)  # Not Accessible

obj = Child()
obj.show()


#Single Inheritance---------------------------------------------------------------

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name  # Instance Variable

    def speak(self):
        return "Animal makes a sound"

# Child Class
class Dog(Animal):
    def speak(self):  # Overriding parent method
        return f"{self.name} barks!"

# Creating an object of Dog class
dog = Dog("Buddy")
print(dog.name)       # Output: Buddy
print(dog.speak())    # Output: Buddy barks!

#Multiple Inheritance-------------------------------------------------------------

# Parent Class 1
class Father:
    def __init__(self, surname):
        self.surname = surname

    def show_father(self):
        return "Father's property"

# Parent Class 2
class Mother:
    def show_mother(self):
        return "Mother's property"

# Child Class (inherits from both Father and Mother)
class Child(Father, Mother):
    def __init__(self, name, surname):
        super().__init__(surname)
        self.name = name

    def show_child(self):
        return f"{self.name} {self.surname} has inherited both properties"

# Creating an object
child = Child("Yash", "Mehta")
print(child.show_father())   # Output: Father's property
print(child.show_mother())   # Output: Mother's property
print(child.show_child())    # Output: Yash Mehta has inherited both properties

#MultiLevel Inheritance-------------------------------------------------------------
#A child class inherits from another child class (grandchild relationship).

# Grandparent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Brand: {self.brand}"

# Parent Class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        return f"Model: {self.model}"

# Child Class (Grandchild)
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def show_battery(self):
        return f"Battery: {self.battery} kWh"

# Creating an object
tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.show_brand())   # Output: Brand: Tesla
print(tesla.show_model())   # Output: Model: Model S
print(tesla.show_battery()) # Output: Battery: 100 kWh

#Heirarchical Inheritance----------------------------------------------------------
#A single parent class is inherited by multiple child classes.
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal makes a sound"

# Child Class 1
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows!"

# Child Class 2
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"

# Creating objects
cat = Cat("Whiskers")
dog = Dog("Rex")

print(cat.speak())  # Output: Whiskers meows!
print(dog.speak())  # Output: Rex barks!








































