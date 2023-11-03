from typing import Any
from typing import Union, overload
import pandas as pd
import sys
from typing import Callable
from typing import Iterator
from typing import TextIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PyPDF2
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

# variables
name: str = "My name is 'salman"
print(type(name))
print(id(name))
print(dir(name))
a: int = 77
b: str = "abc"
c: bool = True
de: str = "my name is \"salman's"

# lists and its methods
x: list[str] = ["a", "b", "c"]
names21: list[Any] = ["Qasim", "Sir Zia", "Sir Inam", 20, True]
print(names21)

x[0] = "f"
# append used to push at the end
x.append("e")
# insert used to any insert at any place by giving index
x.insert(0, "f")
# del is used to delete the list
del x[1]
print(x)
# slicing the list
# 1- start(include)
# 2- end(exclude)
# 2- step(sequence) left to right value works otherwise provide negative value
# print(abc[start:end:step])
abc: list[str] = ["a", "v", "c", "d"]
print(abc[0:3])
print(abc[-1:-4:-1])
# step is used to take steps according to the value we provided jump and dont take that value
xyz: list[str] = list("abcdefghijklmnopq")
print(xyz[0:17:2])
# clear is used to empty the list
ab: list[str] = ["a", "b", "c"]
ab.clear()
print(ab)
# shallow copy
names: list[str] = ["ali", "nabeel", "haider"]
teachers = names
print(teachers)
teachers[0] = "ali khan"
print("After changing")
print(names)
print(teachers)
# deep copy
names1: list[str] = ["ali", "nabeel", "haider"]
teachers1 = names1.copy()
print(teachers1)
teachers1[0] = "ali khan"
print("After changing")
print(names1)
print(teachers1)
# pop is used to remove last value by default it removes last value but we cab=n remove by passing index too
names2: list[str] = ["ali", "nabeel", "haider"]
names2.pop()
names2.pop(0)
print(names2)
# count is used to count the value in the list
xz: list[str] = list("aaaabbcccddd")
print(xz)
print(xz.count("a"))
# Difference b/w append or extend
names3: list[str] = ["ali", "nabeel", "haider"]
names4: list[str] = ["mubeen", "noman", "asgar"]
# names3.append(names4)
print(names3)
names3.extend(names4)
print(names3)

# touples
y: tuple[str, str, str] = ("e", "f", "g")
print(y)

# singleline string
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
print(full_name)

# multiline string
myFirstName: str = "ali"
myName: str = """ 
shahid 
    akram
        butt
"""
print("hello world", myName)

# as or f string
my: str = "ali"
my1: str = f""" 
shahid 
    akram
        butt
        {my}
"""
print(my1)

# strip
d: str = "        xyz   "
print(d.lstrip())
print(d.rstrip())
print(d.strip())

# remove prefixs
f: str = "http//localhost"
print(f.removeprefix("http//"))

# big integer
g: int = 14000_00_00000
print(g)

# const variable capital world define const
A: str = "ali"

# loops
magicians: list[str] = ["alice", "david", "carolina"]
for mag in magicians:
    print(mag)

# string methods format
# 1
af: int = 7
bf: int = 8
df: str = "pakistan value a = {} and value b = {}".format(af, bf)
print(df)

# 2
name2: str = "Muhammad Qasim"
fname2: str = "Muhammad Aslam"
education2: str = "Master in Data Science"
age2: int = 30


card: str = """
PIAIC Student Card
Student Name : {}
Father's Name: {}
Age: {}
Education : {}
""".format(
    fname2, name2, education2, age2
)

print(card)

# 3
name3: str = "Muhammad Qasim"
fname3: str = "Muhammad Aslam"
education3: str = "Master in Data Science"
age3: int = 30


card3: str = """
PIAIC Student Card
Student Name : {1}
Father's Name: {0}
Age: {3}
Education : {2}
""".format(
    fname3, name3, education3, age3
)
#      0      1       2        3

print(card3)

# 4
name4: str = "Muhammad Qasim"
fname4: str = "Muhammad Aslam"
education4: str = "Master in Data Science"
age4: int = 30


card4: str = """
PIAIC Student Card
Student Name : {a}
Father's Name: {b}
Age: {c}
Education : {d}
""".format(
    a=name4, b=fname4, c=age4, d=education4
)

print(card4)

# Python Arithmetic Operators
n: int = 7
m: int = 2

print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n % m)
print(2**2)

# ASCII Code

# A = 65
# B = 66
# Z = 90

# a = 97
# b = 98
# z = 122

# 0=48
# 1=49
# 9=57

print(chr(90))
print(ord("C"))

l: str = "A"
o: str = "B"

print(o >= l)

# Python Logical Operators
print(True and True and True and True)
print(True and True and False and True)
print(False and False and False and True)

print(True or True or True or True)
print(True or True or False or True)
print(False or False or False or True)
print(False or False or False or False)

not True

# Python Identity Operators
v: str = "abc"
z: str = "abc"

print(id(v))
print(id(z))
print(v is z)
print(v is not z)

i: str = "abc"
j: str = "xyz"

print(id(i))
print(id(j))
print(i is j)
print(i is not j)

# Python Membership Operators
names12: list[str] = ["Sir Zia", "Sir Inam", "Qasim"]
uinput: str = input("Enter your name: ")
print(uinput in names12)
print(uinput not in names12)

# PEMDAS
print(3 + 2 - 2 * 4 / 2 + 2)

# unzip
i, g, p = "qasim", 7, 3.0
print(i)
print(g)
print(p)

aa, bd, ce = ("qasim", 7, 3.0)
print(aa)
print(bd)
print(ce)

