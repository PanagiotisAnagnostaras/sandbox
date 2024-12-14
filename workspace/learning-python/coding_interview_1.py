# https://codeinterview.io/blog/python-coding-interview-questions/
## Beginners
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 1")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# What is the output
var1 = 7
var2 = 2
result = var1 // var2 + var1 % var2
print(result)

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 2")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# What is wrong here
# def concatenate_strings(str1, str2):
# 	return str1 + " " + str2

# result = concatenate_strings("Test", 3)
# print(result)

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 3")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# What is wrong here
# def print_uppercase(text):
#     for letter in text:
#       print(f"letter = {letter} text = {text}")
#       print(letter.upper())

# print_uppercase(["Test", "Python"])


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 4")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# Write a method that calculates the simple interest on a loan.
# The program should take user input for the principal amount, the annual interest rate (as a percentage),
# and the time to pay in years. The program should calculate and display the total amount (principal + interest) after the specified time.


class Inputs:
    def __init__(self, principal_amount: float, years: float, interest: float):
        self.principal_amount = principal_amount
        self.years = years
        self.interest = interest


def receive_inputs():
    principal_amount = float(input("give me the principal amount \n"))
    interest = float(input("give me the interest in % \n")) / 100
    years = float(input("give me the years \n"))
    inputs = Inputs(principal_amount=principal_amount, years=years, interest=interest)
    return inputs


def compute_final_amount(inputs: Inputs):
    years = inputs.years
    interest = inputs.interest
    principal_amount = inputs.principal_amount
    full_years = int(years)
    remaining_years = years - full_years
    print(f"full years = {full_years} remaining years = {remaining_years}")
    final_amount = principal_amount
    for year in range(full_years):
        final_amount += interest * final_amount
    final_amount += remaining_years * interest * final_amount
    print(f"final amount = {final_amount}")


# inputs = receive_inputs()
# compute_final_amount(inputs)


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 5")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


# What will be the output of this one
def test(x, y=[]):
    print(f"1) address of x = {id(x)} , y = {id(y)}")
    y.append(x)
    return y


print(f"2) {test(1)}")  # [1]
print(f"3) {test(2)}")  # [1, 2]

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 6")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

name = "Kostas"
if name == "John" or "Brian":
    print("Welcome, John or Brian!")
else:
    print("You're not John or Brian.")

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 7")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

x = "2"  # input("provide first number\n")
y = "10"  # input("provide second number\n")
op = "-"  # input("provide operation (+ | - | * | /)")
if op not in ["+", "-", "*", "/"]:
    print("invalid op")
else:
    print(f"x = {x} type = {type(x)}")
    print(f"y = {y} type = {type(y)}")
    print(f"op = {op} type = {type(op)}")
    result = eval(x + op + y)
    print(f"result = {result} type = {type(result)}")

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 8")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# What is the output
numbers = [5, 1, 9, 3, 7]
squared_numbers = list(map(lambda x: x**2, numbers))  # [25, 1, 81, 9, 49]
squared_numbers.sort(reverse=True)  # [81, 49, 25, 9, 1]
print(squared_numbers[:3])  # [ 81, 49, 25]
print(squared_numbers[-3:])  # [25, 9, 1]


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 9")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# what is wrong here
# import requests
# url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url)
# data = response.json()

# email_addresses = [user["email"] for user in data if user["company"]["catchPhrase"].contains("fintech")]
# print(email_addresses)

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 10")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
## What is wrong here -> cannot change size during iteration
# numbers = {1: "one", 2: "two", 3: "three"}
# for number in numbers:
#     print(number)
#     if numbers[number] == "two":
#         del numbers[number]
# print(numbers)


## Mid-Level
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 11")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

## What is wrong here
print("1) entered Question 1")


def caching_decorator(func):
    print("3) Entered caching_decorator")
    cache = {}

    def wrapper(*args):
        print("5 & 8) entered wrapper")
        if args in cache:
            print("9) found it in memory")
            return cache[args]
        print("6) I have to compute it")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


print("2) Point 1")


@caching_decorator
def add(a, b):
    print("7) entered add")
    return a + b


print("4) calling add 1st time")
add(3, 5)
print("9) calling add 2nd time")
add(3, 5)

# Question 12:
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 12")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


## What is the output here:
def test_function():
    try:
        return "In try"
    finally:
        return "In finally"


result = test_function()
print(result)

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 13")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# Develop a task scheduler that runs a specific function after a certain period of time.
# The scheduler should take user input for the function to run, the time interval (in seconds)
# between each run, and the total number of runs. Use Python’s threading or multiprocessing module
# to develop the scheduler
# import threading
# import time
# import typing
# fun = input("please provide the method to run\n")
# time_interval = float(input("please provide the time interval\n"))
# number_of_runs = int(input("please provide the number of runs\n"))

