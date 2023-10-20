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
