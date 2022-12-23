file = open("test/20.sam", "r")
lines = file.readlines()
sequence = [int(l.strip()) for l in lines]
element_indexes = [i for i in range(len(sequence))]

for i in range(len(element_indexes)):
    curr_index = element_indexes[i]
    element_indexes = [element_indexes[x]-1 if element_indexes[x] > curr_index else element_indexes[x] for x in range(len(element_indexes))]
    n = sequence[curr_index]
    corrected_index = (curr_index+n)
    corrected_index %= (len(sequence)-1)
    element_indexes[i] = corrected_index
    element_indexes = [element_indexes[x]+1 if element_indexes[x] >= corrected_index else element_indexes[x] for x in range(len(element_indexes))]

    sequence.pop(curr_index)
    sequence.insert(corrected_index, n)

i0 = sequence.index(0)
n1000 = sequence[(i0+1000)%len(sequence)]
n2000 = sequence[(i0+2000)%len(sequence)]
n3000 = sequence[(i0+3000)%len(sequence)]
print(n1000,n2000,n3000)
print("Part I: ",(n1000+n2000+n3000))


sequence = [int(l.strip())*811589153 for l in lines]
element_indexes = [i for i in range(len(sequence))]

for r in range(10):
    print(r)
    for i in range(len(element_indexes)):
        curr_index = element_indexes[i]
        element_indexes = [element_indexes[x]-1 if element_indexes[x] > curr_index else element_indexes[x] for x in range(len(element_indexes))]
        n = sequence[curr_index]
        corrected_index = (curr_index+n)
        corrected_index %= (len(sequence)-1)
        element_indexes[i] = corrected_index
        element_indexes = [(element_indexes[x]+1)%len(element_indexes) if element_indexes[x] >= corrected_index else element_indexes[x] for x in range(len(element_indexes))]

        sequence.pop(curr_index)
        sequence.insert(corrected_index, n)

i0 = sequence.index(0)
n1000 = sequence[(i0+1000)%len(sequence)]
n2000 = sequence[(i0+2000)%len(sequence)]
n3000 = sequence[(i0+3000)%len(sequence)]
print(n1000,n2000,n3000)
print("Part II:",(n1000+n2000+n3000))

