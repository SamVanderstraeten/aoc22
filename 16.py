from itertools import permutations

file = open("input/16.sam", "r")
lines = file.readlines()

TIME_LEFT = 30

class Valve:
    def __init__(self, name, rate, neighbors) -> None:
        self.name = name
        self.rate = rate
        self.neighbors = neighbors

    def __str__(self) -> str:
        return "Valve " + self.name + ": " + str(self.rate) + " " + str(self.neighbors)
    
valves = {}
for line in lines:
    first, second = line.split("; ")
    data = first.split(" ")
    neighbors = [l[:-1] if len(l)>2 else l for l in second.split(" ")[4:] ]
    valve = Valve(data[1], int(data[-1].split("=")[1]), neighbors)
    valves[valve.name] = valve

costs = {v: {} for v in valves.keys()}
def get_costs(): # BFS too find distances from all valves to all valves
    for v in valves:
        queue = set()
        next_queue = set()
        queue.add(v)
        current_distance = 0
        while True:
            while len(queue) > 0:
                curr = queue.pop()
                costs[v][curr] = current_distance
                for n in valves[curr].neighbors:
                    if not n in costs[v].keys():
                        next_queue.add(n)
            if not next_queue:
                break
            queue = next_queue
            current_distance += 1
            next_queue = set()

def calc_combo(p, time=30):
    current = "AA"
    time_left = time
    pressure = 0
    for v in p:
        # move
        time_left -= costs[current][v]
        current = v
        if time_left <= 0:
            break            

        # open valve
        time_left -= 1
        if time_left <= 0:
            break
        pressure += valves[v].rate*time_left
    return pressure

# pre calculate costs
get_costs()
pro_valves = [v for v in valves if valves[v].rate > 0]
combos = list(permutations(pro_valves, 6)) 
max_pressure = -1
# scan combos
for p in combos:
    pressure = calc_combo(p)
    max_pressure = max(max_pressure, pressure)
    n = ''.join(list(set(p)))
print("Part I: ", max_pressure)

# Part II - New method was needed... too slow. Could rework part I as well now, but I'm not gonna do that :)
# Elephant will be referred to as John. John would be an appropriate name for a valve-opening elephant.
ultra = 0
best_full_path_me = []
best_full_path_john = []
remaining_valves = [v for v in pro_valves]
future_window = 5

while (len(best_full_path_me) + len(best_full_path_john)) < len(pro_valves):
    curr_best = 0
    best_path_me = None
    best_path_john = None
    combos = list(permutations(remaining_valves, min(future_window, len(remaining_valves))))
    for p in combos:
        for l in range(len(p)):
            path_me = p[:l]
            path_john = p[l:]
            full_perm_me = best_full_path_me + list(path_me)
            total_me = calc_combo(full_perm_me, 26)
            full_perm_john = best_full_path_john + list(path_john)
            total_john = calc_combo(full_perm_john, 26)
            total = total_me + total_john

            if total > curr_best:
                curr_best = total
                ultra = curr_best
                best_path_me = path_me
                best_path_john = path_john

    if len(best_path_me) > 0:
        best_full_path_me.append(best_path_me[0])
        remaining_valves.remove(best_path_me[0])
    elif len(best_path_john) > 0:
        best_full_path_john.append(best_path_john[0])
        remaining_valves.remove(best_path_john[0])

print("Part II:",ultra)