data = ("qasim", 7, 3.0)
print(data[0], data[1], data[2])

data = ("qasim", 7, 3.0)
print(data[0], data[1], data[2])
print(*data)

print("a" * 6)

# Help
# help(object)
# object?
# object??
# ?object
# ??object  used for help in python but only works on build in function like print,len

# iteration on list with while loop
kl: list[str] = ["a", "b", "c", "d"]
pp: int = 0
while pp < len(kl):
    print(kl[pp])
    pp += 1

# loop syntax this is loop syntax after indentation include the body of loop
names22: list[str] = ["Sir Zia", "Muhammad Qasim", "DR Noman"]
# 1
for i in names22:
    print(f"Welcome dear teacher {i.upper()}")
    print("PIAIC Gen AI Team\n")

# 2
for name in names22:
    print(f"Welcome Dear Tacher {name.title()}")
    print("PIAIC Gen AI Team\n")

print("Pakistan zinda bad")

# 3
for name in names22[0:2]:
    print(f"Welcome Dear Tacher {name.title()}")
    print("PIAIC Gen AI Team\n")

print("Pakistan zinda bad")

# 4
for name in names22[::-1]:
    print(f"Welcome Dear Tacher {name.upper()}")
    print("PIAIC Gen AI Team\n")
print("Pakistan zinda bad\n")

# example of for loop with else
# 1
names44: list[str] = ["Sir Zia", "Muhammad Qasim", "DR Noman"]
for name in names44:
    print(name)
else:
    print("Hello world")

# 2
names55: list[str] = ["Sir Zia", "Muhammad Qasim", "DR Noman"]
user_input: str = input("Enter the name? ")
for name in names55:
    if name == user_input:
        print("Found")
        break
else:
    print("Hello world")

# 3
names66: list[str] = ["Sir Zia", "Muhammad Qasim", "DR Noman"]

for name in names66:
    print(name)
    break
else:
    print("Hello world")

# 4
data_base: list[tuple[str, str]] = [
    ("qasim", "123"),
    ("sirzia", "345"),
    ("ikhlas", "789"),
]

input_user: str = input("Enter user name? ")
input_password: str = input("Enter user password? ")

for row in data_base:
    user, password = row
    if input_user == user and input_password == password:
        print(f"Valid User {user}")
        break
else:
    print("Not found or Invalid user name")

# 5
magicians1: list[str] = ["alice", "david", "carolina"]
for magician in magicians1:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# enumerate function return a list with tuple including the index or the value
# 1
magicians11: list[str] = ["alice", "david", "carolina"]
print(list(enumerate(magicians11)))

# 2
magicians33 = ["alice", "david", "carolina"]
for index, name in enumerate(magicians33):
    print(index, name)

# Numbers with loop
# range(start, end, step)

# 1
print(list(range(0, 20, 2)))
print(list(range(10)))

# 2
for n in range(1, 11):
    print(n)

# 3
user1: str = input("Enter a number? ")
for n in range(1, 11):
    print(f"{int(user1)} x {n} = {int(user1)*n}")

# 4
squares: list[int] = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

# List comprehensive style
# [loop_body for item in items_list]

for ip in range(1, 11):
    print(ip**2)

[ip**2 for ip in range(1, 11)]
print([i**2 for i in range(1, 11)])

# 1
digits: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits)
print(max(digits))
print(min(digits))
print(sum(digits))

# Tuples are immutable in every language once their value is assigned cannot be changed but can be reinitialize
names99: tuple[str, str, str] = ("A", "B", "C")

# names99: tuple[str, str, str] = ("A", "B", "C")
# names99[0] = "F"
# print(names99)  cannot be possible

# 1
data23: tuple[str, list[int], bool] = ("A", [1, 2, 3], True)
print(data23[1])
data23[1].append(20)
print(data23)

# If-else-elif
# if logic:
#     True_block
# else:
#     False_block

if True:
    print("Pakistan zinda bad")
else:
    print("Hello world!")

if False:
    print("Pakistan zinda bad")
else:
    print("Hello world!")

# comprehensive if-else
# True_block if logic else False_block

#     True_block               logic           False_block
print("Pakistan zinda bad") if False else print("Hello world!")

if True:
    print("True Pakistan block")

print("1")
print("2")

if False:
    print("True Pakistan block")

print("1")
print("2")

if True:
    print("True_block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")

if False:
    print("True_block")
elif True:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")

# chain1 run only one block
if False:
    print("True_block")
elif False:
    print("elif logic1")
elif True:
    print("elif logic2")
elif True:
    print("elif logic3")
else:
    print("final else block")

# chain2 run only one block
if False:
    print("True_block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")

print("Pakistan")

per: Union[int, float] = 88
grade: Union[str, None] = None

if per >= 80:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else:
    grade = "Fail"

print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")


per1: Union[int, float] = int(input("Enter your percentage:\t"))
# per : int | float = 88
grade1: Union[str, None] = None

if per1 >= 80:
    grade1 = "A+"
elif per1 >= 70:
    grade1 = "A"
elif per1 >= 60:
    grade1 = "B"
elif per1 >= 50:
    grade1 = "C"
elif per1 >= 40:
    grade1 = "D"
elif per1 >= 33:
    grade1 = "E"
else:
    grade1 = "Fail"

print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")


PerType = Union[float, int]

percentages: list[PerType] = [88, 99.9, 50, 51, 65, 70]

grades: list[str] = []

