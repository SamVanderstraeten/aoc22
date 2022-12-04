file = open("input/3.sam", "r")
lines = file.readlines()

def get_score(c):
    return ord(c)-ord('A')+27 if c.isupper() else ord(c)-ord('a')+1

score = sum([get_score([d for d in line[int(len(line)/2):] if d in line[0:int(len(line)/2)]][0]) for line in lines])
print("Part I: ",score)

pr = 0
for i in range(int(len(lines)/3)):
    a,b,c = lines[i*3:i*3+3]
    pr += get_score([w for w in a if w in b and w in c][0])
print("Part II:",pr)