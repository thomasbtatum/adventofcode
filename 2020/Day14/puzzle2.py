
import re,itertools

f = open("Puzzle1.in")

def domask(mask,bits):
    buildbits = ''
    for i in range(0,36):
        if mask[i] == 'X' or mask[i] == '1':
            buildbits+=mask[i]
        else:
            buildbits+=bits[i]
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
        bits = '{0:b}'.format(memidx).zfill(36)
        val =  int(l.split(' = ')[1])

        newbits = domask(mask,bits)
        countfloat = newbits.count('X')
        if countfloat > 0:
            seqs = ["".join(seq) for seq in itertools.product("01", repeat=countfloat)]
            countseqs = 0
            for seq in seqs:
                nbclone = newbits[:]
                for j in range(0,len(seq)):
                    nbclone = nbclone.replace('X',seq[j],1)
                adr = int(nbclone,2)
                mems[adr] = val
                countseqs+=1
        else:
            adr2 = int(newbits,2)
            mems[adr2] = val

print(mems)

count = 0
for k in mems.keys():
    count += mems[k]

print(count)