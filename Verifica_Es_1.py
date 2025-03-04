città=['milano', 'roma', 'napoli']
tmax=[28, 31, 34]
tmin=[18, 21, 24]
for i in range (len(tmax)):
    mediaMax+=tmax
for i in range (len(tmin)):
    mediaMin+=tmin
for i in range (len(città)):
    if(tmin[i]<mediaMin[i]):
        print("Le città",città[i],"ha avuto una temperatura sotto la media.")
        


