from datetime import datetime, date, timedelta

f = open("Puzzle1-sample.in")

departure = 0
first = True
for line in f:
    if first:
        first = False
        departure = int(line.strip('\n'))
    else:
        buses = line.strip('\n')

schedule = {}
maxminute = departure+101
for i in range(0,maxminute):
    schedule[i] = 0

thebusses = buses.split(',')
for bus in thebusses:
    if bus == 'x':
        continue
    #print(bus)
    v = int(bus)
    #d = datetime(2002, 12, 31)
    #d += timedelta(minutes = v)
    #r = d.day
    count = v
    while count < maxminute:
        #k = int(datetime.strftime(d,"%-H%M"))
        schedule[count] = v
        #d += timedelta(minutes = v)
        count+=v

startkey = departure
diff = 0
while schedule[startkey] == 0:
    startkey+=1
    diff+=1

print(schedule[startkey] * diff)

#print(schedule)