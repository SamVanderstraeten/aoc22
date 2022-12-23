from util.parser import Parser
from util.printer import Printer

file = open("test/n.sam", "r")
lines = [l.strip() for l in file.readlines()]

#data = [int(n) for n in lines]
#data = [x.split(",") for x in lines]
#grid = Parser.parse_grid(lines)
#Printer.print_grid(grid)

