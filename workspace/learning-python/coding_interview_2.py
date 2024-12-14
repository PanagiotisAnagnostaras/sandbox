# https://www.datacamp.com/blog/top-python-interview-questions-and-answers
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 1")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
# 4. Explain List, Dictionary, and Tuple comprehension with an example.
## Lists
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

## Dicts
myDict = {key: key for key in range(10) if key % 2 == 0}
print(f"4) {myDict}")
generator = genFun()
myDict = {key: key for key in {key for key in generator} if key is not None}
print(f"5) {myDict}")

## Sets
mySet = {key for key in range(10) if key % 2 == 0}
print(f"6) {mySet}")
generator = genFun()
mySet = {key for key in {key for key in generator} if key is not None}
print(f"7) {mySet}")

## Generator expression
genExpress = (letter for letter in "thisisboring")
myTuple = tuple(l for l in genExpress)
print(f"8) {myTuple}")

# Systems binary, decimal etc
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Arithmetic systems")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


def dec2bin(n: str):
    n = int(n)
    b_str = ""
    while n != 0:
        r = n % 2
        n = n // 2
        b_str = str(r) + b_str
    return b_str


def bin2dec(n: str):
    dec = 0
    for id, d in enumerate(n[::-1]):
        dec += int(d) * 2**id
    return str(dec)


def quad2dec(n: str):
    dec = 0
    for id, d in enumerate(n[::-1]):
        dec += int(d) * 4**id
    return str(dec)


def dec2quad(n: str):
    n = int(n)
    quad_str = ""
    while n != 0:
        r = n % 4
        quad_str = str(r) + quad_str
        n = n // 4
    return quad_str


n = 12  # input(f"provide number in dec\n")
print(
    f"{n} in dec is {bin(int(n))} in bin, {dec2bin(n)} in bin {dec2quad(n)} in quad {quad2dec(dec2quad(n))} in dec and {bin2dec(dec2bin(n))} in dec"
)

# https://www.interviewkickstart.com/blogs/articles/advanced-python-coding-challenges
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 2")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
"""
Write a function named 'format_number' that takes a non-negative number as its only parameter. Your function 
should convert the number to a string and add commas as a thousand separators. For example, calling
format_number(1000000) should return "1,000,000"
"""


def format_number(num):
    num_str = str(num)
    num_commas = len(num_str) // 3
    chucks = []
    for i in range(num_commas):
        if i == num_commas - 1:
            chucks.append(num_str[::-1][i * 3 :])
        else:
            chucks.append(num_str[::-1][i * 3 : (1 + i) * 3])
    str_for = ""
    for chuck in chucks[::-1]:
        str_for = str_for + "," + chuck[::-1]
    return str_for[1:]


num = 213_000_678
print(f"1) before {num} after {format_number(num)}")

# https://medium.com/@nikitasilaparasetty/python-interview-coding-questions-with-solutions-for-beginners-7f6d782defac

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 3")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


def isPalindrome(in_str: str):
    return in_str[::-1] == in_str


print(f"1) dasad = {isPalindrome('dasad')} scd = {isPalindrome('scd')}")


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 4")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


def factorial(num: int):
    fac = 1
    for i in range(num):
        fac = fac * (i + 1)
    return fac


print(f"factorial of 5 = {factorial(5)}")


print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 5")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


def is_prime(n):
    nums_2_check = [i for i in range(n) if i != 0 and i != 1]
    for i in nums_2_check:
        if n % (i) == 0:
            return False
    return True


for num in [3, 17, 24]:
    print(f"is {num} prime? {is_prime(num)}")

print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Question 6")
print("~~~~~~~~~~~~~~~~~~~~~~~~")


def find_common(list_1, list_2):
    common = []
    for el in list_1:
        if el in list_2:
            common.append(el)
    return list(set(common))


list_1 = [0, 2, 4, 5, 4, 4]
list_2 = [3, 4, 6, 5, 4]
print(f"common among {list_1} and {list_2} are {find_common(list_1, list_2)}")
