import operator
file = open("input/21.sam", "r")
lines = [l.strip() for l in file.readlines()]
ops = { "+": operator.add, "*": operator.mul, "-": operator.sub, "/": operator.truediv }
rev_ops = { "+": operator.sub, "*": operator.truediv, "-": operator.add, "/": operator.mul }

mapper = {}

def init_mapper():
    global mapper
    mapper = {}
    for line in lines:
        monkey, operation = line.split(": ")
        mapper[monkey] = operation

def solve_part1(node='root', passes_human=False):
    operation = mapper[node]
    try:
        value = int(operation)
        return value, passes_human
    except:
        value = None

    a,o,b = operation.split(" ")
    passes_human = passes_human or a == "humn" or b == "humn"
    v1, p1 = solve_part1(a, passes_human)
    v2, p2 = solve_part1(b, passes_human)
    passes_human = passes_human or p1 or p2

    r = ops[o](v1, v2)
    return r, passes_human

def solve_for(node, value, search='humn'):
    operation = mapper[node]
    a,o,b = operation.split(" ")

    v1, p1 = solve_part1(a)
    v2, p2 = solve_part1(b)

    if a == search:
        p1 = True
    elif b == search:
        p2 = True

    if p1:
        # v1 is incorrect
        # v1 + v2 = value -> v1 should be value - v2
        # v1 - v2 = value -> v1 should be value + v2
        # v1 * v2 = value -> v1 should be value / v2
        # v1 / v2 = value -> v1 should be value * v2
        rev = rev_ops[o](value,v2)
        if a == search:
            return rev
        return solve_for(a, rev)
    elif p2:
        # v2 is incorrect
        # v1 + v2 = value -> v2 should be value - v1
        # v1 - v2 = value -> v2 should be v1 "-" value ---> -value + v1 :O "-" broke it, i did + :D
        # v1 * v2 = value -> v2 should be value / v1
        # v1 / v2 = value -> v2 should be v1 / value
        if o == "/":
            rev = rev_ops[o](v1,value)
        elif o == "-":
            rev = rev_ops[o](-value,v1)
        else:
            rev = rev_ops[o](value,v1)

        if b == search:
            return rev

        return solve_for(b, rev)
        
def solve_part2():
    operation = mapper['root']
    a,o,b = operation.split(" ")
    r1,p1 = solve_part1(a)
    r2,p2 = solve_part1(b)

    if not p1:
        target = r1
        start = b
    if not p2:
        target = r2
        start = a

    return solve_for(start, target)
  
init_mapper()
print("Part I: ", solve_part1()[0])   
print("Part II:", solve_part2())


