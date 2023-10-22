from typing import Any

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
