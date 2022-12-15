from util.printer import Printer
file = open("input/14.sam", "r")
data = [line.strip().split(" -> ") for line in file.readlines()]
bounds_data = [[[int(x) for x in c.split(",")] for c in d] for d in data]

EMPTY, ROCK, SAND, SIZE = (0,1,2,1000)
INTO_THE_ABYSS = max([b[1] for bounds in bounds_data for b in bounds])
SOURCE = (0, 500)
PRIO = [(1, 0), (1,-1), (1, 1)]

def init_grid(part=1):
    # data is (x,y), I prefer (row, col)
    grid = [[EMPTY]*SIZE for x in range(SIZE)]
    for bounds in bounds_data:
        for i in range(len(bounds)-1):
            p1, p2 = bounds[i:i+2]

            if p1[0] != p2[0]: #horizontal
                mx = max(p1[0],p2[0])
                mn = min(p1[0],p2[0])
                for v in range(mn,mx+1):
                    grid[p1[1]][v] = ROCK
            elif p1[1] != p2[1]: #vertical
                mx = max(p1[1],p2[1])
                mn = min(p1[1],p2[1])
                for h in range(mn,mx+1):
                    grid[h][p1[0]] = ROCK

    if part == 2:
        for i in range(SIZE):
            grid[INTO_THE_ABYSS+2][i] = ROCK
    return grid

def sandstorm(grid, part=1, debug_print=False):
    i=0
    done = False
    while not done:
        i+=1
        r,c = SOURCE
        settled = False
        while not settled and not done:
            for p in PRIO:
                if grid[r+p[0]][c+p[1]] == EMPTY:
                    r+=p[0]
                    c+=p[1]
                    break
            else:
                grid[r][c] = SAND
                settled = True
                if part == 2 and r == SOURCE[0] and c == SOURCE[1]:
                    done = True
            if part == 1 and r >= INTO_THE_ABYSS:
                done = True
        if debug_print:
            Printer.print_grid_region(grid, (0,494,10,10))
            print()
    return i - (1 if part == 1 else 0)

grid = init_grid(1)
print("Part I: ", sandstorm(grid, 1))   
grid = init_grid(2)
print("Part II:", sandstorm(grid, 2))
