from typing import List
from copy import deepcopy

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print(" 1 - types")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

## immutable
### int
x_int = 1
print(f"1) id before = {id(x_int)}")
x_int = 2
print(f"2) id after = {id(x_int)}")
### float
x_float = 1.0
### bool
x_bool = True
### string
x_string = "x"
### tuple
x_tuple = (0, 1, 2)

## mutable
### list
x_list = [0, 1, 2]
print(f"3) id before = {id(x_list)}")
x_list = [3, 4, 5]
print(f"4) id after = {id(x_list)}")
x_list[0] = 4
print(f"5) id after = {id(x_list)}")
### dict
x_dict = {"a": 0, "b": 1}
### set
x_set = {0, 1, 2}
print(x_set)
x_set = {0, 1, 2, 2}
print(x_set)

## iterations
for key in {"one": 1, "two": 2, "three": 3}:
    print(key)

for key, val in {"one": 1, "two": 2, "three": 3}.items():
    print(f"key = {key}, val = {val}")

d = {"one": 1, "two": 2, "three": 3}
for key in d:
    print(key)
    if d[key] == 3:
        # del d[key] -> RuntimeError: dictionary changed size during iteration
        pass
l = [0, 1, 2, 3, 4]
print(f"before = {l}")
for val in l:
    if val == 3:
        del l[val]  # this is fine
print(f"after = {l}")

# lists
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"6) x = {x}")
print(f"7) x[2:]={x[2:]}")  # 2,3,4,5,6,7,8,9
print(f"8) x[:2] = {x[:2]}")  # 0,1
print(f"9) x[4:9:3] = {x[4:9:3]}")  # 4,7
print(f"10) x[::3] = {x[::3]}")  # 0,3,6,9
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("2 - type conversions")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# python is dynamically typed so you can do
a: float = 2.0
b: int = 2
c: str = "hello"


# Print function with alignment
def print_variables(a, b, c, label):
    print(f"{label}) a = {str(a):<10} of type {str(type(a)):<20} at address {id(a):<20} " f"b = {str(b):<10} of type {str(type(b)):<20} at address {id(b):<20} " f"c = {str(c):<10} of type {str(type(c)):<20} at address {id(c):<20}")


print_variables(a, b, c, "1")
a = b
print_variables(a, b, c, "2")
b = c
print_variables(a, b, c, "3")
c = a
print_variables(a, b, c, "4")


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("3 - functions and args and kwargs")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


def myfun1(*args):
    print(f"1) arg = {args}")
    print(f"2) type = {type(args)}")


def myfun2(**kwargs):
    print(f"3) {kwargs}")
    print(f"4) {type(kwargs)}")


def myfun3(x, *args, **kwargs):
    print(f"5) x = {x}")
    print(f"6) args = {args}")
    print(f"7) kwargs = {kwargs}")


myfun1(x_int, x_float)
myfun2(first=x_list, second=x_dict)
myfun3(1, 2, 3, first="Geeks", mid="for", last="Geeks")


def myfun4(*args, args_cache=[]):
    print(f"8) function called with args = {args} at {id(args)} and args_cache = {args_cache} at {id(args_cache)}")
    args_cache.append(args)


myfun4("dog")
myfun4("cat")
myfun4("you")

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("4 - assignment by reference or by copy")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
x = 1
y = 2
print(f"1) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")
x = y
print(f"2) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")
y = 3
print(f"3) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")

x = [1, 2]
y = ["a", "b"]
print(f"4) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")
x = y
print(f"5) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")

y = ["c", "d"]
print(f"6) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")
x = y
y[0] = "cc"
print(f"7) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")

x = 0
y = x
print(f"8) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")
x = 0
y = deepcopy(x)
print(f"9) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")

x = [0]
y = x
print(f"10) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")
x = [0]
y = deepcopy(x)
print(f"11) x = {x} (address = {id(x)}) , y = {y} (address = {id(y)})")


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("5 - pass by reference or by copy")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


