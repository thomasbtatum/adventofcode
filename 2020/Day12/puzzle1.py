
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

x,y = 0,0
direction = 'E'

print(instructions)

for instruction in instructions:
    key = instruction[0]
    amt = int(instruction[1:])
    if key == 'N':
        y-=amt
    elif key == 'S':
        y+=amt
    elif key == 'E':
        x+=amt
    elif key == 'W':
        x-=amt
    elif key == 'L':
        direction = changeDir(direction,'L',amt)
    elif key == 'R':
        direction = changeDir(direction,'R',amt)
    else: #f 
        if direction == 'N':
            y-=amt
        elif direction == 'S':
            y+=amt
        elif direction == 'E':
            x+=amt
        elif direction == 'W':
            x-=amt
    print(x,y,x+y,instruction,direction)