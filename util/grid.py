class Grid:

    def __init__(self):
        self._p = False

    @staticmethod
    def search (grid, e):
        for r in range(len(grid)):
            row = grid[r]
            for c in range(len(row)):
                if grid[r][c] == e:
                    return (r,c)
        return None