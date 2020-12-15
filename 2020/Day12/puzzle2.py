
def changeDir(dir,turndir,degrees):
    returndir = dir
    while degrees > 0:
        if turndir == 'R':
            if returndir == 'N':
                returndir = 'E'
            elif returndir == 'E':
                returndir = 'S'        
            elif returndir == 'S':
                returndir = 'W'
            else: #returndir == 'W':
                returndir = 'N'
        else:
            if returndir == 'N':
                returndir = 'W'
            elif returndir == 'E':
                returndir = 'N'        
            elif returndir == 'S':
                returndir = 'E'
            else: #returndir == 'W':
                returndir = 'S'

        degrees-=90
    return returndir


f = open("Puzzle1.in")

instructions = []
for line in f:
    instructions.append(line.strip('\n'))

wayx,wayy = 10,1
x,y = 0,0

print(instructions)
print(x,y,x+y,0,wayx,wayy)

for instruction in instructions:
    key = instruction[0]
    amt = int(instruction[1:])
    if key == 'N':
        wayy+=amt
    elif key == 'S':
        wayy-=amt
    elif key == 'E':
        wayx+=amt
    elif key == 'W':
        wayx-=amt
    elif key == 'L':
        while amt > 0:
            temp = wayx
            wayx = -1*wayy
            wayy = temp
            amt-=90
    elif key == 'R':
        while amt > 0:
            temp = wayy
            wayy = -1*wayx
            wayx = temp
            amt-=90
    else: #f 
        x+=(amt*wayx)
        y+=(amt*wayy)
    print(x,y,abs(x)+abs(y),instruction,wayx,wayy)