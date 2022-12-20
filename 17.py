from collections import defaultdict

file = open("input/17.sam", "r")
wind = file.read()
WIN = len(wind)
GAPS = defaultdict(list)
WIND_CURSOR = BLOCK_CURSOR = -1
TOP_LINE = [0,0,0,0,0,0,0]
NUM = 2022
WIDTH = 7

class Block:
    def __init__(self, bottom, width, round=[]) -> None:
        self.bottom = bottom
        self.width = width
        self.round = round
        self.x = -1
        self.y = -1

    def shift(self, wind, top):
        nx = self.x + (-1 if wind == "<" else 1)

        if nx >= 0 and nx <= 7-self.width: # side borders
            if self.valid(nx, top):
                self.x = nx

    def valid(self, nx, top):
        for rx,ry in self.round:
            if top[nx+rx] == self.y + ry:
                return False

            if top[nx+rx] > self.y + ry:
                if not (self.y+ry) in GAPS[nx+rx]:
                    return False
        return True

BLOCKS = [
    Block([[0,0], [1,0], [2,0], [3,0]], width=4, round=[[0,0], [1,0], [2,0], [3,0]]), # horiz 4
    Block([[0,1], [1,0], [2,1]], width=3, round=[[0,1], [1,0], [2,1], [1,2]]), # cross
    Block([[0,0], [1,0], [2,0]], width=3, round=[[0,0], [1,0], [2,0], [2,1], [2,2]]), # hook
    Block([[0,0]], width=1, round=[[0,0], [0,1], [0,2], [0,3]]), # vert 4
    Block([[0,0], [1,0]], width=2, round=[[0,0], [1,0], [0,1], [1,1]]) # square
]

def next_wind():
    global WIND_CURSOR, WIN, wind
    WIND_CURSOR = (WIND_CURSOR + 1)%WIN
    return wind[WIND_CURSOR]

def next_block():
    global BLOCK_CURSOR, BLOCKS
    BLOCK_CURSOR = (BLOCK_CURSOR + 1)%len(BLOCKS)
    return BLOCKS[BLOCK_CURSOR]

def check_rest(block: Block):
    for bx,by in block.bottom:
        y_below = block.y + by - 1

        if y_below == TOP_LINE[block.x+bx]: # directly on top surface. stop.
            return True
        if y_below < TOP_LINE[block.x+bx] and (not y_below in GAPS[block.x+bx]): # shifted in below top, bottom is not a gap. stop.
            return True
    return False

def update_top_line(block: Block):
    global TOP_LINE
    my = 0
    for bx, by in block.round:
        py = TOP_LINE[block.x+bx]
        y = block.y + by

        if py > y:
            if y in GAPS[block.x+bx]:
                GAPS[block.x+bx].remove(y)
        
        TOP_LINE[block.x+bx] = max(py, y)
        my = max(my, py, y)

        if y-py > 1:
            for i in range(1,y-py):
                GAPS[block.x+bx].append(py+i)
                if len(GAPS[block.x+bx]) > 3000:
                    GAPS[block.x+bx] = GAPS[block.x+bx][1000:]

        
    return my

def print_line(top):
    print(top)
    for i in range(max(top),0,-1):
        for j in range(7):
            print('# ' if top[j]==i else '. ', end='')
        print()

def drop_block(max_y):
    global TOP_LINE

    curr = next_block()
    curr.x = 2
    curr.y = max_y + 4
    # 3 ticks of free falling
    for w in range(3):
       curr.shift(next_wind(), TOP_LINE) 

    curr.y = max_y + 1
    rest = False
    while not rest:
        curr.shift(next_wind(), TOP_LINE)
        rest = check_rest(curr)
        if rest:
            max_y = max(max_y,update_top_line(curr))
        else:
            curr.y -= 1
    
    return max_y

curr = None
max_y = 0
y = 0
for i in range(NUM):
    y = drop_block(y)

print("Part I: ",y)

WIND_CURSOR = BLOCK_CURSOR = -1
TOP_LINE = [0,0,0,0,0,0,0]
NUM = 1000000000000
GAPS = defaultdict(list)
y=0
count = 0
states = {}
heights = []
found = False
cycle_start_index, cycle_end_index = None, None
while not found:
    y = drop_block(y)
    floor_heights = tuple([y - x for x in TOP_LINE])
    state = (WIND_CURSOR, BLOCK_CURSOR, floor_heights)
    heights.append(y)
    for k, v in states.items():
        if state == v:
            cycle_start_index = k
            cycle_end_index = count
            found = True
            states[count] = state
            break

    states[count] = state
    count += 1

# cyclecyclecyclecyclecycle
cycle_start = states[cycle_start_index]
height_diff = heights[cycle_end_index] - heights[cycle_start_index]
cycle_index_diff = cycle_end_index - cycle_start_index
num_loops = (NUM - cycle_end_index) // cycle_index_diff
y += num_loops * height_diff
TOP_LINE = [y - cycle_start[2][x] for x in range(WIDTH)]
rock_index_after_loop = count + (num_loops * cycle_index_diff)

# last bit
for rock_index in range(rock_index_after_loop, NUM):
    y = drop_block(y)

print("Part II:", y )