from util.parser import Parser
from util.printer import Printer
from util.grid import Grid

file = open("input/12.sam", "r")
lines = file.readlines()

grid = Parser.parse_grid(lines,"")
start = Grid.search(grid, "S")
goal = Grid.search(grid, "E")
grid[start[0]][start[1]] = 'a'
grid[goal[0]][goal[1]] = 'z'
INVALID = 999999

def get_neighbors(p):
    n = []
    c = grid[p[0]][p[1]]
    h = ord(c)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for dir in dirs:
        nr = p[0] + dir[0]
        nc = p[1] + dir[1]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if ord(grid[nr][nc]) - h  <= 1:
                n.append((nr, nc))
    return n

def edsger():
    dist={}
    open = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            dist[(r,c)] = INVALID

    dist[start] = 0
    open = [start]

    while len(open) > 0:
        open = sorted(open, key=lambda a: dist[a])
        c = open.pop(0)

        ns = get_neighbors(c)
        for n in ns:
            if not n in open and dist[n] == INVALID:
                cost = dist[c] + 1
                if cost < dist[n]:
                    dist[n] = cost
                    open.append(n)
                if n == goal:
                    return dist[n]

print("Part I: ", edsger())

yop = []
nope = []
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 'a':
            start = (r,c)

            if not start in nope:
                path = edsger()
                if path == None:
                    q = [start]
                    while len(q) > 0:
                        k = q.pop()
                        nope.append(k)
                        ns = get_neighbors(k)
                        for n in ns:
                            if not n in nope:
                                q.append(n)
                else:
                    yop.append(path)
print("Part II:", min(yop))