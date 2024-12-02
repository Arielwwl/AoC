reports = []

with open("input.txt", "r") as file:
    for i in file:
        data = list(map(int, i.split()))
        reports.append(data)

def safecheck(x):
    diff = [x[i]-x[i+1] for i in range(len(x)-1)] # calculates and shows the difference between 2 numbers in the list.
    if (max(diff) <= 3 and min(diff) >= 1) or (max(diff) <= -1 and min(diff) >= -3): # only returns true for lists that have difference between 1 and 3.
        return True
    else:
        return False

print(sum([safecheck(i) for i in reports])) # part 1. Sums number of trues by iterating through all the reports.


