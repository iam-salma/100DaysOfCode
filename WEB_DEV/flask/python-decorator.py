# Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

# Functions can be nested in other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")
    nested_function()
outer_function()

# Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")
    return nested_function
inner_function = outer_function()
inner_function()


# Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

# With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

# Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()


# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        res = function(*args)
        print(f"It returned: {res}")
        return res
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1, 2, 3)


# TODO: Create the user login auth function 👇
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


# TODO: Create the func execution speed calc function 👇
import time

def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        # return res
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        var = i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        var = i * i

fast_function()
slow_function()