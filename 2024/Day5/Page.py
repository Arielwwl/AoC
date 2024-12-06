rules, updates = [], []
with open("input.txt", "r") as f:
    a, b = f.read().strip().split("\n\n")
    for i in a.split("\n"):
        rules.append(i.split("|"))
    for i in b.split("\n"):
        updates.append(list(map(int, i.split(","))))

def validlist(rule, update): # function that iterates through every update and check if it's valid
        for i in rule:
            if int(i[0]) in update and int(i[1]) in update: # check if both values of the rule are in each update
                if update.index(int(i[0])) > update.index(int(i[1])): # check whether 1st value of rule is before 2nd value of rule in each update
                    return False
        return True

def middles(rules, updates):
    count = 0
    for u in updates:
        if validlist(rules, u):
            count += u[len(u)//2] # sum middle numbers
    return count

middles(rules, updates) # part 1

def resorted(rules, updates): # function to sort the values within each update if they don't follow the rules
    for _ in range(len(updates)):
        for i in rules:
            x, y = int(i[0]), int(i[1])
            if x in updates and y in updates:
                ind1 = updates.index(int(i[0]))
                ind2 = updates.index(int(i[1]))
                if ind1 > ind2: # if update violates the rule
                    updates.remove(x) # remove x (where rule is x|y) 
                    updates.insert(updates.index(y), x) # then add x in again to y's position. So now x is before y.
    return updates

def middles2(rules, updates):
    count = 0
    for u in updates:
        if not validlist(rules, u): # to filter out the wrongly sorted ones
            newupdate = resorted(rules, u) # resort them then sum the middle value
            count += newupdate[len(newupdate)//2]
    return count

middles2(rules, updates) # part 2
