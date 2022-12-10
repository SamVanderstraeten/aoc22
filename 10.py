file = open("input/10.sam", "r")
lines = [line.strip() for line in file.readlines()]

x = 1
cycle = 0
s = []
crt = []

def parse_instruction(line):
    if line[:4] == "noop":
        return "noop", 0
    else:
        return line.split(" ")

def get_num_cycles(instr):
    return 1 if instr == "noop" else 2

def get_signal_strength():
    return x*cycle

for line in lines:
    instr, arg = parse_instruction(line)
    cycles = get_num_cycles(instr)
    for i in range(cycles):
        if (x-1) <= cycle%40 <= (x+1): # scanlines are each [0,40]... seems I skipped that part
            crt.append("#")
        else:
            crt.append(" ")
        cycle += 1
        if cycle%20 == 0 and (cycle/20)%2==1: # 20, 60, 100, 140, 180, 220
            s.append(get_signal_strength())       
    if instr == "addx":
        x += int(arg)

print("Part I: ",sum(s))
print("Part II:")
for i in range(6):
    for p in crt[i*40:(i+1)*40]:
        print(p,end='')
    print('')