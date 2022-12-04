file = open("input/4.sam", "r")
lines = file.readlines()

p1 = p2 = 0
for line in lines:
    a,b = line.strip().split(",")
    start_a,end_a = (int(x) for x in a.split("-"))
    start_b,end_b = (int(x) for x in b.split("-"))
    p1 += 1 if (start_b >= start_a and end_b <= end_a) or (start_a >= start_b and end_a <= end_b) else 0
    p2 += 1 if (start_a <= start_b <= end_a) or (start_b <= start_a <= end_b) else 0
    
print("Part I: ",p1)
print("Part II:",p2)
