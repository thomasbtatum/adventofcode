

def getTrees(slope):
    height = len(vals)
    width = len(line)

    rise,run = slope[0],slope[1]

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
    return countTrees

vals=[]
f = open("Puzzle1.in")
for line in f:
    vals.append(line.strip('\n'))

slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]

val = 1

for slope in slopes:
    temp = getTrees(slope)
    print(slope[0],slope[1],temp)
    val *= temp

print(val)