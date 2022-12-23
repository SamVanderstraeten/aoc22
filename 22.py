import numpy as np 

TEST = False

file = open("test/22.sam", "r") if TEST else open("input/22.sam", "r")
map_data, instructions = file.read().split("\n\n")
lines = map_data.split("\n")

WIDTH = max([len(l) for l in lines])
HEIGHT = len(lines)
VOID = 0
EMPTY = 1
WALL = 4
SIZE = 4 if TEST else 50
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

directions = [(0,1), (1,0), (0,-1), (-1,0)]
map = np.zeros((HEIGHT, WIDTH))
instructions = instructions.strip()

def fill_grid(lines, map):
    first = None
    for r, line in enumerate(lines):
        for c, cell in enumerate(line):
            if cell == '.':
                if first == None:
                    first = (r,c)
                map[r][c] = EMPTY
            elif cell == '#':
                map[r][c] = WALL
    return first
    
instr_pointer = 0
def next_move():
    global instructions, instr_pointer

    if instr_pointer >= len(instructions):
        return -1

    current = instructions[instr_pointer]
    if current == "L" or current == "R":
        instr_pointer += 1
        return current
    else:
        v = 0
        k = 0
        try:
            while(True):
                k += 1
                v = int(instructions[instr_pointer:instr_pointer+k])
                if k > 8: 
                    instr_pointer = len(instructions)
                    return v
        except:
            instr_pointer += (k-1)
            return v

dir_pointer = 0
def turn(d=1):
    global directions, dir_pointer, dir
    dir_pointer = (dir_pointer + d)%len(directions)
    dir = directions[dir_pointer]

def p(p):
    return (p[0]+1, p[1]+1)

def get_score(p):
    return 1000*p[0] + 4*p[1] + dir_pointer

pos = fill_grid(lines, map)
startpos = (pos[0],pos[1])
dir = directions[dir_pointer]

move = next_move()
while move != -1:
    if move == "R":
        turn(1)
    elif move == "L":
        turn(-1)
    else:
        for i in range(move):
            next_step = ((pos[0] + dir[0])%HEIGHT, (pos[1] + dir[1])%WIDTH)
            
            if map[next_step[0]][next_step[1]] == WALL: # stop
                break
            elif map[next_step[0]][next_step[1]] == VOID: # wrap
                turn(2)
                prv_wall = False
                backtrack = (pos[0], pos[1])
                for b in range(max(WIDTH,HEIGHT)):
                    next_backtrack = ((backtrack[0] + dir[0])%HEIGHT, (backtrack[1] + dir[1])%WIDTH)
                    if map[next_backtrack[0]][next_backtrack[1]] == VOID: # stop
                        if not prv_wall:
                            pos = backtrack
                        break
                    elif map[next_backtrack[0]][next_backtrack[1]] == WALL:
                        prv_wall = True
                    else:
                        prv_wall = False
                    backtrack = next_backtrack
                turn(2)
            else: # ok
                pos = next_step
    move = next_move()

result = p(pos)
print("Part I: ", get_score(result))

def build_transfers():
    transfers = {}
    for d in range(0,SIZE):
        # connect 2 & 6
        transfers[(SIZE+d,-1,LEFT)] = (HEIGHT-1, WIDTH-1-d, 1)
        transfers[(HEIGHT, SIZE*3+d, DOWN)] = (SIZE*2-1-d, 0, -1)
        # connect 1 & 3
        transfers[(SIZE-1,SIZE+d, UP)] = (d, SIZE*2, 1)
        transfers[(d, SIZE*2-1, LEFT)] = (SIZE, SIZE+d, -1)
        # connect 3 & 5
        transfers[(SIZE*2, SIZE+d, DOWN)] = (HEIGHT-1-d, SIZE*2, -1)
        transfers[(HEIGHT-1-d, SIZE*2-1, LEFT)] = (SIZE*2-1, SIZE+d, 1)
        # connect 4 & 6
        transfers[(SIZE+d,3*SIZE, RIGHT)] = (SIZE*2, WIDTH-1-d, 1)
        transfers[(SIZE*2-1, WIDTH-1-d, UP)] = (SIZE+d,3*SIZE-1, -1)
        # connect 1 & 2
        transfers[(-1, SIZE*2+d, UP)] = (SIZE, SIZE-1-d, 2)
        transfers[(SIZE-1, d, UP)] = (0, SIZE*3-1-d,2)
        # connect 2 & 5
        transfers[(SIZE*2, d, DOWN)] = (HEIGHT-1, SIZE*3-1-d, 2)
        transfers[(HEIGHT, SIZE*2+d, DOWN)] = (SIZE*2-1, SIZE-1-d, 2)
        # connect 6 & 1
        transfers[(SIZE*2+d, WIDTH, RIGHT)] = (SIZE-1-d, SIZE*3-1, 2)
        transfers[(d, SIZE*3, RIGHT)] = (HEIGHT-1-d, WIDTH-1, 2)
    return transfers

def do_transfer(p):
    if p in transfers.keys():
        return transfers[p]
    return (p[0], p[1])

def rearrange_map():
    global HEIGHT, WIDTH, map
    new_map = np.zeros((WIDTH, HEIGHT))
    
    sub = map[SIZE*2:HEIGHT,0:SIZE]
    sub = np.rot90(sub, 1, axes=(1,0))
    new_map[SIZE:SIZE*2,0:SIZE*2] = sub

    new_map[0:SIZE*3, SIZE*2:SIZE*3] = map[0:SIZE*3, SIZE:SIZE*2]

    sub = map[0:SIZE,SIZE*2:]
    sub = np.rot90(sub, 2)
    new_map[SIZE*2:SIZE*3,SIZE*3:] = sub

    return new_map, WIDTH, HEIGHT

def get_zone(p):
    if p[0] < SIZE: return 1
    elif p[0] < SIZE*2:
        if p[1] < SIZE: return 2
        elif p[1] < SIZE*2: return 3
        else: return 4
    else:
        if p[1] >= SIZE*3: return 6
        else: return 5

if not TEST: # different layout, rearrange all the things
    map, HEIGHT, WIDTH = rearrange_map()

pos = (startpos[0],startpos[1]) if TEST else (0,SIZE*2)
dir_pointer = 0
dir = directions[dir_pointer]
instr_pointer = 0

transfers = build_transfers()
move = next_move()
while move != -1:
    if move == "R":
        turn(1)
    elif move == "L":
        turn(-1)
    else:
        for i in range(move):
            next_step = do_transfer(((pos[0] + dir[0]), (pos[1] + dir[1]), dir_pointer))
           
            if map[next_step[0]][next_step[1]] == WALL: # stop
                break
            else: # ok
                pos = (next_step[0], next_step[1])

            if len(next_step) == 3:
                turn(next_step[2])
    move = next_move()

print("Finished at",p(pos))
print("Zone",get_zone(pos))
# Zone 4 -> column -= 50 when we rearrange to original state (ugly? yup. does it work? yup.)
pos = (pos[0], pos[1]-50)
print("Part II:", get_score(p(pos)))