def modify_1(x: int):
    print("inside modify_1")
    print(f"a) x = {x} (address = {id(x)})")
    x = 2
    print(f"b) x = {x} (address = {id(x)})")
    return True


def modify_2(x: List[int]):
    print("inside modify_2")
    print(f"a) x = {x} (address = {id(x)})")
    x.append(2)
    print(f"b) x = {x} (address = {id(x)})")
    return True


def modify_3(x: List[int]):
    print("inside modify_3")
    print(f"a) x = {x} (address = {id(x)})")
    x = [0, 1, 2]
    print(f"b) x = {x} (address = {id(x)})")
    return True


def modify_4(x: List[List[int]]):
    print("inside modify_4")
    print(f"a) x = {x} (address = {id(x)})")
    x[0] = [0, 1, 2]
    print(f"b) x = {x} (address = {id(x)})")


def modify_5(x: List[List[int]]):
    print("inside modify_5")
    print(f"a) x = {x} (address = {id(x)})")
    x = [[0, 1, 2], [3, 4, 5]]
    print(f"b) x = {x} (address = {id(x)})")


def modify_6(x: List[List[int]]):
    print("inside modify_6")
    print(f"a) x = {x} (address = {id(x)}) x[0] = {x[0]} (address = {id(x[0])})")
    y = x[0]
    print(f"b) x = {x} (address = {id(x)}) x[0] = {x[0]} (address = {id(x[0])}) y = {y} (address = {id(y)})")
    y.append([[1], [2]])
    print(f"c) x = {x} (address = {id(x)}) x[0] = {x[0]} (address = {id(x[0])}) y = {y} (address = {id(y)})")
    y = [0]
    print(f"d) x = {x} (address = {id(x)}) x[0] = {x[0]} (address = {id(x[0])}) y = {y} (address = {id(y)})")


print(f"0) Initial = {x_list} (address = {id(x_list)})")
modify_1(x_list)
print(f"1) After modify_1 = {x_list} (address = {id(x_list)})")
modify_2(x_list)
print(f"2) After modify_2 = {x_list} (address = {id(x_list)})")
modify_3(x_list)
print(f"3) After modify_3 = {x_list} (address = {id(x_list)})")
modify_4(x_list)
print(f"4) After modify_4 = {x_list} (address = {id(x_list)})")
modify_5(x_list)
print(f"5) After modify_5 = {x_list} (address = {id(x_list)})")
modify_6(x_list)
print(f"6) After modify_6 = {x_list} (address = {id(x_list)})")

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("6 - exception handling")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

try:
    x = 2 / 0
except ZeroDivisionError:
    print("1) you cannot divide by zero")
finally:
    print("2) but lets forget about it")

try:
    x = 2 / 0
except:
    print("3) something went wrong")
finally:
    print("4) but lets forget about it")

try:
    x = 2 / 0
except OverflowError:
    print(" did it overflow?")
except:
    print("5) caught it")
finally:
    print("6) but I dont know what it is")

try:
    try:
        x = 2 / 0
    except OverflowError:
        print("")
    except:
        raise Exception("8) Unknown exception occurred")
    finally:
        print("7) whatever")
except Exception as e:
    print(e)

try:
    print("8) try")
except:
    print("9) void")
else:
    print("10) else")
finally:
    print("11) finally")


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("7 - with keyword")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


class oneClass:
    def __init__(self, name: str) -> None:
        print("a) inside init")
        self.name = name

    def __enter__(self):
        print("b) inside enter")
        return ["this is completely irrational"]

    def __exit__(self, *args):
        print("c) inside exit")

    def __str__(self) -> str:
        return f"I am an object and this is my name {self.name}"


print("1) before init")
ob = oneClass(name="panos")
print("2) after init")
with ob as some:
    print(f"3) do something with {some}")
print("4) finished doing something")
print(f"5) the object was {ob}")


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("8 - magic methods (or dunder:=double underscore methods)")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