for per in percentages:
    grade2: str = ""

    if (per >= 0) and (per < 33):
        grade2 = "Fail"
    elif (per >= 33) and (per < 40):
        grade2 = "E"
    elif (per >= 40) and (per < 50):
        grade2 = "D"
    elif (per >= 50) and (per < 60):
        grade2 = "C"
    elif (per >= 60) and (per < 70):
        grade2 = "B"
    elif (per >= 70) and (per < 80):
        grade2 = "A"
    elif (per >= 80) and (per <= 100):
        grade2 = "A+"

    grades.append(grade2)

print(percentages)
print(grades)

# set datatype
data3: set = {7, 1, 2, 1, 1, 1, 1, 3, 2}
print(data3)  # return unique

# Dictionary
# 1
data33: dict[str, str] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}
print(data33)

# 2
Key = Union[int, str, tuple]  # create custom type
Value = Union[int, str, list, dict, tuple, set]

data11: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}

print(data11)
print(data11["name"])
print(data11["fname"])
print(data11["education"])

# 3
data45: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    0: "Pakistan",
}

print(data45)
print(data45["name"])
print(data45["fname"])
print(data45["education"])
print(data45[0])

# 4
data99: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    # [1, 2, 3]: "Pakistan",  # error
    (1, 2, 3): "Pakistan",
    # {1, 2, 3}: "pakistan",  # error
}

print(data99)
print(data99["name"])
print(data99["fname"])
print(data99["education"])

# 5
data00: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    "abc": [1, 2, 3],
    "xyz": {1, 2, 3},
    "efg": (1, 2, 3),
    "cde": {"a": 1, "b": 2},
}

print(data00)
print(data00["name"])
print(data00["fname"])
print(data00["cde"])
print(data00["education"])

# 6
data09: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    "abc": [1, 2, 3],
    "xyz": {1, 2, 3},
    "efg": (1, 2, 3),
    "cde": {"a": 1, "b": 2},
}

print(data09)
print(data09["name"])
print(data09["fname"])
if isinstance(data09["cde"], dict):
    value_b = data09["cde"].get("b")
    if value_b is not None:
        print(value_b)

print(data09["education"])

data10: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    "abc": [1, 2, 3],
    "xyz": {1, 2, 3},
    "efg": (1, 2, 3),
    "cde": {"a": 1, "b": 2},
}

print(data10)
print(data10["name"])
print(data10["fname"])
if isinstance(data10["abc"], list):
    value_b = data10["abc"][0]
    if value_b is not None:
        print(value_b)

print(data10["education"])

data13: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    "abc": [1, 2, 3],
    "xyz": {1, 2, 3},
    "efg": (1, 2, 3),
    "cde": {"a": 1, "b": 2},
}

print(data13)
print(data13["name"])
print(data13["fname"])
if isinstance(data13["efg"], tuple):
    value_b = data13["efg"][0]
    if value_b is not None:
        print(value_b)

print(data11["education"])

data12: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    "abc": [1, 2, 3],
    "xyz": {1, 2, 3},
    "efg": (1, 2, 3),
    "cde": {"a": 1, "b": 2},
}

print(data12)
print(data12["name"])
print(data12["fname"])
if isinstance(data12["xyz"], set):
    value_b = data12["xyz"]
    if value_b is not None:
        print(value_b)

print(data12["education"])

# 7
data55: dict[Key, Value] = {}

data55["name"] = "Muhammad Qasim"  # add new key and values
data55["fname"] = "Muhammad Aslam"
data55["education"] = "MSDS"
print(data55)

# 8
data91: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}
print(data91)
data91["name"] = "M.Qasim"  # update
print(data91)

# methods of dictionary
data01: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}


print([i for i in dir(data01) if "__" not in i])

# 1
data02: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}


#                 key
print(data02.get("pakistan"))
print(data02.get("pakistan", "NA"))
print(data02.get("name", "NA"))

# 2
data03: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}

for Kd in data03:
    print(Kd)

# 3
data04: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}

print(data04.keys())  # keys
print(data04.values())  # values
print(data04.items())

for k in data04.keys():
    print(k)

# 4
keys: list[str] = ["id", "name", "fname", "course"]
data06: dict[Key, None] = {}

print(data06)

data06 = dict.fromkeys(keys, None)  # inline

print(data06)

# 5
data05: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}


print(data05.keys())  # keys
print(data05.values())  # values
print(data05.items())

for kgf in data05.values():
    print(kgf)

# 6
data07: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}

print("Before", data07)

data07.clear()
print("After", data07)

# 7
# data08: dict[Key, Value] = {
#     "fname": "Muhammad Aslam",
#     "name": "Muhammad Qasim",
#     "education": "MSDS",
# }

# print("Before", data08)

# del data08

# print("After", data08)

# 8
data14: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}
print("Before", data14)
data14.pop("education")
print("After", data14)

# 9
data15: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}

print("Before", data15)

data15.popitem()
print("After", data15)

# 10
data16: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}

print("Before", data16)

data16.setdefault("Pakistan", "Empty value")
print("After", data16)

# 11
data17: dict[Key, Value] = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
}


data1: dict[Key, Value] = {"name": "M.Qasim", "age": 30, "Height": "6 Feet"}

data17.update(data1)
print(data17)

# 12 Pandas library use for making data in excel form
students_data: dict[str, list[Any]] = {
    "roll no": [1, 2, 3],
    "Name": ["Sir Zia", "Sir Inam", "Muhammad Qasim"],
    "education": ["Master", "Master", "Master"],
}

dfg: pd.DataFrame = pd.DataFrame(students_data)
print(dfg)

# shuffle
a1: int = 7
b1: int = 9

a1, b1 = b1, a1

print(a1, b1)

# Loop and input from user
# while
# for

# controls
# break
# continue
# pass

# input with input function
# input from console

# Loop working on iterative data types
l1: list[int] = [1, 2, 3, 4, 5, 6]
for n in l1:
    print(n)

