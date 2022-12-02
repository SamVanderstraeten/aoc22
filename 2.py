file = open("input/2.sam", "r")
moves = [a.strip().split(" ") for a in file.readlines()]
opponent = "ABC"
mine = "XYZ"
score = sum([mine.index(m[1])+1 for m in moves]) + sum([(((mine.index(m[1])-opponent.index(m[0]))+1)%3)*3 for m in moves])
print('Part I: ', score)

score = sum([(((opponent.index(m[0])+(mine.index(m[1])-1))%3)+1) for m in moves]) + sum([mine.index(m[1])*3 for m in moves])
print('Part II:',score)