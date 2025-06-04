data = []

file = open('datefiles\TOHDataSplit\TOHData_Pruned2015.csv','r',encoding = 'utf-8').readlines()[1:]
for line in file:
    lat,lon = map(float,line.split(',')[1:3])
    data.append([lon,lat])

B = [-125.0, -69.0, 25.0, 50.0]

stepsize = 0.1
maxla = 56.0/stepsize + 1
maxlo = 25.0/stepsize + 1
i = 0
tally = [[0.0 for _ in range(int(maxla))] for _ in range(int(maxlo))]

for val in data:
    tally[int((val[1]-25)/stepsize)][int((val[0]+125)/stepsize)]+=1
    
for x,val in enumerate(tally):
    for y,index in enumerate(val):
        if(index!=0): print(round(x*stepsize+25,1),round(y*stepsize-125,1),index)