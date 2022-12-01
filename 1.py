file = open("input/1.sam", "r")
elf_totals = [sum([int(c) for c in e.split("\n")]) for e in file.read().split("\n\n")]
print("Part I: ", max(elf_totals))

elf_totals.sort()
print("Part II:", sum(elf_totals[-3:]))