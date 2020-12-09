from collections import deque, defaultdict
target = "shinygold"
rules = defaultdict(list)

def getbagname(longname):
    assert len(longname) > 0 and longname.find('bag') > 0
    longsplit = longname.split(' ')
    return longsplit[0]+longsplit[1]

f = open("Puzzle1.in")

for line in f:
    k,v = line.strip('\n').split(" contain ")
    key = getbagname(k)
    baglist=[]
    bags = v.split(', ')
    for bag in bags:
        if(bag.split(' ')[0] == 'no'):
            continue
        else:
            rules[getbagname(bag.split(' ',1)[1])].append(key)
    
#    if len(baglist) > 0:    
#        rules[key] = baglist

SEEN = set()
Q = deque([target])
while Q:
    x = Q.popleft()
    if x in SEEN:
        continue
    SEEN.add(x)
    for y in rules[x]:
        Q.append(y)
print(len(SEEN)-1)

print(SEEN)
print(rules)