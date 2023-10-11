# Day 3

## Classes

**Inheritance**

You don't always have to start from scratch when writing a class. You can use inheritance. When one class inherits from another, it takes on the attributes and methods of the first class. The child class can inherit any or all of the attributes and methods of its parent class, but it's also free to define new attributes and methods of its own.

When you're writing a new class based on an existing class, you'll often want to call the __init__() method from the parent class. This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class.

```py
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Creates a new attribute and sets its initial value to 0
        self.odometer_reading = 0

    def get_description_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
     """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


# When you create a child class, the parent class must be part of the current file and must appear before the child class is the file.
class ElectricCar(Car):
    """Represent aspect of a car, specific to electric vehicles"""

    # The __init__() method takes in the information required to make a Car instance
    def __init__(self, make, model, year=2023):
        # The super() function is a special function that allows you to call a method from the parent class.
        # This line tells Python to clal the __init__ method from Car, which gives an ElectricCar instance
        # all the attributes defined in that method. The name super comes from a convention of calling the parent
        # class a superclass and the child class a subclass.
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_leaf = ElectricCar("nissan", "leaf")
print(my_leaf.get_description_name())
my_leaf.describe_battery()
```

**Overriding Methods from the Parent Class**

You can override any method from the parent class doesn't fit what you're trying to model with the child class. To do this, you define a method in the child class with the same name. Python will disregard the parent class method and only pay attention to the method you define in the child class.

```py
class ElectricCar(Car):
    def fill_gas_tank(self):
    """Electric cars don't have gas tanks."""
    print("This car doesn't have a gas tank!")
```

When you use inheritance, you can make your child classes retain what you need and override anything you don't need from the parent class.

**Instances as Attributes**

When modeling something from the real world in code, you may find that you're adding more and more detail to a class. You'll find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these situation, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together; this approach is called composition.

For example, if we continue adding detail to the ElectricCar class, we might notice that we're adding many attributes and methods specific to the car's battery. When we see this happening, we can stop and move the attributes and methods to a separate class called Battery. Then we can use a Battery instance as an attribute in ElectricCar class:

**Modeling Real-World Objects**

**Importing Classes**

## File and exceptions

**Reading from a File**

When you want to work with the information in a text file, the first step is to read the file into memory.

**Writing to file**

**Exceptions**

Python uses special objects called exceptions to manage errors that arise during a program's execution. Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object. If you write code that handles the exception, the program will continue running. If you don't handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.

Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong. Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you've written.

```py
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# Any code that depends on the try block executing successfully goes in the else block
else:
    print("Not go into exception")
```

**Failing Silently**

Sometimes, you'll want the program to fail silently when an exception occurs and continue on as if nothing happened.

```py
try:
    print(5/0)
except ZeroDivisionError:
    pass
```

The pass statement also acts as a placeholder. It's a reminder that you're choosing to do nothing at a specific point in your program's execution and that you might want to do something there later.

**Deciding Which Errors to Report**

### Storing Data