l2: tuple[int, int, int, int, int, int] = (1, 2, 3, 4, 5, 6)
for n in l2:
    print(f"current number :{n}")

l3: str = "Pakistan"
for i in l3:
    print(i)

l4: dict[str, str] = {"name": "Muhammad Qasim", "fname": "Muhammad Aslam"}
for k in l4:
    print(f"dictionary key {k} and value is {l4[k]}")

l5: set[int] = {1, 2, 3, 4, 1, 1, 1, 1}
for k in l5:
    print(f"set item is  {k} ")

# input from user
name11: str = input("What is your name? : \t")
print(type(name11))
print(f"Welecom dear User Mr/Miss {name11}!")

# While loop
# while logic: # True/False
#     loop_body

# 1
flag: bool = True  # flag
current_number: int = 0  #
while flag:
    print(f"current number is :{current_number}")
    current_number += 1

    if current_number == 10:  # flag false at some point
        flag = False

# 2
l6: list[int] = [100, 200, 300]
index2: int = 0  #

while index2 < len(l6):
    print(f"current index is :{index2} and list value is {l6[index2]}")
    index2 += 1

# 3
data18: list[dict[str, str]] = []
flag2: bool = True

while flag2:
    print("write quite or exit to stop this program")
    name21: str = input("Your good name ? \t:")
    eduction: str = input("Your last education? \t")

    if name21 in ["exit", "quite", "close", "stop"] or eduction in [
        "exit",
        "quite",
        "close",
        "stop",
    ]:
        flag2 = False
        break
    data18.append({"name": name21, "education": eduction})

print(data18)

# controls

# 1 break
for i9 in range(1, 11):
    if i9 == 5:
        break
    print(i9)

# 2 continue
for i9 in range(1, 11):
    if i9 == 5:
        continue
    print(i9)

# 3 pass
for i10 in range(1, 1000):
    pass

if "a" == "A":
    pass

print("hi")

# For input purpose sys.argv
print("line1")
print("line2")

print(type(sys.argv))
print(sys.argv)  # iterative data type list[str] 0=filename **value user define

# Extract even number
data19: list[int] = [1, 3, 5, 6, 3, 15, 18]
for i54 in data19:
    if i54 % 2 == 0:
        print(i54)

# Extract odd number
data20: list[int] = [1, 3, 5, 6, 3, 15, 18]
for i54 in data20:
    if i54 % 2 != 0:
        print(i54)


# Function
# pre-define function
# provided by in language
# user-define function
# custom function

# Syntax function
# def function_name(param1:type, param2:type,...)->Return_type:
#     function_body

# function_name(arg1,arg2)


# 1
def piaic() -> None:  # declaration/function signature
    # function body start
    print("PIAIC Generative Artificial Intelligence")  # statment1
    print("Python Crash course")  # statment2
    # function body end


piaic()  # calling


# 2
def sum(x: int, y: int) -> int:
    a: int = x + y
    print(a)
    return a


sum(9, 9)

# Required parameters functions


# 1
def add_two_numbers(num1: int, num2: int) -> int:
    print(num1 + num2)
    return num1 + num2


add_two_numbers(7, 20)  # agr1, arg2


# 2
def add_two_numbers1(num1: int, num2: int) -> int:
    print(f"num1 value {num1} and num 2 value {num2}")
    return num1 + num2


add_two_numbers1(7, 20)  # agr1, arg2 postional


# 3
def add_two_numbers2(num1: int, num2: int) -> int:
    print(f"num1 value {num1} and num 2 value {num2}")
    return num1 + num2


add_two_numbers2(num2=7, num1=20)  # agr1, arg2 key word arguments


# fucntion with optional parameters
def add_two_numbers3(num1: int, num2: int = 3) -> int:
    print(num1 + num2)
    return num1 + num2


add_two_numbers3(7)
add_two_numbers3(9, 4)

# Syntax lambda function
# one line function
# without name
# only use in this line
# lambda param1,param2 : function_body

# 1
ax = lambda num1, num2: num1 + num2

print(ax(7, 8))

# 2
add: Callable[[int, int], int] = lambda x, y: x + y
result = add(10, 20)  # result will be 30
print(result)

# 3
sum1: Callable[[int, int], int] = lambda a, b: a + b
print(sum1(9, 1))

# 4
data2021: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2022 = list(map(lambda x: x**2, data2021))
print(data2022)

# 5
data2023: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2024 = list(filter(lambda x: x % 2 == 0, data2023))
print(data2024)

# 6
data991: list[int] = list(filter(lambda x: x % 2 == 0, range(1, 101)))
print(len(data991))
print(data991)

# 7
data992: Iterator[int] = filter(lambda x: x % 2 == 0, range(1, 101))
print(next(data992))
print(next(data992))

# pass unlimited arguments


# 1
def abce(*nums):
    print(nums, type(nums))
    total = 0
    for n in nums:
        total += n
    print(total)
    return total


abce(1, 2, 3, 3, 5, 6)


# 2
def sum5(*num: int) -> tuple[int, ...]:
    print(num, type(num))
    return num


sum5(1, 2, 3, 45)


# 3
def greet(*names: str) -> None:
    """
    This function greets all persons in the names tuple.
    """
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John", "Sir Zia", "Muhammad Qasim")


# 4
def greet2(**xyz) -> None:
    print(xyz, type(xyz))


greet2(a="pakistan", b="China")


# 5
def sum6(**num: int) -> dict[str, int]:
    print(num, type(num))
    return num


sum6(a=1, b=2, c=3, d=45)


# 6
def greet3(**xyz: str) -> None:
    for k, v in xyz.items():
        print(f"The key is {k} and value is {v}")


