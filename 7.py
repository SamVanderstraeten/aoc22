file = open("input/7.sam", "r")
lines = [line.strip() for line in file.readlines()]

counts = {}
dirs = {}
cwd = []

def dir_size(dir):
    size = counts[dir]
    if dir in dirs:
        for sub in dirs[dir]:
            size += dir_size(dir+sub)
    return size

for line in lines:
    if line[0] == "$": #command
        cmd = line[2:4]
        if cmd == "cd":
            dir = line[5:]
            if dir == "/":
                cwd = ["/"]
            elif dir == "..":
                cwd.pop()
            else:
                cwd.append(dir)
    else:
        c = "".join(cwd)
        if not c in counts:
            counts[c] = 0
        if not c in dirs:
            dirs[c] = []   
        
        (a, b) = line.split(" ")
        if a == "dir":    
            dirs[c].append(b)
        else:            
            counts[c] += int(a)

sizes = []
sum = 0
for c in counts:
    size = dir_size(c)
    if size <= 100000:
        sum += size
    sizes.append(size)
print("Part I: ",sum) 

needed_space = dir_size("/") - 40000000
sizes.sort()
delete_folder = [s for s in sizes if s>needed_space].pop(0)
print("Part II:", delete_folder)