# Day 2 (8h)

## If statements

Learned how to write conditional tests, which always evaluate to True or False. You learned to write if statements, if-else chains and if-elif-else chains. You began using these structures to identify particular conditions you need to test and to know when those conditions have been meet in your programs.

## Dictionaries

```py
# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.
# A key's value can be a number, a string, a list or even another dictionary. 
# In Python, a dictionary is wrapped in braces {} with a series of key-value pairs inside the braces.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
```

```py
# It's sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it.
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
```

```py
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
alien_0['addr'] = 'USA'
print(alien_0)
del alien_0['addr']
print(alien_0)
```

**A Dictionary of Similar Objects**

**Using get() to Access Values**

```py
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
# Using keys in square brackets to retrieve the value you're interested in from a dictionary might cause one potential problem:
# if the key you ask for doesn't exist, you'll get an error.
print(alien_0.get('colors', 'default value'))
# If you leave out the second argument in the call to get() and the key doesn't exist, Python will return the value None. The special value None means "no value exists"
# This is not an error: it's a special value meant to indicate the absense of a value.
print(alien_0['colors'])
# The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn't exist.
print(alien_0.get('colors'))
```

**Looping through a dictionary**

```py
persons = {
    'username': 'admin',
    'first': 'super',
    'last': 'ad'
}

for key, value in persons.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

**Looping Through All the Keys in a Dictionary**

```py
persons = {
    'username': 'admin',
    'first': 'super',
    'last': 'ad'
}

# The keys() method is useful when you don't need to work with all of the values in a dictionary. 
for key in persons.keys():
    print(f"\nKey: {key}")
```
Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote:

```py
for name in dictionary:
for name in dictionary.keys():
```

**Looping Through a Dictionary's Keys in a Particular Order**

Looping through a dictionary returns the items in the same order they were inserted. Sometimes, though, you'll want to loop through a dictionary in a different order.

You can use the sorted() function to get a copy of the keys in order:

```py
languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Rust',
    'phil': 'Python'
}

for name in sorted(languages.keys()):
    print(name)
```

**Looping Through All Values in Dictionary**

```py
languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Rust',
    'phil': 'Python'
}

# If you are primarily interested in the values that a dictionary contains, you can use the values() method to return a sequence of values without any keys.
for name in languages.values():
    print(name)
```

```py
languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Rust',
    'phil': 'Python'
}

# set is a collection in which each item must be unique
# when you wrap set() around a collection of values that contains duplicate items, Python identifies the unique items in the collection and builds a set from those items.
# It's easy to mistake for dictionaries because they're both wrapped in braces. When you see braces but no key-value pairs, you're probably looking at a set.
# Unlike lists and dictionaries, sets do not retain items in any specific order.
for name in set(languages.values()):
    print(name)
```

**Nesting**

```py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

```py
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': alien_number, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
```

**A List in a Dictionary**

```py
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

for topping in pizza['toppings']:
    print(f"\t{topping}")
```

**A Dictionary in a Dictionary**

You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do.

```py
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

## User Input and While Loops

**How the input() function works**

The input() function pauses your program and waits for the user to enter some text. Once Python receives the user's input, it assigns that input to a variable to make it convenient for you to work with.

```py
message = input("Tell me something: ")
print(message)
```

**Using int() to Accept Numerical Input**

When you use the input() function, Python interprets everything the user enters as a string. Consider the following interpreter session, which asks for the user's age:

**Introducing while loops**

```py
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

**Using a while loop with Lists and Dictionaries**

A for loop is effective for looping through a list, but you shoudn't modify a list inside a for loop because Python will have trouble keeping tracking of the items in the list

```py
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users has been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

```py
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)
```

## Functions

**Defining a Function**

```py
# Which tells Python that you're defining a function
# This is the function definition, which tells Python the name of the function and,
# if applicable, what kind of information the function needs to do its job. The parentheses hold that information.
def greet_user(): 
    # This text is called a docstring; which describes what the function does. When Python generates documentation
    # for the functions in your programs.
    """Display a simple greeting."""
    print("Hello!")


greet_user()
```

**Arguments and Parentheses**

```py
# parentheses username
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username}!")


# argument "admin"
greet_user("admin")
```

**Passing Arguments**

When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called positional arguments.

```py
def greet_user(username, age):
    """Display a simple greeting."""
    print(f"Hello, {username} - {age} years old!")


greet_user("admin", 23)
```

```py
# Order Matters in Positional Arguments
# check to make sure the order of the arguments in your function call matches the order of the parameters in the function's definition.
def greet_user(username, age):
    """Display a simple greeting."""
    print(f"Hello, {username} - {age} years old!")


greet_user(23, "admin")
```

**Keyword Arguments**

A keyword argument is a name-value pair that you pass to a function. When you pass the argument to the function, there's no confusion. Keyword arguments free you from having to worry about correctly ordering your arguments in the function call.


```py
def describe_pet(animal_type, pet_name):
    """Diplay information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# The order of keyword arguments doesn't matter because Python knows where each value should go.
describe_pet(animal_type="hamster", pet_name="harry")
```

**Default Values**

```py
# Set default value for animal_type = 'dog', we can ignore animal_type when call this function 
# Because the default value makes it unneccessary to specify a type of animal as an argument, the only argument left in the function call is the pet's name.
# Python sill interprets this as a positional argument, so if the function is called with just a pet's name, that argument will match up with the first parameter listed in the function's definition.
def describe_pet(pet_name, animal_type="dog"):
    """Diplay information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name="harry")