class OneClass:
    def __new__(cls):
        print("1) Creating instance")

    def __init__(self) -> None:
        print("1) instance is initialized")


ob = OneClass()  # here only the __new__ is called


class OneClass:
    def __new__(cls):
        print("2) Creating instance")
        return super(OneClass, cls).__new__(cls)

    def __init__(self) -> None:
        print("2) instance is initialized")


ob = OneClass()


class FakeClass:
    name = "kostas"

    def __getattribute__(self, name: str):
        # print("inside __getattribute__")
        super().__getattribute__(name)

    def __getattr__(self, name: str):
        # print("inside __getattr__")
        super().__getattr__(name)


print(f"3) creating object")
ok = FakeClass()
print(f"4) accessing existing attribute")  # calls __getattribute__
ok.name
print(f"5) accessing missing attribute")  # calls __getattribute__ and then __getattr__
try:
    ok.asdafdfdsushf
except AttributeError:
    pass

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("9 - ABC")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# stands for abstract base class
import abc


# manually registering classes by .register()
class BaseClass_a(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        print("BaseClass_a init")


class DerivedClass_a1:
    def __init__(self) -> None:
        print("DerivedClass_a1 init")


class DerivedClass_a2:
    def __init__(self) -> None:
        print("DerivedClass_a2 init")


BaseClass_a.register(DerivedClass_a1)
BaseClass_a.register(DerivedClass_a2)
print(f"1) {isinstance(DerivedClass_a1(), BaseClass_a)}")
print(f"2) {isinstance(DerivedClass_a2(), BaseClass_a)}")
print(f"3) {issubclass(DerivedClass_a1, BaseClass_a)}")
print(f"4) {issubclass(DerivedClass_a2, BaseClass_a)}")


# manually registering classes by @cls.register decorator
class BaseClass_b(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        print("BaseClass_b init")


@BaseClass_b.register
class DerivedClass_b1:
    def __init__(self) -> None:
        print("DerivedClass_b1 init")


class AnotherClass_b1:
    def __init__(self) -> None:
        print("AnotherClass_b1 init")


print(f"5) {issubclass(DerivedClass_b1, BaseClass_b)}")
print(f"6) {issubclass(AnotherClass_b1, BaseClass_b)}")


# automated way to register subclasses based on method implementation
class BaseClass_c(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        print(subclass)
        myFun = getattr(subclass, "myFun", None)
        return callable(myFun)


class DerivedClass_c:
    def __init__(self) -> None:
        print("DerivedClass_c init")

    def myFun(self):
        pass


class AnotherClass_c:
    def __init__(self) -> None:
        print("AnotherClass_c init")

    def anotherFun(self):
        pass


print(f"7) {issubclass(DerivedClass_c, BaseClass_c)}")  # when issubclass is called the __subclasshook__ is executed
print(f"8) {issubclass(AnotherClass_c, BaseClass_c)}")


# forcing derived class to overwrite a method of the parent class
class BaseClass_d(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def doSomething(self):
        pass


class DerivedClass_d1(BaseClass_d):
    def doSomething(self):
        print("overwrote")


class DerivedClass_d2(BaseClass_d):
    def doSomethingElse(self):
        print("didn't overwrite")


print(f"9) {issubclass(DerivedClass_d1, BaseClass_d)}")
print(f"10) {issubclass(DerivedClass_d2, BaseClass_d)}")

# ob1 = BaseClass_d() -> this throws an error due to the abstract method
ob2 = DerivedClass_d1()
# ob3 = DerivedClass_d2() -> this throws an error due to the abstract method

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("10 - some underscores")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

x = 10_000_000.0
print(x)


class oneClass:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self._y = y
        self.__z = z


oneOb = oneClass(1, 2, 3)
print(f"1) {oneOb.x}")
print(f"2) {oneOb._y}")
# print(f"3) {oneOb.__z}") -> this is called Mangling it fails
print(f"4) {oneOb._oneClass__z}")  # wow


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("11 - decorators")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


class SomeClass:
    name = "Panos"

    def __init__(self, age) -> None:
        self.__age = age

    @classmethod
    def getName(cls):  # first argument is cls
        return cls.name

    @staticmethod
    def doSomething():  # no arguments, can have but it must not access cls or self
        return "hey"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val):
        self.__age = val + 100_000

    @age.deleter
    def age(self):
        del self.__age


ob = SomeClass(2)
print(f"1) {ob.age}")
ob.age = 1  # Note it is an assignment not a call
print(f"2) {ob.age}")
del ob.age
try:
    print(f"3) {ob.age}")
except:
    print("3) it has gone")


# Some stuff with functions
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(f"4) {add_15(10)}")

# Create a decorator which doesn't return something
import time
import math


def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("6) Total time taken in : ", func.__name__, end - begin)

    return inner1


@calculate_time
def factorial(num):
    time.sleep(0.01)
    print(f"5) { math.factorial(num)}")


factorial(10)


# Create a decorator which returns a value
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")
        returned_value = func(*args, **kwargs)
        print("after Execution")
        return returned_value

    return inner1


@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("6) Sum =", sum_two_numbers(a, b))


def mydecoration(func):
    cached = {}
    print(f"mydecoration")

    def wrapper(*args):
        print(f"wrapper")
        if args in cached.keys():
            print("returning cached")
            return cached[args]
        else:
            print("returning computed")
            res = func(*args)
            cached[args] = res
            return res

    return wrapper


@mydecoration
def add(x, y):
    return x + y


add(1, 1)
add(1, 2)
add(1, 1)


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("12 - multi threading")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# Develop a task scheduler that runs a specific function after a certain period of time.
# The scheduler should take user input for the function to run, the time interval (in seconds)
# between each run, and the total number of runs. Use Python’s threading or multiprocessing module
# to develop the scheduler
import threading
import time
import typing

fun = 'print("hey")'  # input("please provide the method to run\n")
time_interval = 0.2  # float(input("please provide the time interval\n"))
number_of_runs = 5  # int(input("please provide the number of runs\n"))

ran_already = 0
threads = []
while ran_already <= number_of_runs - 1:
    time.sleep(time_interval)
    threads.append(threading.Thread(target=lambda: eval(fun)))
    threads[-1].start()
    ran_already += 1
for thread in threads:
    threads: typing.List[threading.Thread]
    thread.join()

print("~~~~~~~~~~~~~~~~~~~~~~~~")
# sharing data among threads
x = []
print(f"1) before = {x}")
threads = []
names = ["thread_1", "thread_2", "thread_3"]
for name in names:
    threads.append(threading.Thread(target=lambda x: [x.append(name) for _ in range(3)], args=(x,)))
for thread in threads:  # here happens late binding: x has the last value
    thread.start()
for thread in threads:
    thread.join()
print(f"2) after = {x}")
# try again
x = []
print(f"3) before = {x}")
threads = []
for name in names:
    threads.append(threading.Thread(target=lambda x, name=name: [x.append(name) for _ in range(3)], args=(x,)))
for thread in threads:  # here late binding doesn't happen because we store the var in runtime
    thread.start()
for thread in threads:
    thread.join()
print(f"2) after = {x}")
# one more example
threads = []
f = lambda name: [print(name) for _ in range(10)]
for name in names:
    threads.append(threading.Thread(target=f, args=(name,)))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()


shared_resource = 0


class myLock:
    def __init__(self, name) -> None:
        self.name = name
        self.lock = threading.Lock()

    def __enter__(self):
        self.lock.acquire()
        return self

    def __exit__(self, *args):
        self.lock.release()


lock_instance = myLock("my_resource_lock")


def threadFunWithLock():
    global shared_resource
    for _ in range(100_000):
        with lock_instance as lock:
            shared_resource += 1


threads = []
for _ in range(2):
    threads.append(threading.Thread(target=threadFunWithLock))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"3) sum with lock = {shared_resource}")

shared_resource = 0


def threadFunWithoutLock():
    global shared_resource
    for _ in range(100_000):
        shared_resource += 1


threads = []
for _ in range(2):
    threads.append(threading.Thread(target=threadFunWithoutLock))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"4) sum without lock = {shared_resource}")

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("13 - multi processing")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# ToDo panos
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("14 - inheritance")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


class A:
    def __init__(self) -> None:
        print("A init")


class B1(A):
    def __init__(self) -> None:
        super().__init__()
        print("B1 init")


class B2(A):
    def __init__(self) -> None:
        print("B2 init")


print("Creating A")
A()
print("Creating B1")
B1()
print("Creating B2")
B2()


class C1:
    def __init__(self) -> None:
        print("C1 init")


class C2:
    def __init__(self) -> None:
        print("C2 init")


class D1(C1, C2):
    def __init__(self) -> None:
        super().__init__()
        print("D1 init")


class D2(C1, C2):
    def __init__(self) -> None:
        C1.__init__(self)
        C2.__init__(self)
        print("D2 init")


print("Creating D1")
D1()
print("Creating D2")
D2()


class E:
    def __init__(self) -> None:
        print("E init")


class F1(E):
    def __init__(self) -> None:
        super().__init__()
        print("F1 init")


class F2(E):
    def __init__(self) -> None:
        super().__init__()
        print("F2 init")


class G(F1, F2):
    def __init__(self) -> None:
        super().__init__()
        print("G init")


print("Creating G")  # diamond inheritance
G()
# Here things get interesting:
# read about MRO https://python-history.blogspot.com/2010/06/method-resolution-order.html


class Abstract(metaclass=abc.ABCMeta):
    def __init__(self, abstract_state) -> None:
        self.__state = abstract_state

    @abc.abstractmethod
    def run():
        pass


class Dog(Abstract):
    def __init__(self, abstract_state) -> None:
        super().__init__(abstract_state)

    def eat_cats():
        pass

    def run():
        print("dog runs")

    def exploit_abstract(self):
        print(self._Abstract__state)


class Cat(Abstract):
    def eat_mice():
        pass

    def run():
        print("cat runs")

    def exploit_abstract(self):
        # print(self.__state) -> this fails
        pass


dog = Dog("My child is a dog")
cat = Cat("My child is a cat")
dog.exploit_abstract()
cat.exploit_abstract()


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("15 - mod div")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
x = 7
y = 2
print(f"x = {x} y = {y} x//y = {x//y} , x%y = {x%y}")


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("16 - string manipulation")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# split upper, lower
# ToDo panos

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("17 - common methods")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# append, upper, hasatrr, isinstance, getattr, callable, list, sort
my_list = [0, 23, 3, 2, 5]
print(f"1) before = {my_list}")
my_list.sort()
print(f"2) sorted = {my_list}")
my_list.sort(reverse=True)
print(f"3) sorted reverse = {my_list}")

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("18 - assertions")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

# here nothing is printed but you got it
x = 0
try:
    assert x != 0, "1) x cannot be zero"
except:
    pass

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("19 - list comprehension")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
myList = [x for x in range(10) if x % 2 == 0]
print(f"1) {myList}")

check = lambda x: x % 2 == 0
myList = [x for x in range(10) if check(x)]
print(f"2) {myList}")


def genFun():
    n = 10
    i = 0
    while i < n:
        i += 1
        yield (i - 1) if (i - 1) % 2 == 0 else None


generator = genFun()
myList = [y for y in [x for x in generator] if y is not None]
print(f"3) {myList}")

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("20 - lambda functions and map")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


def f(x):
    return x * 2


lambda x: x * 2
l_f = lambda x: x * 2
print(f"1) normal function {f(2)}")
print(f"2) lambda function {(lambda x: x*2)(2)}")
print(f"3) lambda again {l_f(2)}")

collection_list = [0, 1, 2, 3, 4]
collection_tuple = (0, 1, 2, 3, 4)
list_mapped = map(lambda x: x**2, collection_list)  # this is a map object (iterable) that why you call list afterwards
tuple_mapped = map(lambda x: x**2, collection_tuple)
print(f"4) collection list before {collection_list} and after {list(list_mapped)}")
print(f"5) collection tuple before {collection_tuple} and after {list(tuple_mapped)}")

lambda x, y: x * y
list_and_tuple_mapped = map(lambda x, y: x * y, collection_list, collection_tuple)
print(f"6) apply map to 2 collections {tuple(list_and_tuple_mapped)}")


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("21 - scope")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

x = "x"
print(f"1) global x = {x} at {id(x)}")


def f1():
    print(f"2) inside f1 x = {x} at {id(x)}")


f1()


def f2():
    print(f"4) inside f2 xyz = {xyz} at {id(xyz)}")


xyz = "xyz"
print(f"3) global xyz = {xyz} at {id(xyz)}")
f2()


# here we create a local var inside the function with the same name

y = "y"


def f3():
    print(f"5) f3 y = {y} at {id(y)}")
    # This program will SHOW error
    # if we uncomment below line.
    # y = "y"
    print(f"6) f3 y = {y} at {id(y)}")


f3()

x = "x"
print(f"7) global x = {x} at {id(x)}")


def f4():
    global x
    print(f"8) f4 x = {x} at {id(x)}")
    x = "y"
    print(f"9) f4 x = {x} at {id(x)}")


f4()
print(f"10) f4 x = {x} at {id(x)}")

print("~~~~~~~~~~~~~~~~~~~~~~~~")
# global keyword
# without global
x = "awesome"


def myfunc():
    x = "fantastic"
    print("1) Python is " + x)


myfunc()
print("2) Python is " + x)
# with global
x = "awesome"


def myfunc():
    global x
    x = "fantastic"
    print("3) Python is " + x)


myfunc()
print("4) Python is " + x)

print("~~~~~~~~~~~~~~~~~~~~~~~~")
# nonlocal keyword example 1
x = "0"


def myfunc1():
    x = "1"

    def myfunc2():
        nonlocal x
        x = "2"

        def myfunc3():
            nonlocal x
            x = "3"

        myfunc3()

    myfunc2()
    print(f"1) inside myfunc1 = {x}")


myfunc1()
print(f"2) global x = {x}")

# nonlocal keyword example 2
x = "0"


def myfunc1():
    x = "1"

    def myfunc2():
        nonlocal x
        x = "2"

        def myfunc3():
            global x  # -> it doesn't override the inner scope
            x = "3"

        myfunc3()

    myfunc2()
    print(f"4) inside myfunc1 = {x}")


myfunc1()
print(f"5) global x = {x}")

# nonlocal keyword example 3


def outer():
    a = 5

    def inner():
        nonlocal a
        a = 10

    inner()
    print(f"6) {a}")  # 10


outer()


def outer():
    a = 5

    def inner():
        a = 10

    inner()
    print(f"7) {a}")


outer()


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("22 - generators")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


# A generator function in Python is defined like a normal function, but whenever it needs
# to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function
# automatically becomes a Python generator function.
def iter_fun():
    yield 1
    yield 2


for it in iter_fun():
    print(f"1) it = {it}")

# generator functions return a generator object which is an iterator
it = iter_fun()
print(f"2) {it.__next__()}")
print(f"2) {it.__next__()}")


# The yield statement suspends a function’s execution and sends a value back to the caller, but retains
# enough state to enable the function to resume where it left off. When the function resumes, it continues execution immediately after the last yield run. This allows
# its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
def gen():
    print("3) ")
    yield 0
    print("4) ")
    yield 1
    print("5) ")
    yield 2
    print("6) ")
    yield 3


for it in gen():
    pass
it = gen()
it.__next__()
it.__next__()
it.__next__()
it.__next__()


# generator function for fibonacci
def fib_it(n):
    a, b, length = 0, 1, 0
    while True:
        length += 1
        yield a
        if length == n:
            break
        a, b = b, a + b


fib_list = [number for number in fib_it(10)]
print(fib_list)


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("24 - metaclasses")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


# Taken from
# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
# https://medium.com/@miguel.amezola/demystifying-python-metaclasses-understanding-and-harnessing-the-power-of-custom-class-creation-d7dff7b68de8


# Introduction
class aClass:
    def __init__(self) -> None:
        pass


anObject = aClass()
print(f"1) class = {aClass} at address {id(aClass)} and type = {type(aClass)}")
print(f"2) object = {anObject} at address {id(anObject)} and type = {type(anObject)}")

class_var = aClass
class_var.amIaClass = True
print(f"3) is class_var a class {class_var.amIaClass} type = {type(class_var)} address = {id(class_var)}")
print(f"4) is aClass a class {aClass.amIaClass} type = {type(aClass)} address = {id(aClass)}")


# here type is used to create a class on the fly
class classA:
    pass


classB = type("classA", (), {})

print(f"5) classA = {classA} at address {id(classA)} and type = {type(classA)}")
print(f"6) classB = {classB} at address {id(classB)} and type = {type(classB)}")

# lets spicy it up
sr = lambda self, x: print(f"7) square root of {x} is {math.sqrt(x)}")
classCalculator = type(
    "classC",
    (),
    {"squared": lambda self, x: print(f"8) {x} squared is {x**2}"), "square_root": sr},
)
myCalc = classCalculator()
myCalc.square_root(4)
myCalc.squared(4)


def division(self, x):
    print(f"9) {x} divided by 2 is {x/2}")


classCalculator.forgotDivision = division
myCalc.forgotDivision(4)  # this is crazy
myCalc.forgotAddition = lambda x: x + 2
print(f"10) 4 plus 2 is {myCalc.forgotAddition(4)}")
myFakeCalc = classCalculator()
try:
    addition = getattr(myCalc, "forgotAddition")
    isFun = callable(addition)
except AttributeError:
    isFun = False
finally:
    print(f"11) myCalc has addition method = {isFun}")
try:
    addition = getattr(myFakeCalc, "forgotAddition")
    isFun = callable(addition)
except AttributeError:
    isFun = False
finally:
    print(f"12) myFakeCalc has addition method = {isFun}")

# Now that we saw how to create class objects with the method type() let's go to metaclasses


class MyMetaClass_v1(type):
    def __new__(cls, name, bases, attrs):
        # do stuff here
        return super().__new__(cls, name, bases, attrs)

    def __init__(self, name, bases, attrs):
        # do stuff here
        return super().__init__(name, bases, attrs)


class MyMetaClass_v2(type):
    def __new__(cls, name, bases, attrs):
        attrs["this_is_a_method"] = lambda self: print("called method class")
        attrs["this_is_a_attr"] = 2
        return super().__new__(cls, name, bases, attrs)


class normalClass_1(metaclass=MyMetaClass_v2):
    pass


class normalClass_2(MyMetaClass_v2):
    pass


ob_1 = normalClass_1()
print(f"13) attr = {ob_1.this_is_a_attr}")


# like an interface
class metaClass(type):
    def __new__(cls, name, bases, attrs):
        print(f"14) this class has the following attrs = {attrs}")
        if "print_name" not in attrs:
            raise NotImplementedError
        return super().__new__(cls, name, bases, attrs)


class ClassA(metaclass=metaClass):
    name = None
    age = None

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def print_name(self):
        print(f"15) my name is {self.name}")


o = ClassA("Kostas", 23)
o.print_name()

try:

    class ClassB(metaclass=metaClass):
        def __init__(self, name, age) -> None:
            self.name = name
            self.age = age

        def print_age(self):
            print(f"16) I am {self.age} yo")

except NotImplementedError:
    print(f"16) ok I knew")
