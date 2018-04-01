# Python Decorator
# This note is based on Python3

#############
# Decorators
#############

# Documentation:
# https://www.thecodeship.com/patterns/guide-to-python-function-decorators/
# Key features:
# - Take a function as argument
# - Return value assigned back to the passed in function

# Evolution of Decorater

# Step1: Assign function to a variable
def greet(name):
    return "Hi " + name

greet_someone = greet("Zhen")
# call "greet_someone" equivalent to "greet("Zhen")"
print(greet_someone)

# Step2: Define a function within a function
# In this example, locally define and use a function "getGreetingMsg()"
def greet(name):
    def getGreetingMsg():
        return "Hi "
    greetMsg = getGreetingMsg() + name
    return greetMsg
print(greet("Zhen"))

# Step3: Functions can be passed as parameters to other functions
# Like in Step2 example, function "getGreetingMsg()" can be defined outside function "greet(name)"
# and get passed in greet(name) as argument
def getGreetingMsg():
    return "Hi "

def greet(func): # greet will use other function as an argument
    name = "Zhen"
    return func() + name
# getGreetingMsg got passed into a function as an argument
# It's called nside of greet(func).
print(greet(getGreetingMsg))

# Step4: Functions can return other functions
# In other words, functions generating other functions.
def greetFunc():
    def getGreetingMsg():
        return "Hello there!"
    return getGreetingMsg
# Note that "composeGreetFunct()" -> returns the function "getGreetingMsg" address
# Need to add () to make a call on that returned function
print(greetFunc()())

# Step5: based on Step4, enclosed function has ONLY READ ACCESS to outside varibles
def greetFunc(name):          # decorator function
    def getGreetingMsg():     # enclosed function that defines decoration rules
        return "Hi " + name
    return getGreetingMsg     # return the decoration function as the return value of decorator
print(greetFunc("Zhen")())

# Step6: Simple version of decorator
# function to be decorated
def greet(name):
    return "Hi " + name
# decorator
def p_decorator(func):
    def funcWrapper(name):    # name here refers to argument of the passed in function greet(name)
        return "<p>" + func(name) + "</p>"
    return funcWrapper
# apply p_decorator upon function greet(name)
print(p_decorator(greet)("Zhen"))
                  # |---------------- p_decorator takes func as argument, so here use "greet"  not greet("Zhen")
                  #         |-------- p_decorator returns function funcWrapper, which takes name, same argument as
                  #                   as decorated function "greet".
                  #                   The final return value is defined in decoration logic and it's return value
# More flexible way of using decorated functions
decorated_greet = p_decorator(greet)
greetZhen = decorated_greet("Zhen")
greetNemo = decorated_greet("Nemo")
print("For Zhen: %s" %greetZhen)
print("For Nemo: %s" %greetNemo)

# Step 7: Python's syntax in using

@p_decorator
def greet(name):
    return "Hi " + name
print("For Papaya: %s" %greet("Papaya"))

# Note <IMPORTANT>:
# In the above example, function greet has been decorated by p_decorator
# test_result = p_decorator(greet)("Zhen") --> "<p><p>Hi Zhen</p></p>", double decorated by p_decorator
# Delete greet function for now
del greet

# Step 8: (Feature 1) multiple decorators can decorate on function at the same time
# Define more decorator function as examples
# Decorator that adds "Strong" tag around the text
def strong_decorator(func):
    def funcWrapper(name):
        return "<strong>" + func(name) + "</strong>"
    return funcWrapper
# Decorator that adds "div" tag around the text
def div_decorator(func):
    def funcWrapper(name):
        return "<div>" + func(name) + "<div>"
    return funcWrapper
# function to be decorated
def greet(name):
    return "Hi " + name

# Method 1: Using traditional (nexted function calls) to get the decorated result
trad_decorated = div_decorator(strong_decorator(p_decorator(greet)))("Zhen")
print("Traditional call: %s" %trad_decorated)
# Expected: Traditional call: <div><strong><p>Hi Zhen</p></strong><div>

# Method 2: Using python syntax
@strong_decorator
@p_decorator
@div_decorator
def greet(name):
    return "Hi " + name
python_decorated = greet("Zhen")
print("Python call: %s" %python_decorated)
del greet

# Python call: <strong><p><div>Hi Zhen<div></p></strong>
# Note that the result order are different based on how decorators listed above function

# Step 9: (Feature 2) decorators can accomodate functions of ANY arguments
# Example
"""
def div_decorator(func):                       # ---- func: function to be decorated
    def funcWrapper(name):                     # ---- name is argument that will passed in for the decorated func
        return "<div>" + func(name) + "<div>"  # ---- func(name) is essentially where decorated function being used
    return funcWrapper
decorated = greet("Zhen")                      # ---- This is the use case where name passed
"""
# This patten's limitation is that this decorator can only decorate function with ONLY ONE argument
# as func(name)
# To solve this issue and accomodate all sorts of functions

def p_decorator(func):
    def funcWrapper(*args, **kwargs):
        return "<p>" + func(*args, **kwargs) + "</p>"
    return funcWrapper

@p_decorator
def greet1(name):
    return "Hi " + name
@p_decorator
def greet2(firstName, lastName):
    return "Hi " + firstName + " " + lastName
kw_decorated_1 = greet1("Zhen")
kw_decorated_2 = greet2("Papaya", "Gua")
print("kw_decorated1: %s" %kw_decorated_1)
print("kw_decorated2: %s" %kw_decorated_2)

# Step 10: (Feature 3) Decorator can take arguments other than function name,
#          and decorator can use these arguments to customize decorator functionality
# In previous examples, decorators p_decorator, div_decorator, and strong_decorator are doing similar
# jobs, and can be generalized in one decorator (say tag_decorator) with different tag value passed in
# as arguments
def tags(tagValue):                            # Passing argument to decorator means an extra layer of logic
    def tag_decorator(func):                   # The previous decorator func of no arguments
        def funcWrapper(*args, **kwargs):      # enclosed function has read access to outside "tagValue"
            return "<" + tagValue + ">" + \
                    func(*args, **kwargs) + \
                    "</" +tagValue + ">"
        return funcWrapper                     # Return funcWrapper function
    return tag_decorator                       # Return the decorator function

@tags("underscore")
def greet(name):
    return "Hi " + name
tag_decorated = greet("Zhen")
print("tag_decorated: %s" %tag_decorated)
# Expected:
# tag_decorated: <underscore>Hi Zhen</underscore>

print("test: %s" %tags("test")(greet)("Gua"))
                        # |------------------- tags("test") -> return a tag_decorator function with tagValue "test"
                        #         |----------- tags("test")(greet) -> return funcWrapper function passed in greet
                        #                |---- tags("test")(greet)("Gua") -> return wrapped value by calling function greet with passed in argument "Gua"
# Expected:
# test: <test><underscore>Hi Gua</underscore></test>
