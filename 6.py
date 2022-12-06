file = open("input/6.sam", "r")
line = file.readline()

def find_window(size):
    for i in range(len(line)):
        if len(set(line[i:i+size])) == size:
            return (i+size)
    return -1

print("Part I: ", find_window(4))
print("Part II:", find_window(14))