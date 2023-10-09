# Day 1 (6h)

I search for "best books for python". After research, i decided [PYTHON CRASH COURSE](https://github.com/ngoctd314/books/blob/master/Python%20Crash%20Course%203rd.pdf) is my first book for my Python career. Hope it is true decision.

OK. Let's Get started.

## Part 1. Basics

### Chapter 1: Getting Started

After quick look. I by pass this chapter. All are related to hello world program and setup env. As i talk before. I understand all of it. If you are not, you need read it step by step.

### Chapter 2: Variables and Simple Data Types

**What really happens when you run hello_world.py**    

When you run the file hello_world.py, the ending .py indicates that the file is a Python program. Your editor then runs the file through the Python interpreter, which reads through the program and determines what each word in the program means.

**Variables**

```py
message = "Hello Python world!"
print(message)
```

Output: Hello Python world!

You can change the value of a variable in your program at any time, and Python will always keep track of its current value.

```py
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

Output:
```txt
Hello Python world!
Hello Python Crash Course world!
```

You can change the value of a variable in your program at any time, and Python will always keep track of its current value.

**Naming and Using Variables**

**Avoiding Name Errors When Using Variables**

Every programmer makes mistakes, and most make mistakes every day. Although good programmers might create errors, they also know how to respond to those errors efficiently. 

When an error occurs in your program, the Python interpreter does its best to help you figure out where the problem is. The interpreter provides a traceback when a program cannot run successfully. A traceback is a record of where the interpreter ran into trouble when trying to execute your code.

```py
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print(mesage)
NameError: name 'mesage' is not defined
```

**Variables are labels**

Variables are often described as boxes you can store values in. This idea can be helpful the first few times you use a variable, but it isn't an accurate way to describe how variables are represented internally in Python. It's much better to think of variables as labels that you can assign to values. You can also say that a variable references a certain value.

This distinction probably won't matter much in your initial programs, but it's worth learning earlier rather than later. At some point, you'll see unexpected behavior from a variable, and an accurate understanding of how variables work will help you identify what's happening in your code.

**Strings**

```py
# String's method
message = "hello Python world!"

print(message.title())
print(message.upper())
print(message.lower())
# Hello Python World!
# HELLO PYTHON WORLD!
# hello python world!
```

```py
# Using variables in strings
first_name = "ada"
last_name = "lovelace"
# These strings are called f-strings.
full_name = f"{first_name} {last_name}"
print(full_name)
```

```py
# Adding whitespace to strings with tabs or newlines
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
```

```py
lang = "Python    "
print(lang.rstrip(), lang.__len__(), lang.rstrip().__len__())
```

```py
# remove Prefixes
nostarch_url = "https://nostarch.com"
nostarch_url.removeprefix("https://")
print(nostarch_url)
```

```py
# Avoiding syntax errors with strings
```

**Number**

```py
print(2+3)
print(2*3)
print(2**3) # 2*2*2
print(3/2)
```

```py
print(.1 + .1)
print(.2 + .2)
print(.3*3)
```

Be aware that you can sometimes get an arbitrary number of decimal places in your answer:

```txt
3*0.1 = 0.30000000000000004
```

```py
# mix an integer and a float in any other operation, you'll get a float as well 
print(4/2)
print(1+2.0)
```

```py
# multiple assignment
a, b = 1, 2
a, b = b, a+b
print(a, b)
```

```py
# Python doesn't have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed
MAX_CONNECTIONS = 5000
```

**The Zen of Python**

Experienced Python programmers will encourage you to avoid complexity and aim for simplicity whenever possible. The Python community's philosophy is contained in "The Zen of Python"


### Chapter 3. Introducing Lists

Lists allow you store sets of information in one place, whether you have just a few items or millions of items. Lists are one of Python's most powerful features readily accessible to new programmers, and they tie together accessible to new programmers, and they tie together many important concepts in programming.

**What is a List**

A list if a collection of items in a particular order. You can put anything you want into a list, and the items in your list don't have to be related in any particular way.

```py
ids = [1,2,3,4,5]

print(ids)
print(ids[0]) # index positions start at 0, not 1
print(ids[-1])
print(ids[ids.__len__()-1]) # as same as -1
ids[0] = 11 # modifying
print(ids[0])
```

```py
motorcycles = []

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

motorcycles.insert(0, 'ducati') # you can add a new element at any position in your list by using the insert() method.
print(motorcycles)

del motorcycles[0] # we use the del statement to remove the first item, "ducati" from the list of motorcycles 
print(motorcycles)

popped = motorcycles.pop() # the pop() method removes the last item in a list, but it lets you work with that item after removing it.
print(popped) 
print(motorcycles)

popped = motorcycles.pop(0) # you can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses
print(motorcycles, popped)
```

```py
# remove an item by value
# sometimes you won't know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the remove() method.
motorcycles = ["honda", "yamaha", "suzuki"]

print(motorcycles)
# remove() method tells Python to figure out where ducati appears in the list and remove that element
# remove() method deletes only the first occurrence of the value you specify. If there's a possibility the value appears more than once in the list, you'll need to use a loop to make sure all occurences of the value are removed.
motorcycles.remove("yamaha")
print(motorcycles)
```

**Organizing a List**

```py
motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles.sort()
print(motorcycles)
motorcycles.sort(reverse=True)
print(motorcycles)
```

```py
# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. The sorted() function lets you display your list in a particular order
# but doesn't affect the actual order or the list
motorcycles = ["honda", "yamaha", "suzuki"]

print(sorted(motorcycles))
print(motorcycles)
```

```py
motorcycles = ["honda", "yamaha", "suzuki"]

# reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.
motorcycles.reverse()
print(motorcycles)
```

**Avoiding Index Errors When Working with Lists**

### Chapter 4: Working with Lists

**Looping through an entire List**

```py
locations = ["a", "e", "c", "b", "d"]

for loc in locations:
    print(loc)
```

**A Closer Look at Looping**

**Doing More Work Within a for Loop**

**Avoiding Indentation Errors**

Python uses indentation to determine how a line, or group of lines, is related to the rest of the program.

**Making Numerical Lists**

```py
# range function() causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. 
for value in range(1,5):
    print(value)
```

```py
# Make a list of numbers, you can convert the results of range() directly into a list using the list() function.
numbers = list(range(1, 6))
print(numbers)
# [1, 2, 3, 4, 5]

# Pass a third argument to range(), Python uses that value as a step size when generating numbers.
numbers = list(range(1, 10, 2))
print(numbers)
```

**List Comprehensions**

```py
squares = [value **2 for value in range (1, 11)]
print(squares)
```

```py
for i in range(1, 21):
    print(i)

for i in range(1, 10**6+1):
    print(i)

ar1M = list(range(1, 10**6+1))
sum1M = sum(ar1M)
print(sum1M, (1 + 10**6)*(10**6) / 2)

odd_numbers = [x for x in range(1,20, 2)]
print(odd_numbers)

threes = [x*3 for x in range(1,11)]
print(threes)

cubes = [x**3 for x in range(1,11)]
print(cubes)
```

**Working with Part of a List**

```py
players = [f"player-{x}" for x in range(1, 6)]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
# If a third value is included, this tells Python how many items to skip between items is the specified range
print(players[0:-1:2])
```

```py
players = [f"player-{x}" for x in range(1, 6)]
# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:])
# This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
cpPlayers = players[:]

cpPlayers[0] = f"update-{cpPlayers[0]}"
print(players)
print(cpPlayers)
```


**Tuples**
