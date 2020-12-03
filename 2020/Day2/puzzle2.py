
def processLine(line):
    print(line)
    x = line.split(' ')
    print(x)
    min,max = x[0].split('-')
    print(min,max)
    find = x[1].split(':')[0]
    print(find)
    str = x[2]

    print(str[int(min)-1],str[int(max)-1])
    if bool(str[int(min)-1] == find) ^ bool(str[int(max)-1] == find):
        return True
    else:
        return False

vals=[]
f = open("Puzzle2.in")
for line in f:
    vals.append(line.strip('\n'))

print(vals)
count = 0
for line in vals:
    if processLine(line):
        print("Yes")
        count+=1

print(count)
