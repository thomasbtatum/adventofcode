f = open("Puzzle1.in")
vals = []
group = []
for line in f:

    if line == '\n':
        vals.append(group)
        group = []
    else:
        group.append(line.strip('\n'))

    
print(vals)
total = 0
count = 0
for val1 in vals:
    seed = ''
    count = 0
    for val in val1:
        if count == 0:
            seed = set(val)
        else:
            seed = set(val).intersection(seed) 
            if(len(seed) == 0):
                break

        count+=1

    total += len(seed)

print(total)