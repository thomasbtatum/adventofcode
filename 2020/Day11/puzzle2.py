import copy

def countoccupied(seats):
    count = 0
    for i in range(0,len(seats)):
        for j in range(0,len(seats[0])):
            if seats[i][j] == '#':
                count+=1
    return count

def printseats(seats):
    for i in range(0,len(seats)):
        for j in range(0,len(seats[0])):
            print(seats[i][j]),
        print('\n')

def compareseats(sr1,sr2):
    for x in range(0,len(sr1)):
        for y in range(0,len(sr1[0])):
            if(sr1[x][y]!= sr2[x][y]):
                return False
    return True

def analyzeseat(seats,row,col,chrow,chcol):
    row+=chrow
    col+=chcol
    while row >= 0 and col >= 0 and row < len(seats) and col < len(seats[0]):
        if seats[row][col] == '#':
            return 1
        elif seats[row][col] == 'L':
            return 0
        else:
            row+=chrow
            col+=chcol
    return 0

def simulateSeating(seats):
    newSeats = []
    for i in range(0,len(seats)):
        row = []
        for j in range(0,len(seats[0])):
            if seats[i][j] == '.':
                row.append('.')
                continue

            count = 0
            for x in ['n','ne','e','se','s','sw','w','nw']:
                if x == 'n':
                    count+=analyzeseat(seats,i,j,-1,0)
                if x == 'ne':
                    count+=analyzeseat(seats,i,j,-1,1)
                if x == 'e':
                    count+=analyzeseat(seats,i,j,0,1)
                if x == 'se':
                    count+=analyzeseat(seats,i,j,1,1)
                if x == 's':
                    count+=analyzeseat(seats,i,j,1,0)
                if x == 'sw':
                    count+=analyzeseat(seats,i,j,1,-1)
                if x == 'w':
                    count+=analyzeseat(seats,i,j,0,-1)
                if x == 'nw':
                    count+=analyzeseat(seats,i,j,-1,-1)
            if seats[i][j] == '#' and count > 4:
                row.append('L')
            elif seats[i][j] == 'L' and count == 0:
                row.append('#')
            else:
                row.append(seats[i][j])
        newSeats.append(row)
    return newSeats
 
f = open("Puzzle1.in")

seatrows = []
for line in f:
    seatrows.append(list(line.strip('\n')))



#printseats(seatrows)
nextseats = simulateSeating(seatrows)
#print('-')
#printseats(nextseats)
#print('-')

while(not compareseats(seatrows,nextseats)):
    seatrows = copy.deepcopy(nextseats)
    nextseats = simulateSeating(nextseats)
    #printseats(nextseats)
    #print('-')

print(countoccupied(nextseats))