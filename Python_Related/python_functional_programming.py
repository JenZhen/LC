# Python Functional Programming
# This note is based on Python3

#############
# Generators
#############

# Official Document: https://docs.python.org/3/tutorial/classes.html#generators
# Key features:
# - Looks like a function
# - Uses "yield" instead of "return"
# - next() to iterate through values, cannot go back

# Benefit
# - Lazy way of generate values
# - Save memory
# - Save time

# Construct iterators
# Example
def evenNumGen():
    value = 0
    while True:
        yield value # yield signify this is generator
        value += 2  # generator, unlike function, CAN do inifite loop

g = evenNumGen() # g is a generator
# use next() iterator to call next element
# 1) next(g);
# 2) in python3 g.__next__()
#    in python2 g.next()
print("Example for evenNumGen")
print(g.__next__()) # 0
print(next(g))      # 2
print("\n")
# Like function, generator constructor can pass in varibales
# Once iterator is out of boundry, raise StopIteration Error

def evenNumGenLimited(limit):
    value = 0
    while value <= limit:
        if value % 2 == 0:
            yield value
        value += 1

g = evenNumGenLimited(10) # generator limit is 10
print("Example for evenNumGenLimited")
print(next(g))      # 0
print(next(g))      # 2
print(next(g))      # 4
print(next(g))      # 6
print(next(g))      # 8
print(next(g))      # 10
#print(next(g))      # StopIteration Error
print("\n")


#############
# Iterators
#############

# Explicit Use
l = [1, 2, 3, 4]
l_it = iter(l)
print("Iter value from list: %s" %l_it.__next__())

# Implicit Use
# for loop, "for" factory method in dictionay, set, tuple, list
# that after each loop, element will use next() to do auto-increment
# Example
for i in range(4):
    pass
    # do something
    # i auto increase

l = [1, 2, 3]
t = (1, 2, 3)
s = {1, 2, 3}
dic = {1: "a", 2: "b", 3: "c"}

for i in l:
    print("in l: %s" %i)
for i in t:
    print("in t: %s" %i)
for i in s:
    print("in s: %s" %i)
for i in dic:
    print("in dic: [%s, %s]" %(i, dic[i]))

print("\n")

###################
# function/lambda
###################

# Documentation:
# https://www.dataquest.io/blog/introduction-functional-programming-python/
# Key features:
# - lambda: no function name, can be assigned to a variable
# - Anonymous: no function name, not assgined to anyone, succinct

# Example

# Define a add function
def add_function(a, b):
    return a + b

# add_lambda variable refers to a lambda function
add_lambda = lambda a, b: a + b
print("Example for lambda function")
print(add_function(1, 2)) # 3
print(add_lambda(1, 2))   # 3

