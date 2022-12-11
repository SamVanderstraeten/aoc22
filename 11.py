import math
import operator
file = open("input/11.sam", "r")
lines = [m.split('\n') for m in file.read().split("\n\n")]
ops = { "+": operator.add, "*": operator.mul, "^": operator.pow }
monkeys = []

class Monkey:
    def __init__(self, m):
        self.parse(m)
        self.items_inspected = 0

    def parse(self, m):
        self.items = [int(n.strip()) for n in m[1].split(": ")[1].split(",")]
        op_value = m[2].split(" ")[-1]       
        if op_value == "old":
            self.orig_op = "^"
            self.op = ops["^"]
            self.op_value = 2
        else:
            self.orig_op = m[2].split(" ")[-2].strip()
            self.op = ops[m[2].split(" ")[-2].strip()]
            self.op_value = int(m[2].split(" ")[-1].strip())
        self.div = int(m[3].split(" ")[-1])
        self.positive = int(m[4].split(" ")[-1])
        self.negative = int(m[5].split(" ")[-1])

def monkey_stuff(num, ultra=None):
    for i in range(num):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                item = monkey.op(item, monkey.op_value)

                if ultra:
                    item %= ultra
                else:
                    item = item // 3
                
                monkey.items_inspected  += 1
                if item % monkey.div == 0:
                    pos = monkeys[monkey.positive]
                    pos.items.append(item)
                else:
                    neg = monkeys[monkey.negative]
                    neg.items.append(item)

for m in lines:
    monkeys.append( Monkey(m) )
monkey_stuff(20)
mb = [m.items_inspected for m in monkeys]
mb.sort()
print("Part I: ", mb[-1]*mb[-2])

monkeys.clear()
for m in lines:
    monkeys.append( Monkey(m) )
ultra = math.lcm(*(monkey.div for monkey in monkeys))
monkey_stuff(10000, ultra)
mb = [m.items_inspected for m in monkeys]
mb.sort()
print("Part II:", mb[-1]*mb[-2])