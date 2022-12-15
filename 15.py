TEST = False

file = open("test/15.sam", "r") if TEST else open("input/15.sam")
lines = file.readlines()
scanline = 10 if TEST else 2000000
RANGE = 20 if TEST else 4000000

coords = set()
sensors = []
beacons = []
unique_beacons_list = []

for line in lines:
    data = line.split(" ")
    sensorx = int(data[2][2:-1])
    sensory = int(data[3][2:-1])
    beaconx = int(data[8][2:-1])
    beacony = int(data[9][2:])
    sensors.append((sensorx, sensory))
    beacons.append((beaconx, beacony))
unique_beacons_list = list(set(beacons))

def dist(p1,p2):
    return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])

def intersect(center, radius, line):
    if radius < (abs(line-center[1])): 
        return 0,0
    d = radius - abs(line-center[1])
    x1 = center[0] + d
    x2 = center[0] - d
    return x1,x2

def beacons_on_line(line):
    return len([b for b in unique_beacons_list if b[1] == line])
    
def scan_line(line):
    pieces = []
    for i in range(len(sensors)):
        sensor = sensors[i]
        beacon = beacons[i]

        radius = dist(sensor, beacon)
        x1,x2 = intersect(sensor, radius, line)
        pieces.append((min(x1,x2), max(x1,x2)))

    pieces.sort(key=lambda a:a[0])
    follow = pieces[0][1]
    for k in range(1, len(pieces)):
        piece = pieces[k]
        if piece[0] <= follow+1:
            follow = max(follow, piece[1])
        else: 
            return pieces[0][0], follow+1
    return pieces[0][0], follow+1

x1,x2 = scan_line(scanline)
print("Part I: ", str(abs(x1-x2)-beacons_on_line(scanline)))

for i in range(RANGE):
    x1,x2 = scan_line(i)
    if x2 < RANGE:
        print("Part II:",str(x2*4000000 + i))
        break
