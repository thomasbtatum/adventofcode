# Part 2: 
#credit where credit is due:
#this solution was found in comments of JP YouTube channel
#worked like a charm!
#https://www.youtube.com/watch?v=x40aLK9KjYQ


f = open("Puzzle1.in")

first = True
for line in f:
    if first:
        first = False
        departure = int(line.strip('\n'))
    else:
        buses = line.strip('\n')

departure_list = buses.split(',')

iFactor = 1

iBusNr = 1
iTime = 0
for Bus in departure_list:
    if Bus == 'x':
        iBusNr += 1
        continue
    
    while (iTime + iBusNr) % int(Bus) > 0:
        iTime += iFactor

    iFactor *= int(Bus)

    #print iBusNr, Bus, iTime, iFactor
    
    iBusNr += 1


p2 = iTime + 1
print(p2)