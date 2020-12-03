
def processLine(line):
    print(line)
    x = line.split(' ')
    print(x)
    min,max = x[0].split('-')
    print(min,max)
    find = x[1].split(':')[0]
    print(find)
    str = x[2]
    print(str)

    if str.count(find) >= int(min) and str.count(find) <= int(max):
        return True
    else:
        return False

vals=[]
f = open("Puzzle1.in")
for line in f:
    vals.append(line.strip('\n'))

print(vals)
count = 0
for line in vals:
    if processLine(line):
        count+=1

print(count)
