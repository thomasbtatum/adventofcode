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

def findsequence(num, numbers):
    start = 0
    while start < len(numbers):
        idx = start
        total = 0
        while idx < len(numbers):
            total+=numbers[idx]
            if(total > num):
                break
            if(total == num):
                sublist = numbers[start:idx+1]
                low = min(sublist)
                high = max(sublist)
                print("found sum. low and high are:",low,high,low+high)
                quit()
            idx+=1
        start+=1

f = open("Puzzle1.in")

preamblesize = 25
preamble = deque([])
numbers = []

count = 0
for line in f:
    newnumber = int(line.strip('\n'))
    numbers.append(newnumber)

    if(count < preamblesize):
        preamble.append(newnumber)
        count+=1
    else:
        if numbersumsfrompreamble(preamble, newnumber):
            preamble.popleft()
            preamble.append(newnumber)
        else:
            print(newnumber)
            findsequence(newnumber,numbers)