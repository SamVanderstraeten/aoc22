import numpy as np
from collections import defaultdict
import random

file = open("input/19.sam", "r")
lines = [l.strip() for l in file.readlines()]

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

blueprints = []
bp_max_bots = []
for line in lines:
    max_bots = np.zeros(4)
    max_bots[GEODE] = 999

    costs = [0]*4
    data = [int(s) for s in line.split() if s.isdigit()]
    costs[ORE] = [data[0],0,0,0]
    costs[CLAY] = [data[1],0,0,0]
    costs[OBSIDIAN] = [data[2],data[3],0,0]
    
    costs[GEODE] = [data[4],0,data[5],0]
    
    max_bots[ORE] = max(max_bots[ORE], data[0], data[1], data[2], data[4])
    max_bots[CLAY] = max(max_bots[CLAY], data[3])
    max_bots[OBSIDIAN] = max(max_bots[OBSIDIAN], data[5])    

    blueprints.append(np.array(costs))
    bp_max_bots.append(max_bots)

NUM = 24

bests = defaultdict(int)
def run(resources, bots, blueprint, bp_max_bots, time=0):
    # check what is affordable and split up possibilities
    possible_bots = []
    for c, cost in reversed(list(enumerate(blueprint))):
        if (cost<=resources).all(): # affordable?
            if bots[c] < bp_max_bots[c]: # don't allow more than X bots of same type
                possible_bots.append(c)
        if c == 3 and len(possible_bots) == 1:
            break
    
    # gather resources
    resources = np.add(resources, bots)

    if resources[GEODE] < bests[time]:
        return resources[GEODE]
    bests[time] = max(bests[time], resources[GEODE])

    # start subroutine for each possible bot (& no bot at all)
    if time+1 >= NUM:
        return resources[GEODE]
    else:
        k = 0
        for bot in possible_bots:
            bot_cost = blueprint[bot]
            bots_add = [0]*4
            bots_add[bot] = 1
            r = np.subtract(resources, bot_cost)
            b = np.add(bots, bots_add)
            k = max(k, run(r, b, blueprint, bp_max_bots, time+1))
        k = max(k, run(resources, bots, blueprint, bp_max_bots, time+1))
        
        return k       


sum = 0
for i, blueprint in enumerate(blueprints):
    print("Blueprint",(i+1))
    resources = np.zeros(4)
    bots = np.zeros(4)
    bots[0] = 1
    
    obs = run(resources, bots, blueprint, bp_max_bots[i])
    print(int((i+1)*obs))
    sum += int((i+1)*obs)
print("Part I:",sum)
    