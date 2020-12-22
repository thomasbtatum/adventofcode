
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
        yourticket = next(f).strip('\n')
        throwaway = next(f)
    elif input.startswith('nearby tickets:'):
        count = 0
        while True:
            try:
                readnearby = next(f)
                nearbytickets[count] = list(map(int,readnearby.strip('\n').split(',')))
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


#print("valid ranges",validRanges)
#print("nearby tickets",nearbytickets)
#print("valid nearbys",validnearbys)

departureranges  = {k:v for (k,v) in validRanges.items() if k.startswith('departure')}
print("we have:", len(departureranges))
print("we have:", len(validnearbys))

for k in departureranges:
    for idx in range(0,len(validnearbys[0])):
        countGood = 0
        for v in validnearbys:
            if not checkValueagainstranges(validnearbys[v][idx],departureranges[k]):
                countGood = 0
                break
            else:
                countGood+=1
        if countGood > 0:
            print ("good idx", k, idx, countGood)