greet3(a="pakistan", b="China")


# 7
def my_function(a, b, *abc, **xyz):
    print(a, b, abc, xyz)


my_function(1, 2, 7, 9, 9, 9, c=20, d=30, x=100)


# 8
def my_function1(a: int, b: int, *abc: int, **xyz: int):
    print(a, b, abc, xyz)


my_function1(1, 2, 7, 9, 9, 9, c=20, d=30, x=100)

# Recursice function A function call itself in his body


# 1
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# Generator function


# 1
def my_range(start, end, step=2):
    for i in range(start, end + 1, step):
        yield i  # The yield statement in Python is used within a function to turn it into a generator


aw = my_range(1, 10)
print(aw)
print(list(aw))


# 2
def my_range1(start: int, end: int, step: int = 2) -> Iterator[int]:
    for i in range(start, end + 1, step):
        yield i


print(list(my_range1(1, 9, 1)))

# Decorator function is a function which takes another function,updates it and then return it


# 1
def greet11(fn: Callable[[], None]):
    def wrapper():
        print("Good morning")
        fn()
        print("Thanks for using it")

    return wrapper


@greet11
def hello():
    print("Hello world")


hello()


# 2
def greet121(fn: Callable[[int, int], None]):
    def wrapper(*args, **kargs):
        print("Good morning")
        fn(*args, **kargs)
        print("Thanks for using it")

    return wrapper


@greet121
def sum12(x, y):
    print(x + y)


sum12(4, 5)


# 3
def my_decorator(func: Callable[[int], None]) -> Callable[[int], None]:
    def wrapper(num1: int) -> None:
        print("Something is happening before the function is called.")
        func(num1)
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello(num1: int) -> None:
    print(num1)


say_hello(100)

# shallow copy
# 1
list_a: list[int] = [1, 2, 3]  # 4
list_b = list_a
list_a.append(4)
print("list_b:", list_b)  # Output: list_b: [1, 2, 3, 4]

# 2
num_a: int = 5
num_b = num_a
num_a += 1
print("num_b:", num_b)  # Output: num_b: 5

# Addressing Changes without Function Calls
# 1
xz1 = 10
print("Before modification:", xz1, id(xz1))
xz1 += 1
print("After modification:", xz1, id(xz1))

# 2
a12: int = 5

print(f"First Assignment of variable a value is {id(a12)}")


def abced(num1: int) -> None:
    print(f"\tValue of start of function {num1} address {id(num1)}")
    num1 = 6  # copy now it will change update object

    print(f"\tnum1 value end of function {num1} address {id(num1)}")  # change here
    print("\tEnd of program")


abced(a12)  # pass by value imutable

print(f"End of program variable value is {a12} address of a {id(a12)}")

# 3
a21: list[int] = [1, 2, 3, 4]

print(id(a21))


def abc1(num1: list[int]) -> None:
    print(f"\tValue of start of function {num1} address {id(num1)}")
    num1.append(200)  # added on element
    print(f"num1 value is {num1} address {id(num1)}")


abc1(a21)  # pass by refference (mutable data type)

print(a21)

# Run time Error
# 1
a2: int = int(input("Enter number1:\t"))
b2: int = int(input("Enter number2:\t"))

print(a2 / b2)

# 2
names42: list[str] = ["Sir Zia", "Sir Inam", "Muhammad Qasim"]
indx: int = int(input("Enter index number:\t"))
print(names42[indx])

# 3
# data : tuple[int,int,int] = (1,2,3)
# data[0] = 2000

# Handle Run time error
# Syntax

# try:
#     logic
# except (Error_class1, Error_class2):
#     if error accured then run this block
# else:
#     if error not accured
# finally:
#     always run

# 1
print("logic1")
print("logic2")
print(5 / 0)  # Error
print("logic4")
print("logic5")

# 2
print("logic1")
print("logic2")
try:
    print(5 / 0)  # Error
except ZeroDivisionError:
    print("Zerro Division Error!")
print("logic4")
print("logic5")

# 3
print("logic1")
print("logic2")
try:
    print(5 / 0)  # Error
except ZeroDivisionError:
    pass
print("logic4")
print("logic5")

# 4
# print("logic1")
# print("logic2")

# l12: list[int] = [1, 2, 3]

# try:
#     print(5 / 0)  # Error
#     print(l12[0])
#     print(xyz1)


# except (ZeroDivisionError, IndexError, NameError):
#     print("Zerro Division Error!")
# print("logic4")
# print("logic5")

# 5
# print("logic1")
# print("logic2")

# l12: list[int] = [1, 2, 3]

# try:
#     print(5 / 0)  # Error
#     print(l12[0])
#     print(xyz1)

# except ZeroDivisionError:
#     print("Zero Division Error!")


# except IndexError:
#     print("Index Error!")


# except NameError:
#     print("Name Error!")

# print("logic4")
# print("logic5")

# Error handling for dynamic errors
# 1

l11: list[int] = [1, 2, 3]
try:
    # print(age)
    print(l11[200])
except Exception as e:
    print(f"Some thing is wrong!\n{e}")


# Create your custom error
class StudentCard:
    def __init__(self, roll_no: int, name: str, age: int) -> None:
        if age < 18 or age > 60:
            raise StudentAgeError("Your are not eligible for this program!")
        self.roll_no = roll_no
        self.name = name
        self.age = age


class StudentAgeError(Exception):  # custom error class
    pass


studen1 = StudentCard(1, "Qasim", 130)
print(studen1.name, studen1.roll_no, studen1.age)
studen1 = StudentCard(1, "Hammad", 16)

# File handling