```

Because positional arguments, keyword arguments, and default values can be used together, you'll often have several equivalent ways to call a function. 

```py
# Equivalent Function Calls
def describe_pet(pet_name, animal_type='dog'):
```
With this definition, an argument always needs to be provided for pet_name, and this value can be provided using the positional or keyword format.

**Avoiding Argument Errors**

**Return values**

```py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
```

**Using a Function with a while Loop**

```py
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        print(name)


usernames = ["a", "b", "c"]
greet_users(usernames)
```

```py
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

**Preventing a Function from Modifying a List**

Sometimes you'll want to prevent a function from modifying a list.  In this case, you can address this issue by passing the function a copy affect only the copy, leaving the origin list intact. 

You can send a copy of list to a function like this:

```py
function_name(list_name[:])
```

**Passing an Arbitrary Number of Arguments**

```py
# The asterisk in the parameter name *toppings tells Python to make a tuple called toppings, containing all the values this function receives.
# Note that Python packs the arguments into a tuple, even if the function receives only one value
def make_pizza(*toppings):
    """Print the list of toppings that have been"""
    print(toppings)
```

**Mixing Positional and Arbitrary Arguments**

You'll often see the generic parameter name *args, which collects arbitrary positional arguments like this.

```py
def make_pizza(size, *toppings):
    """Print the list of toppings that have been"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni", "mushrooms", "green peppers")
```

**Using Arbitrary Keyword Arguments**

Sometimes you'll want to accept an arbitrary number of arguments, but you won't know ahead of time what kind of information will be parsed to the function. In this case, you can write functions that accept as many key-value pairs as the calling statement provides. One example involves building user profiles:  

```py
# The double asterisk before the parameter **user_info cause Python to create a dictionary called user_info containing all the extra name-value pairs the function receives.
# You'll often see the parameter name **kwargs used to collect nonspecific keyword arguments.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)

print(user_profile)
```

**Storing Your Functions in Modules**

```py
# A module is a file ending in .py that contains the code you want to import into your program.
# When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions
# from it into this program. You don't actually see code being copied between fileds because Python copies the code behind the scenes, just before the program runs
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def make_name():
    print("abc")
```

## Classes

Object-oriented programming (OOP) is one of the most effective approaches to writing software. In object-oriented programming, you write classes that represent real-world things and situations, and you create objects based on these classes.

**Creating and Using a Class**

```py
# We first define a class called Dog
# By convention, capitalized names refer to classes in Python.
# There are no parentheses in the class definition because we're create this class from scratch.
class Dog:
    """A simple attempt to model a dog."""

    # The __init__() Method
    # A function that's part of a class is a method.
    # __init__() method is a special method that Python runs automatically whenever we create a new instance based on the Dog class.
    # We define the __init__() method to have three parameters: self, name, and age.
    # The self parameter is required in the method definition, and it must come first, before the other parameters.
    # It must be included in the definition because the Python calls method later (to create an instance of Dog).
    # the method call will automatically pass the self argument. Every method call associated with an instance automatically passes self
    # which is a reference to the instance itself; which is a reference to the instance itself; it gives the individual instance access to
    # the attributes and methods in the class. When we make an instance of Dog, Python will call the __init__() method from the Dog class.
    # We'll pass Dog() a name and age as arguments; self is passed automatically, so we don't need to pass it.
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # The two variables defined in the body of the __init__() method each have the prefix self. Any variable prefixed with self is available to every
        # method in the class, and we'll also be able to access these variables through any instance created from the class. The line self.name = name
        # takes the value associated with the parameter name and assigns it to the variable name, which is then attached to the instance being created.
        # The same process happens with self.age = age. Variables that are accessible through instances like this are called attributes.
        self.name = name
        self.age = age

    # The Dog class has two other methods defined: sit() and roll_over()
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Python reads this line, it calls the __init__() method in Dog with the arguments 'Willie' and 6.
# The __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values we provided.
# Python then returns an instance representing this dog. We assign that instance to the variable my_dog. The naming convention is helpful here;
# we can usually assume that a capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.
my_dog = Dog("Willie", 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

# Even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class. You can make as many instances from
# one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary. 
your_dog = Dog("Lucy", 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```

```py
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)

    def open_restaurant(self):
        print("is open")


res = Restaurant("name's", "cuisine")
res.describe_restaurant()
res.open_restaurant()
```

**Working with Classes and Instances**

You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

```py
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_description_name())
```

You can change an attribute's value in three ways: you can change the value directly through an instace, set the value through a method, or increment the value (and a certain amount to it) through a method.

```py
# The simplest way to modify the value of an attribute is to access the attribute directly through an instance. Here we set the odometer reading to 23 directly.
my_new_car.odometer_reading = 10
my_new_car.read_odometer()
```

Modifying an Attribute's Value Through a Method

In can be helpful methods that update certain attributes for you. Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.
