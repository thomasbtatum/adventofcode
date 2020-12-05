import string

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

def isyearbetween(yr,low,high):
    if yr and yr.isdigit():
        return int(yr) >= low and int(yr) <= high
    return False

def isvalidheight(ht):
    amt = ht[:-2]

    if ht.endswith('cm'):
        return int(amt) >= 150 and int(amt) <= 193
    if ht.endswith('in'):
        return int(amt) >= 59 and int(amt) <= 76
    return False

def isvalidhaircolor(hc):

    if hc[0] != "#" or len(hc) != 7:
        return False
    
    hcolor = hc[1:]
    for c in hcolor:
        if c not in string.hexdigits:
            return False
            
    return True

def validValues(vals):
    ret = True

    for v in vals:
        if v:
            if not ret:
                return False
            k,v = v.split(":")

            if k == fields[0]:
                #byr 4d 1920-2002
                ret = isyearbetween(v,1920,2002)
            elif k == fields[1]:
                #iyr 4d 2010-2020
                ret = isyearbetween(v,2010,2020)
            elif k == fields[2]:
                #eyr 4d 2020-2030
                ret = isyearbetween(v,2020,2030)
            elif k == fields[3]:
                #hgt xxxcm or xxin
                #cm 150-193  in 59-76
                ret = isvalidheight(v)
            elif k == fields[4]:
                #hcl
                ret = isvalidhaircolor(v)
            elif k == fields[5]:
                #ecl
                ret = v in ['amb','blu','brn','gry','grn','hzl','oth']
            elif k == fields[6]:
                ret = v and v.isdigit() and len(v) == 9
                #pid

    return ret   

vals=[]
f = open("Puzzle2.in")
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
        if validValues(data):
            countvalid+=1
    else:
        isvalid = False
        
print(countvalid)
