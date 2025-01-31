#wraping variable and code in class -> encapsulation
#variables cannot be directly accessed outside of class
#It ensures controlled access using getters and setters.

#_protected: Can be accessed in derived classes.
#__private: Cannot be accessed directly in derived classes.

class Student:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.__age = age  # Private attribute

    def get_age(self):
        """Getter method to access private attribute."""
        return self.__age

    def set_age(self, new_age):
        """Setter method to modify private attribute."""
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive.")

# Creating an object of Student class
student = Student("Yashvi", 21)

# Accessing public attribute
print(f"Student Name: {student.name}")

# Trying to access private attribute directly (will cause an error)
# print(student.__age)  # This will raise an AttributeError

# Accessing private attribute using getter
print(f"Student Age: {student.get_age()}")

# Modifying private attribute using setter
student.set_age(22)
print(f"Updated Age: {student.get_age()}")

# Trying to set an invalid age
student.set_age(-5)  # This will not update the age


# Encapsulation: The __age attribute is private and cannot be accessed directly.
# Getter (get_age()): Allows controlled access to the private attribute.
# Setter (set_age()): Ensures the private attribute is modified with valid data.
# Security: Prevents direct modification of the age, ensuring valid values.













































