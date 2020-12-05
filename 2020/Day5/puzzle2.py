

import bisect

def idofseat(row,seat):
    return row * 8 + seat

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
    #return rows[0] * 8 + seats[0]
    return rows[0],seats[0]

f = open("Puzzle1.in")

planemap = {}

for line in f:
    line = line.strip('\n') 
    
    row,seat = processline(line)
    if row not in planemap:
        planemap[row] = [seat]
    else:
        bisect.insort(planemap[row],seat)

print(planemap)
#items = sorted(boardingpasses.items(), key=lambda x: x[1], reverse=True)
#print(items)

for r in range(5,100):
    if r == 0 or r == 127:
        continue
    if r not in planemap:
        print("key not found=",r)
    diff = set(range(0,8)).difference(planemap[r])
    if(diff):
        print("bad row was:",r)
        print(planemap[r])
        print("Id is:" , idofseat(r,list(diff)[0]))