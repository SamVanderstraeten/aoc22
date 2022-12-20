file = open("input/18.sam", "r")
data = [[int(x) for x in p.strip().split(",")] for p in file.readlines()]

class Pixel:
    def __init__(self,pos) -> None:
        self.pos = pos
        self.adj = []

    def adjacent_to(self, p) -> bool:
        c = 0
        d = 0
        for i in range(len(self.pos)):
            if p.pos[i] == self.pos[i]:
                c += 1
            else:
                d = abs(p.pos[i]-self.pos[i])
        return c == 2 and d == 1

    def __str__(self) -> str:
        return str(self.pos)

    def __eq__(self, other) -> bool:
        if other == None: return False
        return self.pos[0] == other.pos[0] and self.pos[1] == other.pos[1] and self.pos[2] == other.pos[2]

pixels = []
most_top = None
maxs = [0,0,0]
mins = [999,999,999]
for x,y,z in data:
    p = Pixel((x,y,z))
    maxs = [max(maxs[l], p.pos[l]+2) for l in range(3)]
    mins = [min(mins[l], p.pos[l]-2) for l in range(3)]
    most_top = p if most_top == None or p.pos[1] > most_top.pos[1] else most_top
    for pixel in pixels:
        if pixel.adjacent_to(p):
            pixel.adj.append(p)
            p.adj.append(pixel)
    pixels.append(p)

print(mins,"->",maxs)

total = 0
for p in pixels:
    total += (6-len(p.adj))
print("Part I: ",total)

def in_bounds(curr, mins, maxs):
    for i in range(3):
        if not (mins[i] < curr[i] < maxs[i]):
            return False
    return True

start = Pixel((most_top.pos[0], most_top.pos[1]+1, most_top.pos[2]))
print("Starting BFS @", start.pos)

dirs = [(0,0,1),(0,0,-1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]
queue = [start]
visited = []
faces = 0
while len(queue) > 0:
    curr = queue.pop()
    for p in pixels:
        if p.adjacent_to(curr):
            faces += 1
    visited.append(curr)

    if not in_bounds(curr.pos, mins, maxs):
        continue

    for d in dirs:
        dp  = (curr.pos[0] + d[0], curr.pos[1] + d[1], curr.pos[2] + d[2])
        np = Pixel(dp)
        if not np in visited and not np in pixels and not np in queue:
            queue.append(np)

print("Part II:",faces) # takes a bit long but hey, it works