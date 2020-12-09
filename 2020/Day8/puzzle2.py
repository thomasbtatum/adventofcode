import copy

def testbootcode(bootcode):

    acc = 0
    SEEN = set()
    idx = 0
    while True:

        if idx == len(bootcode):
            return acc
        if idx in SEEN:
            print('infinite loop')
            return -1

        SEEN.add(idx)

        op,arg = bootcode[idx]

        if op == 'jmp':
            idx+=arg
        else:
            idx+=1

        if op == 'acc':
            acc+=arg


f = open("Puzzle1.in")
originalbootcode = []
for line in f:
    op,arg = line.strip('\n').split()
    originalbootcode.append([op,int(arg)])

accumulator = -1
idx = 0
jmpflag = True

while accumulator == -1:
    if jmpflag:
        if(originalbootcode[idx][0] == 'jmp'):
            localboot = copy.deepcopy(originalbootcode)
            localboot[idx][0] = 'nop'
            accumulator = testbootcode(localboot)
        jmpflag = False
    else:
        if(originalbootcode[idx][0] == 'nop'):
            localboot = copy.deepcopy(originalbootcode)
            localboot[idx][0] = 'jmp'
            accumulator = testbootcode(localboot)
        jmpflag = True
        idx+=1

print(accumulator)