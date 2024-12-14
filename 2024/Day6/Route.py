import os
os.chdir(r"c:\Users\ariel\Documents\GitHub\AoC\2024\Day6")

with open("input.txt", "r") as f:
    data = f.read().strip()

def parsemap(data):
    grid = []
    start = None
    face = None
    directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    for y, line in enumerate(data.splitlines()): # split data by lines and get y coord and the line itself
        grid.append(line)
        for x, char in enumerate(line): # get x coord and every chara in each line
            if char in directions:
                start = (x, y) # get coordinates of the starting point
                face = directions[char] # get the direction we're facing at the start
    
    return grid, start, face

def patrol(grid, start, face):
    maxy = len(grid)
    maxx = len(grid[0])
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # upwards, right, down, left

    x, y = start
    visited = set() # create a variable that's a set, which doesn't allow duplicates
    visited.add((x, y)) # starting position added
    been = set()

    while True:
        state = (x, y, face) # ensures we don't get stuck in infinite loop where guard moves in a circle
        if state in been:
            break
        been.add(state)

        dx, dy = face
        newx, newy = x + dx, y + dy # move and calc new coords depending on direction we're facing

        if 0 <= newx < maxx and 0 <= newy < maxy and grid[newy][newx] != "#": # if within grid and not obstacle
            x, y = newx, newy # move forward
            visited.add((x, y)) # add new positions to the set
        else:
            current = directions.index(face) # if not turn right then continue the loop
            face = directions[(current+1)%4] # move one index to the right of directions since directions is alr sorted to move clockwise
        
        if not (0 <= x < maxx and 0 <= y < maxy): # exit loop when move outside of grid
            break
    
    return visited # return the set containing every unique coordinate travelled

grid, start, face = parsemap(data)
coords = patrol(grid, start, face)
print(len(coords)) # part 1 FAIL :(