# ran_already = 0
# threads = []
# while ran_already<=number_of_runs-1:
#     time.sleep(time_interval)
#     threads.append(threading.Thread(target=lambda: eval(fun)))
#     threads[-1].start()
#     ran_already += 1
# for thread in threads:
#     threads: typing.List[threading.Thread]
#     thread.join()


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 15")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# # What will be the output of the below code:
# import threading
# counter = 0
# print("without lock")
# def increment_counter():
#     global counter
#     for _ in range(100_000):
#         counter += 1 # race condition: this is a non atomic operation (involves three steps: read, append, write back). Race condition between threads

# threads = [threading.Thread(target=increment_counter) for _ in range(10)]
# [thread.start() for thread in threads]
# [thread.join() for thread in threads]

# print(counter) # 100_000 * 10 != 832_891

# print("with lock")
# counter = 0
# lock = threading.Lock()
# def increment_counter():
#     global counter
#     for _ in range(100_000):
#         with lock:
#             counter += 1

# threads = [threading.Thread(target=increment_counter) for _ in range(10)]
# [thread.start() for thread in threads]
# [thread.join() for thread in threads]

# print(counter) # 100_000 * 10 = 1_000_000


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 16")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


# What will be the output of the below code:
def outer_function():
    value = "Say cheese to"

    def inner_function1():
        nonlocal value
        value = "Python"

    def inner_function2():
        global value
        value = "Engineers"

    inner_function1()
    inner_function2()
    return value


value = "Programming"
result = outer_function()
print(value, result)


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 17")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# # What is wrong with below code:
# import requests
# def fetch_data(api_url):
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         return response.json()
#     except requests.HTTPError as e:
#         print("Error: ", e)

# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# data = fetch_data(api_url)
# print(data["title"])


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 18")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


# Develop a Python function that reads a text file and calculates the metadata, including the number of lines,
# words, and characters in the file. You can ignore whitespaces and punctuation when counting characters.
# There will be only one input to this program: the text file. After processing, the result will be printed.
def calculate_file_metadata(filepath):
    number_of_lines, number_of_words, number_of_chars = 0, 0, 0
    try:
        with open(file=filepath) as file:
            lines = file.readlines()
            number_of_lines = len(lines)
            for line in lines:
                words = line.split()
                number_of_words += len(words)
                number_of_chars += sum(list(map(len, words)))

    except:
        print(f"function = {calculate_file_metadata.__name__} failed")
        return
    print(
        f"number of lines = {number_of_lines}\nnumber of words = {number_of_words}\nnumber of chars = {number_of_chars}"
    )


file_path = "Dockerfile"
calculate_file_metadata(file_path)


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 19")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

data = [
    {"id": 1, "name": "Helen", "age": 28},
    {"id": 2, "name": "Chris", "age": 49},
    {"id": 3, "name": "Jennifer", "age": 19},
]
result = {item["name"]: item["age"] for item in data if item["age"] > 20}
print(result)


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 20")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# Implement two versions of a function that generates the first n Fibonacci numbers. The first version of the function should
# be a regular function that returns a list of Fibonacci numbers, while the other version
# should be a generator function that produces Fibonacci numbers one at a time. Compare both implementations’ memory usage and runtime performance and share your results.
import time


def fib_v1(n: int):
    fib_list = [0, 1]
    for _ in range(n - 2):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


def fib_v2(n):
    a, b, length = 0, 1, 0
    while True:
        length += 1
        yield a
        if length == n:
            break
        a, b = b, a + b


n = 1_000
start = time.time()
fib1 = fib_v1(n)
end = time.time()
print(f"v1 took {end-start} sec, length = {len(fib1)}")
start = time.time()
fib2 = [it for it in fib_v2(n)]
end = time.time()
print(f"v2 took {end-start} sec, length = {len(fib2)}")
print(fib1 == fib2)

## Advanced
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 21")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# What is the issue here
class MyResource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Acquiring {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Releasing {self.name}")
 
def use_resource():
    with MyResource("Resource A") as res_a, MyResource("Resource B") as res_b:
        raise Exception("An error occurred")
        
 
try:
    use_resource()
except Exception as e:
    print(e)

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 22")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# What is the output
class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs["greeting"] = "Hello, Python Engineers!"
        return super().__new__(cls, name, bases, attrs)
    
class MyClass(metaclass=Meta):
    pass
obj = MyClass()
print(obj.greeting)


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 23")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# What will be the output of the below code:
class DynamicAttributes:
    def __getattr__(self, name):
       return name.upper()
    def __getattribute__(self, name):
        if name.startswith("get_"):
            return super().__getattribute__(name[4:])
        raise AttributeError
dyn = DynamicAttributes()
print(dyn.get_foo)