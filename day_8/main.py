from collections import defaultdict
from itertools import combinations

def ReadFile(file_name):
    return open(file_name, "r").read()


def get_filtered_data():
    content = ReadFile("input.txt").strip().split("\n")
    return content

def in_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid)

def get_all_locs(grid):
    all_locs = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != ".":
                all_locs[grid[i][j]].append((i,j))
    return all_locs


def get_antinodes(a, b, grid):
    ax, ay = a
    bx, by = b
    cx, cy = ax - (bx - ax), ay - (by - ay)
    dx, dy = bx + (bx - ax), by + (by - ay)
    
    if in_bounds(cx, cy, grid):
        yield (cx, cy)
    if in_bounds(dx, dy, grid):
        yield (dx, dy)

def Solution1():
    grid = get_filtered_data()
    all_locs = get_all_locs(grid)
    antinodes = set()
    
    for freg in all_locs:
        locs = all_locs[freg]
        for a,b in combinations(locs, r=2):
            for antinode in get_antinodes(a, b, grid):
                antinodes.add(antinode)
                
    return len(antinodes)


def get_antinodes2(a, b, grid):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    
    i = 0
    while True:
        point = (ax - dx * i, ay - dy * i)
        if in_bounds(point[0], point[1], grid):
            yield (point)
        else:
            break
        i += 1
        
    i = 0
    while True:
        point = (bx + dx * i, by + dy * i)
        if in_bounds(point[0], point[1], grid):
            yield (point)
        else:
            break
        i += 1    

def Solution2():
    grid = get_filtered_data()
    all_locs = get_all_locs(grid)
    antinodes = set()
    
    for freg in all_locs:
            locs = all_locs[freg]
            for a,b in combinations(locs, r=2):
                for antinode in get_antinodes2(a, b, grid):
                    antinodes.add(antinode)
                
    return len(antinodes)


# print(Solution1())
print(Solution2())
