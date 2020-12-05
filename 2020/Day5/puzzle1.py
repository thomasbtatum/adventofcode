
def processline(line):
    rows = list(range(0,128))
    for i in range(7):
        if line[i] == 'F':
            rows = rows[:len(rows)//2]
        else:
            rows = rows[len(rows)//2:]
    print("row=",rows)

    seats = list(range(0,8))
    for j in range(7,10):
        if line[j] == 'L':
            seats = seats[:len(seats)//2]
        else:
            seats = seats[len(seats)//2:]  
    print("seat=",seats)
    return rows[0] * 8 + seats[0]

f = open("Puzzle1.in")
boardingpasses = {}
for line in f:
    line = line.strip('\n') 
    
    id = processline(line)
    boardingpasses[line] = id

#print(boardingpasses)
items = sorted(boardingpasses.items(), key=lambda x: x[1], reverse=True)
print(items)