
# def getRangefrom(inp):
#     allranges = inp.split(': ')[1]
#     ranges = allranges.split(' or ')
#     theranges = []
#     for r in ranges:
#         theranges.append(list(map(int,r.split('-'))))
#     return theranges

def getRangefrom(inp):
    kv = inp.split(': ')
    allranges = kv[1]
    key = kv[0]
    ranges = allranges.split(' or ')
    theranges = []
    for r in ranges:
        theranges.append(list(map(int,r.split('-'))))
    return key,theranges

def checknearby(num, ranges):
    checkRange = False
    for r in ranges:
        if num >= ranges[r][0][0] and num <= ranges[r][0][1]:
            checkRange = True
            break
        if num >= ranges[r][1][0] and num <= ranges[r][1][1]:
            checkRange = True
            break
    return checkRange

def checknearbysingle(num, ranger):
    checkRange = False
    if num >= ranger[0][0] and num <= ranger[0][1]:
        checkRange = True
    if num >= ranger[1][0] and num <= ranger[1][1]:
        checkRange = True
    return checkRange

f = open("Puzzle1.in")

yourticket = None
throwaway = None
nearbytickets = []
validRanges = {}

for line in f:
    input = line.strip('\n')
    if input.find(' or ') > -1:
        k,v = getRangefrom(input)
        validRanges[k] = v
        # rs = getRangefrom(input)
        # for r in rs:
        #     validRanges.append(r)
    elif input.startswith('your ticket'):
        yourticket = [int(x) for x in next(f).strip('\n').split(',')]
        throwaway = next(f)
    elif input.startswith('nearby tickets:'):
        while True:
            try:
                nearbytickets.append(list(map(int,next(f).split(','))))
            except(StopIteration):
                break
    else:
        pass

goodNearbys = []

errorRate = 0
for nbticket in nearbytickets:
    goodTicket = True
    for nearbynum in nbticket:
        if not checknearby(nearbynum,validRanges):
            errorRate+=nearbynum
            goodTicket = False
    if goodTicket:
        goodNearbys.append(nbticket)

print(errorRate)
OK = [[True for _ in range(20)] for _ in range(20)]


for vn in goodNearbys:
    for i,v in enumerate(vn):
        for j,k in enumerate(validRanges):
            #print(i,j)
            if not checknearbysingle(vn[i],validRanges[k]):
                OK[i][j] = False

MAP = [None for _ in range(20)]
USED = [False for _ in range(20)]

found = 0

while True:
    for i in range(20):
        valid_j = [j for j in range(20) if OK[i][j] and not USED[j]]
        if len(valid_j) == 1:
            print(i,valid_j)
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