# 1 open,close,read file in this way we have to close the file by ourself
data44: TextIO = open("./abc.txt")  # connectivity with abc.txt file
print(data44.read())
data44.close()  # close connectivity

# 2 but in this way we do not have to close the file it happen automatically
with open("./abc.txt") as file:
    print(file.read())

# 3
with open("./abc.txt") as file1:  # type: TextIO
    print(type(file1))
    print(file1.readline())  # read only one line (first line)
    print(file1.readline())  # line2

# 4
with open("./abc.txt") as file2:  # type: TextIO
    print(type(file2))
    print(file2.readline(), end="")  # read only one line
    print(file2.readline(), end="")  # line2

# 5
with open("./abc.txt") as file3:  # type: TextIO
    print(type(file3))
    print(file3.readlines())  # read all lines in the form of list

# 6
with open("./abc.txt", "r") as file4:  # type: TextIO
    print(type(file4))
    print(file4.readlines()[:3])

# 7
with open("./abc.txt", "r") as file5:  # type: TextIO
    print(file5.read())
    file5.write("Pakistan zinda bad")  # r can only read file

# 8
with open("./abc.txt", "w") as file7:  # type: TextIO
    print(file7.read())
    file7.write("Pakistan zinda bad")

# 9
with open("./abc1.txt", "w") as file6:  # type: TextIO
    file6.write("Pakistan zinda bad")

# 10
with open("./abc1.txt", "r+") as file8:  # type: TextIO
    print(file8.read())
    file8.write("WE love our country!")

# 11
with open("./abc1.txt", "r+") as file10:  # type: TextIO
    print(file10.read())

    file10.write("WE love our country!")

    print("After", file10.read())

# 12
with open("./abc1.txt", "r+") as file9:  # type: TextIO
    print(file9.read())

    file9.write("WE love our country!")
    file9.seek(0)

    print("After", file9.read())

# 13
with open("./abc2.txt", "r") as file11:  # type: TextIO
    print(file11.read())

# 14
with open("./abc2.txt", "w") as file12:  # type: TextIO
    # print(file.read())
    file12.write("Pakistan")

# if file exist then it overwrite the text
# if file not exist then it will create new file

# 15
with open("./abc3.txt", "a") as file13:  # type: TextIO
    # print(file.read())
    file13.write("Pakistan")

# if file not exist then it will create new file
# add content in last

# read some real world data files
# image
# csv
# live camera

# 1 cs file into table through pandas library
df1: pd.DataFrame = pd.read_csv("./data.csv")
print(df1)

# 2 excel file into table through pandas library
df2: pd.DataFrame = pd.read_excel("./demo.xlsx")
print(df2)

# 3 img checking in python through matplotlib library
img = mpimg.imread("img1.jpeg")  # covert into numpy array
print(plt.imshow(img))


# 4 pdf into python through PyPDF2 library
def read_pdf(file_path: str) -> list[str]:
    with open(file_path, "rb") as file:  # The 'b' in 'rb' stands for binary mode
        reader: PyPDF2.PdfReader = PyPDF2.PdfReader(file)
        text_content: list[str] = [page.extract_text() for page in reader.pages]
        return text_content


pages: list[str] = read_pdf("./mypdf.pdf")
print(pages)


# OOP (Object Oriented Programming)
# Class
# method
# first argument must be additional variable (self, this, or anything else)
# attribute
# connect with individual object
# class variables
# constructor
# def __init__(self,arg1, arg2)
# Class variable
# this value use for all objects
# ClassName.class_vriable
# class ClassName():
#     class_variable1 : type = Value
# Syntax of class
# class ClassName():
#     pass


# 1
class Teacher:
    name: str
    age: int

    def __init__(self, age: int, name: str) -> None:
        self.age = age
        self.name = name

    def Personality(self):
        print("The teacher personality is good")


obj: Teacher = Teacher(20, "Ali")
print(obj.age)
print(obj.name)
obj.Personality()


# 2
class Teacher1:
    def __init__(
        self, teacher_id: int, teacher_name: str
    ) -> None:  # method/constructor
        self.name: str = teacher_name  # self.attribute_name = value
        self.teacher_id: int = teacher_id
        self.organization_name: str = "PIAIC"

    def speak(self, words: str) -> None:  # method
        print(f"{self.name} is speaking {words}")

    def teaching(self, subject: str) -> None:  # method
        print(f"{self.name} is teaching {subject}...!")


teacher1: Teacher1 = Teacher1(12, "Sana")
print(teacher1.name)
print(teacher1.organization_name)
print(teacher1.teacher_id)
teacher1.speak("Hello")
teacher1.teaching("Python")

# Class Variable
# Class variable
# this value use for all objects
# ClassName.class_variable
# object_name.class_variable
# class ClassName():
#     class_variable1 : type = Value


# 1
class Teacher2:
    counter: int = 0  # Class variable1
    help_line_number: str = "0315-2968211"  # class variable2

    def __init__(
        self, teacher_id: int, teacher_name: str
    ) -> None:  # method/constructor
        self.name: str = teacher_name  # self.attribute_name = value
        self.teacher_id: int = teacher_id
        self.organization_name: str = "PIAIC"
        Teacher2.counter += 1

    def speak(self, words: str) -> None:  # method
        print(f"{self.name} is speaking {words}")

    def teaching(self, subject: str) -> None:  # method
        print(f"{self.name} is teaching {subject}...!")

    def details(self) -> None:
        information: str = f"""
Teacher name is {self.name}
our help line number is {Teacher2.help_line_number}

"""
        print(information)


