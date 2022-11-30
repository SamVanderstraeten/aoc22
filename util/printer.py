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
    def print_grid_nums(grid, charTrue="█", charFalse='.'):
        for row in grid:
            for e in row:
                c = charTrue if int(e) > 0 else charFalse
                print(c, end='')
            print()