
def neighbors(point):
    ne = []
    #9 of these
    ne.append((point[0]-1, point[1]-1, point[2]-1))
    ne.append((point[0], point[1]-1, point[2]-1))
    ne.append((point[0]+1, point[1]-1, point[2]-1))
    ne.append((point[0]-1, point[1], point[2]-1))
    ne.append((point[0], point[1], point[2]-1))
    ne.append((point[0]+1, point[1], point[2]-1))
    ne.append((point[0]-1, point[1]+1, point[2]-1))
    ne.append((point[0], point[1]+1, point[2]-1))
    ne.append((point[0]+1, point[1]+1, point[2]-1))
    
    #9 of these
    ne.append((point[0]-1, point[1]-1, point[2]+1))
    ne.append((point[0], point[1]-1, point[2]+1))
    ne.append((point[0]+1, point[1]-1, point[2]+1))
    ne.append((point[0]-1, point[1], point[2]+1))
    ne.append((point[0], point[1], point[2]+1))
    ne.append((point[0]+1, point[1], point[2]+1))
    ne.append((point[0]-1, point[1]+1, point[2]+1))
    ne.append((point[0], point[1]+1, point[2]+1))
    ne.append((point[0]+1, point[1]+1, point[2]+1))

    ne.append((point[0]-1, point[1]-1, point[2]))
    ne.append((point[0], point[1]-1, point[2]))
    ne.append((point[0]+1, point[1]-1, point[2]))
    ne.append((point[0]-1, point[1], point[2]))
    #ne.append[(point[0], point[1], point[2))
    ne.append((point[0]+1, point[1], point[2]))
    ne.append((point[0]-1, point[1]+1, point[2]))
    ne.append((point[0], point[1]+1, point[2]))
    ne.append((point[0]+1, point[1]+1, point[2]))

    return ne

f = open("Puzzle1.in")
L = list(l.strip() for l in f)
active = []
y = 0
for l in L:
    x = 0
    for c in l:
        if c == '#':
            active.append((x,y,0))
        x+=1
    y+=1

print(active)

for k in range(6):
    addthese = []
    removethese = []
    for x in range(-20, 20):
        for y in range (-20,20):
            for z in range(-20,20):
                point = (x,y,z)
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