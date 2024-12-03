import re

with open ("input.txt", "r") as file:
    data = file.read().strip()

def multiply(x):
    sum = 0
    matches = re.findall(r"mul\((\b\d{1,3}),(\b\d{1,3})\)", x)
    for a, b in matches:
        sum += int(a)*int(b)
    return sum
    
multiply(data) # part 1

def enabled(x):
    sum = 0
    cont = True
    matches = re.finditer(r"do\(\)|don't\(\)|mul\((\b\d{1,3}),(\b\d{1,3})\)", x)
    for i in matches:
        if i.group().startswith("mul"):
            a, b = i.groups()
            if cont:
                sum += int(a)*int(b)
        if i.group() == "do()":
            cont = True
        elif i.group() == "don't()":
            cont = False
    return sum

enabled(data) # part 2