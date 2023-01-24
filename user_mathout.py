"""
Always start with a docstring that describes what the module does.
Include Courtney Pigford 1/21/2023. 

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math
from multiprocessing.connection import answer_challenge

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = 0 # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)




# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":


    ### Testing the import math functions 
    print("Courtney Pigford", "1/21/23")
    
    number1 = int(input('number of pasta sauce:  '))
    number2 = int(input('number of noodles: '))
    total = number1 * number2
    print('How many combinations', number1, 'and', number2, 'is', total)

 ### Ratio's of Pasta to Sauce.  


# Import math library 

import math 

print('round ounces of sauce to its nearest ounce')

print(math.ceil(1.5))
print(math.ceil(4.5))
print(math.ceil(9.25))

import math 

print('How packages of pasta you need')

number1 = (math.fabs(-2.5))
number2 = (math.ceil(15.5))
total = number1 + number2
print(total, 'is the number of packages of pasta you need')

print('How Many Pots')
number1 = int(1)
print('You will need', math.sqrt(number1), 'size pot')

print("how many combinations of past dishes you can make")
n=13
k=8
print(math.comb(n, k))
print(f"math.perm(13, 8) = {math.perm(13, 8)}")

print('Cost to make a pasta dish')


def get_price_of_pasta(unit_price=1.99, quantity=1):
    """return price of pasta."""
    return unit_price * quantity

print(get_price_of_pasta())

def get_price_of_sauce(jar_cost=2.49, quantity=1):
    """return price of sauce."""
    return jar_cost * quantity

print(get_price_of_sauce())

def get_sum_of_cost(price_of_pasta=1.99, price_of_sauce=2.49):
    """Sum of Cost."""
    return price_of_pasta * price_of_sauce

print('Total cost:  ',get_sum_of_cost())

(base) Courtney-MacBook-Pro:datafun-02-functions resetandwiped$ /usr/local/bin/python3 /Users/resetandwiped/Desktop/44608-80:81/datafun-02-functions/user_mathout.py
Courtney Pigford 1/21/23
number of pasta sauce:  5
number of noodles: 6
How many combinations 5 and 6 is 30
round ounces of sauce to its nearest ounce
2
5
10
How packages of pasta you need
18.5 is the number of packages of pasta you need
How Many Pots
You will need 1.0 size pot
how many combinations of past dishes you can make
1287
math.perm(13, 8) = 51891840
Cost to make a pasta dish
1.99
2.49
Total cost:   4.955100000000001
(base) Courtney-MacBook-Pro:datafun-02-functions resetandwiped$ 