from util.parser import Parser

file = open("input/8.sam", "r")
grid = Parser.parse_int_grid(file.readlines(), '')

def check_line(line, row, col, reversed=False):
    var = []
    max = int(line[0])
    for i in range(1,len(line) - 1):
        h = int(line[i])
        if h > max:
            max = h
            if row > 0:
                var.append((row, i if not reversed else len(line)-1-i))
            elif col > 0:
                var.append((i if not reversed else len(line)-1-i, col))
        if max == 9:
            break
    return var

v = []
for i in range(1, len(grid)-1):
    line = grid[i]
    v.append(check_line(line, i, -1))
    v.append(check_line(line[::-1], i, -1, True))
    
for i in range(1, len(grid[0])-1):
    line = [a[i] for a in grid]
    v.append(check_line(line, -1, i))
    v.append(check_line(line[::-1], -1, i, True))

num = len(set(sum(v, [])))
round = len(grid)*2 + len(grid[0])*2 - 4
print("Part I: ", str(num+round)) 

# wrong choice in part I, start over again ;D

def find_vis_in_dir(row, col, dir):
    t = grid[row][col]
    count = 0
    for i in range(1,100):
        cr = row+dir[0]*i
        cc = col+dir[1]*i
        if cr < 0 or cc < 0 or cr > len(grid)-1 or cc > len(grid)-1:
            return count
        count +=1
        if grid[cr][cc] >= t:
            return count
    return count

max = 0
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
for row in range(1, len(grid)-1):
    for col in range(1, len(grid[0])-1):
        s = 1
        for d in dirs:
            s *= find_vis_in_dir(row, col, d)
        if s > max:
            max = s
print("Part II:",max)