obj1: Teacher2 = Teacher2(1, "Sir Zia Khan")
obj2: Teacher2 = Teacher2(2, "Muhammad Qasim")
print(obj1.counter)
print(obj2.counter)
print(Teacher2.counter)

print(obj1.help_line_number)
print(obj2.help_line_number)
print(Teacher2.help_line_number)

# Inheritance
# class ChileClass(ParentClass):
#     pass


# 1
class Parents:
    def __init__(self) -> None:
        self.eye_color: str = "Brown"
        self.hair_color: str = "black"

    def speak(self, words: str) -> None:
        print(f"Parent method speak: {words}")

    def watching(sef, object_name: str) -> None:
        print(f"You are looking {object_name}!")


class Child(Parents):
    pass


obj3: Parents = Parents()
print(obj3.eye_color)
print(obj3.hair_color)
obj3.speak("Pakistan zinda bad!")
obj3.watching("TV")

print("======Child object=======")
### Child object

obj4: Child = Child()
obj4.watching("Cenima")
obj4.speak("Hello World")
print(obj4.eye_color)
print(obj4.hair_color)


# 2
class Parents1:
    def __init__(self) -> None:
        self.eye_color: str = "Brown"
        self.hair_color: str = "black"

    def speak(self, words: str) -> None:
        print(f"Parent method speak: {words}")

    def watching(sef, object_name: str) -> None:
        print(f"You are looking {object_name}!")


class Child1(Parents1):
    def teaching(self, subject: str) -> None:
        print(f"Child method for teaching : {subject}")


obj5: Parents1 = Parents1()
print(obj5.eye_color)
print(obj5.hair_color)
obj5.speak("Pakistan zinda bad!")
obj5.watching("TV")


print("======Child object=======")
### Child object

obj6: Child1 = Child1()
obj6.watching("Cenima")
obj6.speak("Hello World")
print(obj6.eye_color)
print(obj6.hair_color)
obj6.teaching("Generative AI")


# 3
class Employee:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.education: str = ""
        self.department: str = ""


class Designer(Employee):
    def __init__(self, title: str, name: str) -> None:
        super().__init__(name)
        self.title: str = title


class Developer(Employee):
    def __init__(self, title: str, name: str) -> None:
        super().__init__(name)
        self.title: str = title
        self.programming_skills: list[str] = ["python"]


designer1: Designer = Designer("Animation Artist", "Asif Khan")
dev1: Developer = Developer("GenAI Engineer", "John Doe")

print(designer1.title)  # Output: Animation Artist
print(dev1.programming_skills)  # Output: ['python']


# 4
class Employee1:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Designer1(Employee1):
    title: str

    def __init__(self, title: str, name: str, age: int) -> None:
        super().__init__(name, age)
        self.title: str = title


class Developer1(Employee1):
    skills: str

    def __init__(self, skills: str, name: str, age: int) -> None:
        super().__init__(name, age)
        self.skills: str = skills
        self.programming_skills: list[str] = ["python"]


designer2: Designer1 = Designer1("Animation Artist", "Asif Khan", 20)
dev2: Developer1 = Developer1("GenAI Engineer", "John Doe", 34)

print(designer2.title)  # Output: Animation Artist
print(dev2.programming_skills)


# Multiple inheritance
# 1
class A1:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class B1:
    title: str

    def __init__(self, title: str) -> None:
        self.title = title


class C1(A1, B1):
    skills: str

    def __init__(self, skills: str, name: str, age: int, title: str) -> None:
        A1.__init__(self, name, age)  # Call A's constructor explicitly
        B1.__init__(self, title)  # Call B's constructor explicitly
        self.skills = skills
        self.programming_skills = ["python"]


# 2 In multiple inheritance if both parent have same method or variable then it will take nearest to it in this case it will take mother speaking method or gender variable
class Mother:
    gender: str = "Female"

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.eye_color: str = "blue"

    def speaking(self, words: str) -> str:
        return f"Monther Speaking function: {words}"


class Father:
    gender: str = "Male"

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.height: str = "6 Feet"

    def speaking(self, words: str) -> str:
        return f"Father Speaking function: {words}"


class Child12(Mother, Father):
    def __init__(self, mother_name: str, father_name: str, child_name: str) -> None:
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name)
        self.child_name: str = child_name


qasim: Child12 = Child12("Naseem Bano", "Muhammad Aslam", "Muhammad Qasim")

print(f"object height {qasim.height}")
print(qasim.gender)
print(f"object eye color {qasim.eye_color}")
print(qasim.speaking("Pakistan zinda bad"))

# Generice class
# 1
T = TypeVar("T")


class Node(Generic[T]):
    x: T

    def __init__(self, x: T) -> None:
        self.x = x


x1 = Node("")  # Inferred type is Node[str]
y1 = Node(0)  # Inferred type is Node[int]
z1 = Node(True)  # Inferred type is Node[Any]

a122 = Node[int](0)
b12 = Node[str]("a")
b121 = Node[bool](False)
a1211 = Node[tuple[int, int, int]]((1, 2, 3))
d1211 = Node[list[int]]([1, 2, 3])

p1 = Node[int](0)
q1 = Node[str]("Hello")

print(a1211.x)
print(d1211.x)


# Function Overloading
# 1
@overload
def add21(x: int, y: int) -> int:
    ...


@overload
def add21(x: float, y: float) -> float:
    ...


@overload
def add21(x: str, y: str) -> str:
    ...


def add21(
    x: Union[int, float, str], y: Union[int, float, str]
) -> Union[int, float, str]:
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    elif isinstance(x, float) and isinstance(y, float):
        return x + y
    elif isinstance(x, str) and isinstance(y, str):
        return x + y
    else:
        raise TypeError("Invalid argument types!")


