fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

vals=[]
f = open("Puzzle1.in")
passport = ''
for line in f:
    if line == '\n':
        vals.append(passport)
        passport = ''
    else:
        passport += line.strip('\n')
        passport += ' '

print(vals)

countvalid = 0


for passport in vals:
    copyfields = list(fields)

    data = passport.split(' ')
    for item in data:
        c = item.split(':')[0]
        if len(c) > 0:
            if len(c) != 3:
                y=1

            if c in copyfields:
                copyfields.remove(c)
            else:
                x=1
    
    if len(copyfields) == 0 or (len(copyfields) == 1 and copyfields[0] == 'cid'):
        isvalid = True
        countvalid+=1
    else:
        isvalid = False

    with open('valid.txt', 'a') as the_file:
        data.sort()
        the_file.write("%s " % isvalid)
        for d in data:
            the_file.write("%s " % d.split(':')[0])
        the_file.write("\n")
        
print(countvalid)
