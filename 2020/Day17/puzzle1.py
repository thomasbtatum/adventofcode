
def neighbors(point):
    ne = []

    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            for dz in [-1,0,1]:
                for dw in [-1,0,1]:
                    if dx!=0 or dy!=0 or dz!=0 or dw!=0:
                        ne.append((point[0]+dx,point[1]+dy,point[2]+dz,point[3]+dw))

    return ne

f = open("Puzzle1.in")
L = list(l.strip() for l in f)
active = []
y = 0
for l in L:
    x = 0
    for c in l:
        if c == '#':
            active.append((x,y,0,0))
        x+=1
    y+=1

print(active)

for k in range(6):
    addthese = []
    removethese = []
    for x in range(-15, 15):
        for y in range (-15,15):
            for z in range(-8,8):
                for w in range(-8,8):
                    point = (x,y,z,w)
                    print(k,point)
                    n = neighbors(point)
                    activen = len(set(n).intersection(set(active)))
                    if point in active:
                        if not 2<=activen<=3:
                            removethese.append(point)
                    else:
                        if 3 == activen:
                            addthese.append(point)

    for p in addthese:
        active.append(p)
    for q in removethese:
        active.remove(q)

print(len(active))