# Usage examples
result1 = add21(1, 2)  # Should return 3
result2 = add21(1.5, 2.5)  # Should return 4.0
result3 = add21("Hello, ", "world!")  # Should return "Hello, world!"

print(result1)
print(result2)
print(result3)


# Method Overloading
# 1
class Adder:
    @overload
    def add(self, x: int, y: int) -> int:
        ...

    @overload
    def add(self, x: float, y: float) -> float:
        ...

    @overload
    def add(self, x: str, y: str) -> str:
        ...

    def add(
        self, x: Union[int, float, str], y: Union[int, float, str]
    ) -> Union[int, float, str]:
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        elif isinstance(x, float) and isinstance(y, float):
            return x + y
        elif isinstance(x, str) and isinstance(y, str):
            return x + y
        else:
            raise TypeError("Invalid argument types!")


# Usage examples
adder = Adder()
result1 = adder.add(1, 2)  # Should return 3
result2 = adder.add(1.5, 2.5)  # Should return 4.0
result3 = adder.add("Hello, ", "world!")  # Should return "Hello, world!"

print(result1)
print(result2)
print(result3)


# Overridding
# 1
class Animal:
    def eating(self, food: str) -> None:  # same method
        print(f"Animal is eating {food}")


class Bird(Animal):
    def eating(self, food: str) -> None:
        print(f"Bird is eating {food}")


bird: Bird = Bird()
bird.eating("bread")

animal: Animal = Animal()
animal.eating("grass")

# Polymorphism means many forms
animal1: Animal = Bird()  # run time it will decide which object method it will be run
animal1.eating("grass")
print(type(animal1))


# Static Method and Static variable(class variable)
# 1
class MathOperations:
    counter: int = 100
    organization: str = "PIAIC"

    @staticmethod
    def add(x: int, y: int) -> int:
        """Add two numbers."""
        return x + y

    @staticmethod
    def multiply(x: int, y: int) -> int:
        """Multiply two numbers."""
        return x * y


# Using the static methods
result_add = MathOperations.add(10, 20)
result_multiply = MathOperations.multiply(10, 20)

print("Addition:", result_add)
print("Multiplication:", result_multiply)

print("Static variable or Class variable", MathOperations.organization)

# Everything is an object


class Human:
    def eating(self, food: str) -> None:
        print(f"Human is eating {food}")


obj121: Human = Human()
obj121.eating("Biryani")
print(dir(obj121))


class Human1(object):
    def eating(self, food: str) -> None:
        print(f"Human is eating {food}")


print(dir(object))

obj211: Human1 = Human1()
obj211.eating("Biryani")
print(dir(obj211))


# Callable
# 1
class PowerFactory:
    def __init__(self, exponent=2):
        self.exponent = exponent

    def __call__(self, base):
        return base**self.exponent


a221: PowerFactory = PowerFactory()
print(a221.exponent)
print(a221(3))


# 2
class CumulativeAverager:
    def __init__(self):
        self.data = []

    def __call__(self, new_value):
        self.data.append(new_value)
        print(self.data)
        return sum(self.data) / len(self.data)


stream_average = CumulativeAverager()

print(stream_average(12))  # data = [12] (12/1)

print(stream_average(13))  # data = [12,13] (12+13/2)

print(stream_average(11))  #

print(stream_average(10))

print(stream_average.data)


# Data Access Modifier
# 1
class Piaic:
    def __init__(self) -> None:
        # self.name                             public
        self.piaic_helpline: str = "0800"  #
        # self._name                             protected
        self._total_expense: int = 6000000  #
        # __ = dundder
        # self.__name                             private
        self.__test_announcement: str = "5 Nov 2023"


class A3(Piaic):
    def __init__(self) -> None:
        super().__init__()


isfhan: Piaic = Piaic()
print(isfhan.piaic_helpline)
print(isfhan._total_expense)
# print(isfhan._Piaic__test_announcement) access private variable

isfhan.piaic_helpline = "0300"
isfhan._total_expense = 4000
print(isfhan.piaic_helpline)
print(isfhan._total_expense)
isfhan.__test_announcement = "2300"
print(isfhan.__test_announcement)


Ali: A3 = A3()
print(Ali.piaic_helpline)
print(Ali._total_expense)
# print(Ali.__test_announcement)


# Str method in class
# 1
class Teacher200:
    def __init__(self, name) -> None:
        self.name: str = name


sir_zia: Teacher200 = Teacher200("sir zia")

print(sir_zia)


# 2
class Teacher300:
    def __init__(self, name) -> None:
        self.name: str = name

    def __str__(self) -> str:
        return f"Teacher name is {self.name}"


sir_zia1: Teacher300 = Teacher300("sir zia")

print(sir_zia1)

# Abstract Class
# 1 Cannot create instance of abstract class
# class Animal21(ABC):
#     @abstractmethod
#     def __init__(self) -> None:
#         super().__init__()
#         self.living_thing: bool = True


# isfahan: Animal21 = Animal21()


# 2
class Animal11(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.living_thing: bool = True

    @abstractmethod
    def eat(self, food: str):
        ...


class Cat(Animal11):
    def __init__(self) -> None:
        super().__init__()  # parent

    def eat(self, food: str):
        return f"Cat is eating {food}"


isfahan: Cat = Cat()


print(isfahan.living_thing)
print(isfahan.eat("Mouse"))

# Duck Typing
class Duck:
    def quack(self):
        return "Quack!"


class Person:
    def quack(self):
        return "I'm Quacking Like a Duck!"


def in_the_forest(cake):
    print(cake.quack())


donald: Duck = Duck()
john: Person = Person()
in_the_forest(donald)
in_the_forest(john)
