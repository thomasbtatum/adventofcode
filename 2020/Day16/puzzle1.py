
def getRangefrom(inp):
    allranges = inp.split(': ')[1]
    ranges = allranges.split(' or ')
    theranges = []
    for r in ranges:
        theranges.append(list(map(int,r.split('-'))))
    return theranges

def checknearby(num, ranges):
    checkRange = False
    for range in ranges:
        if num >= range[0] and num <= range[1]:
            checkRange = True
            break
    return checkRange

f = open("Puzzle1.in")

yourticket = None
throwaway = None
nearbytickets = None
validRanges = []

for line in f:
    input = line.strip('\n')
    if input.startswith('class') or input.startswith('row') or input.startswith('seat'):
        rs = getRangefrom(input)
        for r in rs:
            validRanges.append(r)
    elif input.startswith('your ticket'):
        yourticket = next(f)
        throwaway = next(f)
    elif input.startswith('nearby tickets:'):
        while True:
            try:
                readnearby = next(f)
                if nearbytickets != None:
                    nearbytickets += ','

                if nearbytickets == None:
                    nearbytickets = readnearby
                else:
                    nearbytickets += readnearby
            except(StopIteration):
                break
    else:
        pass

nearbys = list(map(int,nearbytickets.split(',')))

errorRate = 0
for nearbynum in nearbys:
    if not checknearby(nearbynum,validRanges):
        errorRate+=nearbynum

print(errorRate)