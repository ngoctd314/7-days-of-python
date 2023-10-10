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
