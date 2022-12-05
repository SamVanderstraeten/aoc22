input = open("input/5.sam", "r").read()

# Read stacks
stacks = {}
start_config = [l[:-1] for l in input.split('\n\n')[0].split('\n')]
for line in start_config[:-1]:
    for i in range(10):
        ix = i*4 + 1
        if ix < len(line) and line[ix] != ' ':
            if (i+1) in stacks.keys():
                stacks[i+1].append(line[ix])
            else:
                stacks[i+1] = [line[ix]]

cmd = [l.strip() for l in input.split('\n\n')[1].split('\n')]
for c in cmd:
    a, amount, b, stack_from, c, stack_to = c.split(" ")    
    # Part I
    #for i in range(int(amount)):
    #    stacks[int(stack_to)].insert(0, stacks[int(stack_from)].pop(0))
    # Part II
    for i in range(int(amount), 0, -1):
        stacks[int(stack_to)].insert(0, stacks[int(stack_from)].pop(i-1))

# Sort keys and print top crates
keys = list(stacks.keys())
keys.sort()
code = [stacks[c][0] for c in keys]
print("Solution:", ''.join(code))