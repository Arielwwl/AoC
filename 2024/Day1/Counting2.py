list1
list2

count = 0
for i in tuple(list1):
    if i in tuple(list2):
        count += 1
print(count)