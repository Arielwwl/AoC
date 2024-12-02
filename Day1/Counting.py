list1, list2 = [], []

with open("input.txt", "r") as file:
    for i in file:
        line = i.split()
        a, b = line[0], line[1]
        list1.append(int(a))
        list2.append(int(b))
    
list1.sort()
list2.sort()

count = 0
for x, y in zip(list1, list2):
    count += abs(x-y)
print(count)