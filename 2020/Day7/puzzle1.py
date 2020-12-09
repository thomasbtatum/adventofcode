from collections import deque, defaultdict
target = "shinygold"
rules = defaultdict(list)
contents = defaultdict(list)

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
            name = getbagname(bag.split(' ',1)[1])
            count = int(bag.split(' ',1)[0])
            rules[name].append(key)
            contents[key].append((count,name))

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

def size(bag):
    ans = 1
    for(n,y) in contents[bag]:
        ans += n*size(y)
    return ans
print(size(target)-1)