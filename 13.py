import ast
from functools import cmp_to_key

file = open("input/13.sam", "r")
pairs = [p.split("\n") for p in file.read().split("\n\n")]

def int_compare(a,b):
    if a < b: return -1
    if a > b: return 1
    return 0

def compare(a, b):
    if type(a) == int and type(b) == int:
        return int_compare(a,b)
    else:
        if type(a) != list: a = [a]
        if type(b) != list: b = [b]
        for i in range(min(len(a), len(b))):
            v = compare(a[i],b[i])
            if v != 0: return v
        return int_compare(len(a), len(b))

sum = 0
for i in range(len(pairs)):
    p1,p2 = pairs[i]
    p1 = ast.literal_eval(p1)
    p2 = ast.literal_eval(p2)
    valid = compare(p1,p2)
    if valid == -1:
        sum += (i+1)
print("Part I: ",sum)

packets = [ast.literal_eval(p) for pair in pairs for p in pair]
packets.append([[2]])
packets.append([[6]])
compare_key = cmp_to_key(compare)
packets.sort(key=compare_key)
print("Part II:",(packets.index([[2]])+1) * (packets.index([[6]])+1))