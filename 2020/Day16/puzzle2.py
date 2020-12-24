
def getRangefrom(inp):
    kv = inp.split(': ')
    allranges = kv[1]
    key = kv[0]
    ranges = allranges.split(' or ')
    theranges = []
    for r in ranges:
        theranges.append(list(map(int,r.split('-'))))
    return key,theranges

def checkValueagainstranges(val,ranges):
    for range in ranges:
        if val >= range[0] and val <= range[1]:
            return True
    return False

def checknearby(ticket, ranges):
    for t in ticket:
        oneTrue = False
        for rk in ranges.keys():
            for range in ranges[rk]:
                if t >= range[0] and t <= range[1]:
                    oneTrue = True
        if not oneTrue:
            return False
    return True

f = open("Puzzle1.in")

yourticket = None
throwaway = None
nearbytickets = {}
validRanges = {}
OK = [[True for _ in range (20)] for _ in range(20)]

for line in f:
    input = line.strip('\n')
    if input.find(' or ') > -1:
        k,v = getRangefrom(input)
        validRanges[k] = v
    elif input.startswith('your ticket'):
        yourticket = [int(x) for x in next(f).strip('\n').split(',')]
        throwaway = next(f)
    elif input.startswith('nearby tickets:'):
        count = 0
        while True:
            try:
                nearbytickets[count] = [int(x) for x in next(f).strip('\n').split(',')]
                count+=1
            except(StopIteration):
                break
    else:
        pass

#print(validRanges)
#print(nearbytickets)

validnearbys = {}

for nt in nearbytickets.keys():
    if checknearby(nearbytickets[nt],validRanges):
        validnearbys[nt] = nearbytickets[nt]

#build ok
for vn in validnearbys:
    avalid = validnearbys[vn]
    for i,v in enumerate(avalid):
        for j,k in enumerate(validRanges):
            if not checkValueagainstranges(avalid[i],validRanges[k]):
                OK[i][j] = False

MAP = [None for _ in range(20)]
USED = [False for _ in range(20)]

found = 0

while True:
    for i in range(20):
        valid_j = [j for j in range(20) if OK[i][j] and not USED[j]]
        if len(valid_j) == 1:
            MAP[i]  = valid_j[0]
            USED[valid_j[0]] = True
            found += 1
    if      found == 20:
        break

print(yourticket)
print(MAP)
p2 = 1
for i,j in enumerate(MAP):
    if j < 6:
        p2 *= yourticket[i]
    
print(p2)
