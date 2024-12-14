with open("input.txt", "r") as f:
    lines = [i.rstrip() for i in f]

def patrol(data):
    visited = set()
    obstacles = set()
    xbound, ybound = 0, 0
    startx, starty = None, None
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # upwards, right, down, left
    index = 0

    for y, line in enumerate(data):
        if not xbound:
            xbound = len(line)
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((x, y)) # save coords of obstacles
            elif char == "^":
                startx, starty = x, y # find coords of starting point
        ybound += 1

    cx, cy = startx, starty # initial coords

    while cx in range(0, xbound) and cy in range(0, ybound): # when within bounds
        dx, dy = directions[index] # current direction
        visited.add((cx, cy)) # add current position to set of coords that we visited

        if (cx + dx, cy + dy) in obstacles: # turn if obstacle
            index = (index + 1) % 4 # move one index to the right of directions since directions is alr sorted to move clockwise
        else: # no obstacle, then move forward
            cx += dx
            cy += dy

    return len(visited)

patrol(lines) # part 1