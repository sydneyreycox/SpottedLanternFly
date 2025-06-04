truncData = []

file = open('datefiles\LFDataSplit\LFData_Pruned2015.csv','r',encoding = 'utf-8').readlines()[1:]
for line in file:
    lat,lon = map(float,line.split(',')[1:3])
    lat = int(lat * 10)/10
    lon = int(lon * 10)/10
    truncData.append([lon,lat])

B = [-125.0, -69.0, 25.0, 50.0]

stepsize = 0.1
maxla = 56.0/stepsize + 1
maxlo = 25.0/stepsize + 1
i = 0
tally = [[0.0]*int(maxla)]*int(maxlo)

while i < len(truncData):
    indexr = int((truncData[i][0] + 125)/stepsize)
    indexc = int((truncData[i][1] - 25)/stepsize)
    tally[indexr][indexc] += 1
    i += 1

print(tally)