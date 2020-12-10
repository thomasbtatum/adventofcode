from collections import deque

def numbersumsfrompreamble(preamble, newnumber):
    idx1 = 0
    while idx1 < len(preamble):
        idx2 = idx1+1
        while idx2 < len(preamble):
            if preamble[idx1] + preamble[idx2] == newnumber:
                return True
            idx2+= 1
        idx1 += 1
    return False


f = open("Puzzle1.in")

preamblesize = 25
preamble = deque([])

count = 0
for line in f:
    newnumber = int(line.strip('\n'))

    if(count < preamblesize):
        preamble.append(newnumber)
        count+=1
    else:
        if numbersumsfrompreamble(preamble, newnumber):
            preamble.popleft()
            preamble.append(newnumber)
        else:
            print(newnumber)
            quit()