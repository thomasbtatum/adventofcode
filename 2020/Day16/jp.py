import fileinput
import re

#
#https://www.youtube.com/watch?v=OhqvfoaBljY&t=1061s
#


f = open("Puzzle1.in")
limits=[]
L = list(l.strip() for l in f)

scanning = False
OK = [[True for _ in range(20)] for _ in range(20)]
p1=0
for l in L:
    if scanning:
        vs = [int(x) for x in l.split(',')]
        ticket_valid = True
        for v in vs:
            valid = False
            for a,b,c,d in limits:
                if a<=v<=b or c<=v<=d:
                    valid = True
            if not valid:
                p1 += v
                ticket_valid = False
        
        if ticket_valid:
            for i,v in enumerate(vs):
                for j,(a,b,c,d) in enumerate(limits):
                    if not (a<=v<=b or c<=v<=d):
                        OK[i][j] = False
        assert len(vs) == len(limits)
    else:
        xs = [int(x) for x in re.findall('\d+',l)]
        if len(xs) == 4:
            limits.append(xs)
        if 'nearby tickets' in l:
            scanning = True
print(p1)

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
yourticket = [103,197,83,101,109,181,61,157,199,137,97,179,151,89,211,59,139,149,53,107]
print(yourticket)
print(MAP)
p2 = 1
for i,j in enumerate(MAP):
    if j < 6:
        p2 *= yourticket[i]
    
print(p2)


