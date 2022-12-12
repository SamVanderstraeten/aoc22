class Parser:

    def __init__(self):
        self._p = False

    @staticmethod
    def parse_grid(lines, delim=",", tr={}, strip=True):
        grid = []
        for line in lines:
            if delim == "":
                k = line[:-1] if line[-1] == "\n" else line
                if strip:
                    k = line.strip()
                grid.append([x if not x in tr else tr[x] for x in k if x != "\\n"])
            else:
                grid.append(line.strip().split(delim))
        return grid
    
    @staticmethod
    def parse_int_grid(lines, delim=","):
        grid = []
        for line in lines:
            if delim == "":
                k = line.strip()
                grid.append([int(x) for x in k if x != "\\n"])
            else:
                grid.append(line.strip().split(delim))
        return grid

    @staticmethod
    def parse_grid_ords(lines):
        grid = []
        for line in lines:
            grid.append([ord(x) for x in line.strip() if x != "\\n"])
        return grid