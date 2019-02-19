import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============ USER DEFINED FUNCTION ============

def tuple_ex():
    """ return defined t tuple"""
    t = (1,2,3)
    return t
a,b,c = tuple_ex()  # a = 1, b = 2, c = 3


# # ============ SCOPE ============
# Global: defined in main body in script
# Local: defined in a function
# Build in scope: names in pre-difined built in scope module (such as print, len)

x = 2
def f():
    x = 3
    return x
print(x)      # x = 2 global scope
print(f())    # x = 3 local scope


# What if there is no local scope?
x = 5

def f():
    y = 2*x        # there is no local scope x
    return y
print(f())         # it uses global scope x
# First local scopesearched, then global scope searched, if two of them cannot be found lastly built in scope searched.


# ============ NESTED FUNCTION ============
def square():
    """ return square of value """
    def add():
        """ add two local variable """
        x = 2
        y = 3
        z = x + y
        return z
    return add()**2
print(square())


# ============ DEFAULT and FLEXIBLE ARGUMENTS ============

# flexible arguments *args
def f(*args):
    for i in args:
        print(i)


# flexible arguments **kwargs that is dictionary (kwargs = keyworded argument, such as dictionary entry)
def f(**kwargs):
    """ print key and value of dictionary"""
    for key, value in kwargs.items():
        print(key, " ", value)


# ============ LAMBDA FUNCTION ============
# lambda function
square = lambda x: x**2     # where x is name of argument
print(square(4))
tot = lambda x,y,z: x+y+z   # where x,y,z are names of arguments
print(tot(1,2,3))


# ============ ANONYMOUS FUNCTION ============
# Similar to Lambda function, but it can take more than one arguments

number_list = [1,2,3]
y = map(lambda x:x**2,number_list)
print(list(y))


# ============ ITERATORS ============

name = "ronaldo"
it = iter(name)
print(next(it))    # print next iteration ('r')
print(*it)         # print remaining iteration ('o n a l d o')

# zip example
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
z = zip(list1, list2)  # Creates a zip object
z_list = list(z)  # Turns zip object into a list
print(z_list)     # [(1, 5), (2, 6), (3, 7), (4, 8)]

un_zip = zip(*z_list)
un_list1, un_list2 = list(un_zip)  # unzip returns tuple (same values as input above)


# ============ * LIST COMPREHENSION ^ ============
# Collapse for loops for building lists into a single line.
# Ex. num1 = [1,2,3] and we want to make it num2 = [2,3,4]. This can be done with for loop. However it is unnecessarily
# long. We can make it one line code that is list comprehension.

# Example of list comprehension
num1 = [1, 2, 3]
num2 = [i + 1 for i in num1]  # Results in [2,3,4]

# Conditionals on iterable
num1 = [5, 10, 15]
num2 = [i**2 if i == 10 else i-5 if i < 7 else i+5 for i in num1]  # Results in [0, 100, 20]

# lets return pokemon csv and make one more list comprehension example
# lets classify pokemons whether they have high or low speed. Our threshold is average speed.
data = pd.read_csv('./input/pokemon.csv')
threshold = sum(data.Speed)/len(data.Speed)
data["speed_level"] = ["high" if i > threshold else "low" for i in data.Speed]
data.loc[:10, ["speed_level", "Speed"]]


# ======================================================================================================================
# Link : https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners
# ======================================================================================================================
