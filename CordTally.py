
truncData = []
file = open('datefiles\LFDataSplit\LFData_Pruned2015.csv','r',encoding = 'utf-8').readlines()[1:]

for line in file:  #Data is truncated to a single decimal place for each lat and long value
    lat,lon = map(float,line.split(',')[1:3])
    lat = int(lat * 10)/10
    lon = int(lon * 10)/10
    truncData.append([lon,lat])

B = [-125.0, -69.1, 25.0, 50.1] #initialization of the max coordinate values being used in creating the 2D array
la1 = B[0]
la2 = B[1]
lo2 = B[2]
r1 = len(truncData)
tally = []
indexr = 0

while la1 < la2:
    lo1 = B[3]
    index = 0
    while lo1 > lo2:
        t1 = 0
        while t1 < r1:
            if(truncData[t1][0] == la1 and truncData[t1][1] == lo1):
                found = False
                for pair in tally:
                    if pair[0] == index and pair[1] == indexr:
                        pair[2] += 1 
                        found = True
                        break
                if not found:
                    tally.append([index,indexr, 1]) # [longitude_col, latitude_row, count]
            t1 += 1
        lo1 = round(lo1 - 0.1, 1)
        index += 1
    la1 = round(la1 + 0.1, 1)
    indexr += 1

print(tally)