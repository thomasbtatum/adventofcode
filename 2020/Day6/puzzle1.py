f = open("Puzzle1.in")
vals = []
group = ''
for line in f:

    if line == '\n':
        vals.append(group)
        group = ''
    else:
        group += line.strip('\n')

    
print(vals)

count = 0
for val in vals:
    count += len(set(val))

print(count)