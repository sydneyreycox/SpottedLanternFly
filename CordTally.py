
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
#lo1 = B[2]
lo2 = B[3]
r1 = len(truncData)
r2 = 0
tally = 0

while la1 < la2:
    #print('la1:',la1)
    lo1 = B[2]
    while lo1 < lo2:
        t1 = 0
        #print('\n',truncData[t1][0], truncData[t1][1])
        #print('lo1:',lo1)
        while t1 < r1:
            #print('t1',t1)
            if(truncData[t1][0] == la1 and truncData[t1][1] == lo1):
                tally += 1  
                #print('\n',truncData[t1][0], truncData[t1][1])
            t1 += 1
        lo1 = round(lo1 + 0.1, 1)
    la1 = round(la1 + 0.1, 1)

print(tally)

#for la in range(B[0], B[1]):
 #   print(la)
   # for lo in range(B[2], B[3]):
       # if(truncData[lo][la]):