import numpy as np
from collections import defaultdict

file = open("input/23.sam", "r")
lines = [l.strip() for l in file.readlines()]

class Elf:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.proposal = None

    def propose(self, p):
        self.proposal = p

    def move(self):
        if self.proposal != None:
            self.pos = self.proposal
            self.proposal = None

ELF = 1
VOID = 0
BASE = (1,1)
NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3
DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
SCAN_ORDER = [NORTH, SOUTH, WEST, EAST]
SCAN_DIRS = [
    [(-1,0), (-1,-1), (-1,1)],
    [(1,0), (1,-1), (1,1)],
    [(0,-1), (-1,-1), (1,-1)],
    [(0,1), (1,1), (-1,1)]
]

def init_grid():
    s = max(len(lines), len(lines[0]))
    grid = np.zeros((s*20,s*20), dtype=np.int8)
    BASE = (s*10,s*10)
    elves = []
    for r, line in enumerate(lines):
        for c, e in enumerate(line):
            if e == "#":
                grid[r+BASE[0]][c+BASE[1]] = ELF
                elves.append(Elf((r+BASE[0],c+BASE[1])))
    return grid, elves

def scan_surrounding(grid, pos):
    return np.sum(grid[pos[0]-1:pos[0]+2,pos[1]-1:pos[1]+2])-1

''' Returns True if space is clear '''
def scan_dir(grid, pos, dir):
    for d in SCAN_DIRS[dir]:
        if grid[pos[0]+d[0]][pos[1]+d[1]] == ELF:
            return False
    return True

def move_elf(grid, elf):
    grid[elf.pos[0]][elf.pos[1]] = VOID
    grid[elf.proposal[0]][elf.proposal[1]] = ELF
    elf.move()

def get_score(grid, elves):
    # Calculate
    min_row = min([elf.pos[0] for elf in elves])
    max_row = max([elf.pos[0] for elf in elves])

    min_col = min([elf.pos[1] for elf in elves])
    max_col = max([elf.pos[1] for elf in elves])

    return count_elves(grid, min_row, min_col, max_row, max_col)

def count_elves(grid, min_row, min_col, max_row, max_col):
    area = (max_row - min_row + 1) * (max_col - min_col + 1)
    elves = np.sum(grid[min_row:max_row+1, min_col:max_col+1])
    return area-elves

def play(grid, elves, rounds=100000):
    proposals = defaultdict(int)
    for i in range(rounds):
        if i == 10:
            print("Part I: ", get_score(grid, elves))

        # Phase I
        for elf in elves:
            n = scan_surrounding(grid, elf.pos)
            if n == 0: continue
            for dir in SCAN_ORDER:
                if scan_dir(grid, elf.pos, dir):
                    target_pos = (elf.pos[0]+DIRS[dir][0], elf.pos[1]+DIRS[dir][1])
                    elf.propose(target_pos)
                    proposals[target_pos] += 1
                    break
        
        # Phase II
        for elf in elves:
            if elf.proposal != None and proposals[elf.proposal] < 2:
                move_elf(grid, elf)
            else:
                elf.propose(None)

        if len(proposals) == 0:
            print("Part II:", (i+1))
            return

        proposals = defaultdict(int)
        SCAN_ORDER.append(SCAN_ORDER.pop(0))    

grid, elves = init_grid()
play(grid, elves)

