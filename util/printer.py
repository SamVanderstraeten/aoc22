class Printer:
    
    def __init__(self):
        self._p = False
        
    @staticmethod
    def print_grid(grid):
        for row in grid:
            for e in row:
                print(str(e) + " ", end='')
            print()

    @staticmethod
    def print_grid_region(grid, region=None):
        if region == None:
            print("Specify region")
            return
            
        for r in range(region[0], min(region[0]+region[2], len(grid))):
            row = grid[r]
            for c in range(region[1], min(region[1]+region[3], len(grid[0]))):
                e = row[c]
                print((str(e) if e!=0 else " ") + " ", end='')
            print()

    @staticmethod
    def print_grid_nums(grid, charTrue="█", charFalse='.'):
        for row in grid:
            for e in row:
                c = charTrue if int(e) > 0 else charFalse
                print(c, end='')
            print()