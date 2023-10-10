# variables
a: int = 77
b: str = "abc"
c: bool = True

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

# remove prefix
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
