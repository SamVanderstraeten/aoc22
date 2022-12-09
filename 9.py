file = open("input/9.sam", "r")
lines = [l.strip() for l in file.readlines()]

def zero_or_abs(n):
    return 0 if n == 0 else n/abs(n)

def follow(knot, target):
    dx = target[0] - knot[0]
    dy = target[1] - knot[1]    
    if abs(dx)<=1 and abs(dy)<=1:
        return knot
    return (knot[0] + zero_or_abs(dx), knot[1] + zero_or_abs(dy))

def move(num):
    dirs = {'R': (1,0), 'L': (-1,0), 'D': (0,-1), 'U': (0,1)}
    posT = []
    head = (0,0)
    knots = [(0,0)]*num
    for line in lines:
        d, num = line.split(" ")
        for i in range(int(num)):
            head = (head[0]+dirs[d][0], head[1]+dirs[d][1])
            prev = head
            for k in range(len(knots)):
                knots[k] = follow(knots[k], prev)
                prev = knots[k]
            posT.append(knots[-1])
    return len(set(posT))

print("Part I: ", move(1))
print("Part II:", move(9))