# Not assigning lambda function to any variable is called "anonymous function"
l_unsorted = [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
# key of sorted function takes an anonymous function
#                                             x refers to each element of l_unsorted, x[1] is number part of tuple
l_sorted = sorted(l_unsorted, key = lambda x: x[1])
print("sorted list: %s" %l_sorted)

print("\n")

###################
# map/filter/reduce
###################

# map function
# Documentation: https://www.dataquest.io/blog/introduction-functional-programming-python/
# Key features:
# transform lists into list, note that input could be multiple lists, depending on function inputs
# transformation rule: function that provides a transformation logic
#                      1)function name 2) lambda function
#                      function takes the SAME NUMBER of arguments as the number of input lists
#                      output is a list whose element is the value of input list(s) in transformation function

# Diff in python2.x and python3.x
# python2.x map() return a list
# python3.x map() return map function address
#   - to convert to a list, use list comprehension list(map(xxx)) = [xxx]

# Example:
# Same add function as above
def add_function(a, b):
    return a + b

def square_function(x):
    return x ** 2

print("Example for map function")

l_function = list(map(square_function, range(1, 6)))
print("l_function: %s" %l_function)
l_lambda = list(map(lambda x: x ** 2, range(6)))
print("l_lambda: %s" %l_lambda)

# following example works as
# [0, 1, 2, 3, 4] +
# [0, 1]          =
# [0, 2]
l_lambda = list(map(lambda a, b: a + b, range(5), range(2)))
print("l_lambda: %s" %l_lambda)

print("\n")

# filter function
# Documentation: https://www.dataquest.io/blog/introduction-functional-programming-python/
# Key features:
# transform list into list
# transformation rule: function is a predict, aka filtering criteria
#                      1)function name 2) lambda function
#                      function takes ONLY ONE arguments, there is ONLY ONE input list
#                      output is part of the input list of elements that satisfy the predict criteria

# Example:
def isEvenNum(x):
    return x % 2 == 0

print("Example for filter function")

l_function = list(filter(isEvenNum, range(10)))
# Expected
# [0, 2, 4, 6, 8]
print("l_function: %s" %l_function)
l_lambda = list(filter(lambda x: x % 2 == 0, range(10)))
# Expected
# [0, 2, 4, 6, 8]
print("l_lambda: %s" %l_lambda)

# Diff between filter and map

# 1. Following example will have error
# TypeError: filter expected 2 arguments, got 3
# both_even = list(filter(lambda a, b: a % 2 == 0 and b % 2 == 0, range(6), range(6)))
# print("both_even: %s" %both_even)
# 2. map transform the value to the function, output length same as the min-length of all input lists
#    filter select element from input based on function criteria, output length is less or equal to the input list
l_map = list(map(lambda x: x % 2 == 0, range(4))) # [True, False, True, False]
print("l_map: %s" %l_map)
l_filter = list(filter(lambda x: x % 2 == 0, range(4))) # [0, 2]
print("l_filter: %s" %l_filter)

print("\n")

# reduce function
# Documentation: https://www.dataquest.io/blog/introduction-functional-programming-python/
# Key features:
# transform list into list
# transformation rule: a function that does a computation, and takes ONLY TWO inputs
#                      1)function name 2) lambda function
#                      function takes ONLY TWO arguments, there is ONLY ONE input list
#                      output A VALUE the input list of elements

# Example
# Same add function as above
def add_function(a, b):
    return a + b

print("Example for filter function")

# Note: in Python3.x, reduce was move under functools
from functools import reduce
val_function = reduce(add_function, range(5))
# Expected:
# 0 + 1 = 1;
#         1 + 2 = 3;
#                 3 + 3 = 6;
#                         6 + 4 = 10;
# return a value of 10
print("val_function: %d " %val_function)
val_lambda = reduce(lambda a, b: a + b, range(5))
# Expected:
# return a value of 10
print("val_lambda: %d " %val_lambda)

print("\n")

#################
# Comprehensions
#################

# Documentaion: https://www.dataquest.io/blog/introduction-functional-programming-python/
# Benefit:
#   - As alternative to map/filter
#   - More efficient and simple to write
# Rule can be either pre-defined function or lambda function
# Types:
#   - list comprehension (replacement of map or filter function)
#       - build list(s) to list
#   - set comprehension (python3 only)
#       - build set to set or build list to set
#   - dictionary comprehension (python3 only)
#       - build dict to dict
#   - generator comprehension

# Example:
# Same add function as above
def square(x):
    return x ** 2
def isEvenNum(x):
    return x % 2 == 0

print("Example for comprehension")

# list comprehension
l_origin = range(0, 4) # [0, 1, 2, 3]

# Compare with map function
l_map_function = [square(x) for x in l_origin]
# Expected:
# [0, 1, 4, 9]
print("l_map_function: %s" %l_map_function)
l_map_lambda = [x ** 2 for x in l_origin]
print("l_map_lambda: %s" %l_map_lambda)

# Compare with filter function
# Note that filter criteria function, name or lambda function
# all in the "if clause" at the end of comprehension
l_filter_function = [x for x in l_origin if isEvenNum(x)]
# Expected:
# [0, 2]
print("l_filter_function: %s" %l_filter_function)
l_filter_lambda = [x for x in l_origin if x % 2 == 0]
print("l_filter_lambda: %s" %l_filter_lambda)

# set comprehension
set_origin = {'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob'}
set_filtered = {s for s in set_origin if len(s) > 3}
# Expected:
# {'JOHN', 'ALICE', 'alice'}
print("set_filtered: %s" %set_filtered)
set_mapped = {s[0].upper() + s[1:].lower() for s in set_origin if len(s) > 3}
# Expected:
# {'John', 'Alice'}
print("set_mapped: %s" %set_mapped)

# dictionary comprehension
dict_origin = {'a':10, 'b': 34, 'A': 7, 'Z':3}
dict_filtered = {key: dict_origin[key] for key in dict_origin if key <= 'a'}
# Expected:
# {'a': 10, 'A': 7, 'Z': 3}
print("dict_filtered: %s" %dict_filtered)
dict_mapped = \
    {key.lower(): dict_origin.get(key.lower(), 0) + dict_origin.get(key.upper(), 0) for key in dict_origin}
# Expected:
# {'a': 17, 'b': 34, 'z': 3}
print("dict_mapped: %s" %dict_mapped)

print("\n")

#############
# Decorators
#############

# See python_decorator.py


#############
# Metaclass
#############

# Documentation:
# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python





