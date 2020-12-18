
import re

f = open("Puzzle1.in")

def domask(mask,bits):
    buildbits = ''
    for i in range(0,36):
        if mask[i] == 'X':
            buildbits+=bits[i]
        else:
            buildbits+=mask[i]
    return buildbits

memidx = 0
mems={}

for line in f:
    l = line.strip('\n')
    if(l[:2] == 'ma'):
        mask = l[7:]
    else:
        m = re.search(r"\[([0-9]+)\]", l)
        memidx = int(m.group(1))
        bits = '{0:b}'.format(int(l.split(' = ')[1])).zfill(36)
        newbits = domask(mask,bits)
        mems[memidx] = newbits

print(mems)

count = 0
for k in mems.keys():
    count += int(mems[k],2)

print(count)