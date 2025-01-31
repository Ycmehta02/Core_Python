#1) Comiple time error - syntactical error eg. missing(:)
#2) Logical error - wrong output
#3) Runtime error - divide by zero
#-------------------------------------------------------------------------------------
"""
try:
    # Code that may raise an exception
    pass
except ExceptionType:
    # Code to handle the exception
    pass
finally:
    # Code that always runs, whether an exception occurs or not
    pass
"""
#-------------------------------------------------------------------------------------
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2  # This might raise a ZeroDivisionError
    print("Result:", result)
except ZeroDivisionError:  # Handling division by zero
    print("Error: Division by zero is not allowed!")
except ValueError:  # Handling invalid input
    print("Error: Please enter valid integers!")
finally:
    print("Execution completed.")  # This will always execute

#Custom Exception------------------------------------------------------------------------
#A custom exception can be created by subclassing the built-in Exception class

# Defining a custom exception
class AgeTooSmallError(Exception):
    def __init__(self, message="Age must be 18 or above"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise AgeTooSmallError  # Raising the custom exception
    else:
        print("Access granted!")

# Using try-except to handle the custom exception
try:
    age = int(input("Enter your age: "))
    check_age(age)
except AgeTooSmallError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a valid number!")

#-------------------------------------------------------


# try-except-finally helps handle exceptions and ensures error-free execution.
# Multiple except blocks can catch different exceptions.
# finally always executes, even if an exception occurs.
# Custom exceptions allow us to define and handle application-specific errors.




































