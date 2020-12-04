vals=[]
f = open("Puzzle1.in")
for line in f:
    vals.append(line.strip('\n'))

rise = 1
run = 3
height = len(vals)
width = len(line)

print(vals)
print(rise, run, height, width)

countTrees = 0
row = rise
col = run

while row < height:
    print(row, col)
    print(vals[row][col])
    if(vals[row][col] == '#'):
        countTrees+=1
    row += rise
    col += run 
    col %= width

print(countTrees)