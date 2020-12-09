f = open("Puzzle1.in")
bootcode = []
for line in f:
    op,arg = line.strip('\n').split()
    bootcode.append([op,int(arg)])

acc = 0
SEEN = set()
idx = 0
while True:

    if idx in SEEN:
        print(acc)
        quit()

    SEEN.add(idx)

    op,arg = bootcode[idx]

    if op == 'jmp':
        idx+=arg
    else:
        idx+=1

    if op == 'acc':
        acc+=arg

print(bootcode)