
truncData = []

file = open('datefiles\LFDataSplit\LFData_Pruned2015.csv','r',encoding = 'utf-8').readlines()[1:]
for line in file:
    lat,lon = map(float,line.split(',')[1:3])
    lat = int(lat * 10)/10
    lon = int(lon * 10)/10
    truncData.append([lon,lat])
#print(truncData)

B = [-125.0, -69.0, 25.0, 50.0]
la1 = B[0]
la2 = B[1]
lo2 = B[2]
r1 = len(truncData)
r2 = 0
tally = []
index = 0


while la1 < la2:
    #print('la1:',la1)
    lo1 = B[3]
    while lo1 > lo2:
        t1 = 0
        #print('\n',truncData[t1][0], truncData[t1][1])
        #print('lo1:',lo1)
        indexr = 0
        while t1 < r1:
            #print('t1',t1)
            present = 0
            if(truncData[t1][0] == la1 and truncData[t1][1] == lo1):
                #present += 1
                found = False
                for pair in tally:
                    if pair[0] == index:
                        pair[1] += 1 
                        found = True
                        break
                if not found:
                    tally.append([index,indexr, 1])
                #tally.append([index,present])  
                #print('\n',truncData[t1][0], truncData[t1][1])
            t1 += 1
        lo1 = round(lo1 - 0.1, 1)
        indexr += 1
    index += 1
    la1 = round(la1 + 0.1, 1)
    #print(index)

print(tally)