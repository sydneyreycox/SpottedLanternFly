import numpy as np    
from scipy.stats import linregress
import matplotlib.pyplot as plt

def coordTal(path):
    data = []
    file = open(path,'r',encoding = 'utf-8').readlines()[1:]
    for line in file:
        lat,lon = map(float,line.split(',')[1:3])
        data.append([lon,lat])

    B = [-75.0, -73.0, 39.0, 41.0]

    stepsize = 0.1
    maxla = (B[1] - B[0])/stepsize + 1
    maxlo = (B[3] - B[2])/stepsize + 1
    tally = [[0.0 for _ in range(int(maxla))] for _ in range(int(maxlo))]

    

    for val in data:
        if val[0] <= B[1] and val[0] >= B[0]:
            #print(maxla, maxlo)
            #print(int((val[1]-B[2])/stepsize),int((val[0]-B[0])/stepsize))
            if val[1] <= B[3] and val[1] >= B[2]:
                tally[int((val[1]-B[2])/stepsize)][int((val[0]-B[0])/stepsize)]+=1
        
    '''for x,val in enumerate(tally):
        for y,index in enumerate(val):
            if(index!=0): print(round(x*stepsize+25,1),round(y*stepsize-125,1),index)'''

    return tally


graphData = []

tallySLF = coordTal('datafiles/LFData_Pruned.csv')
tallyT = coordTal('datafiles/ASData_Pruned.csv')

for x,val in enumerate(tallyT):
    for y in range(len(val)):
        graphData.append((tallyT[x][y], tallySLF[x][y]))

graphData = np.array(graphData)
TPoints = graphData[:,0]
SLFPoints = graphData[:,1]

slope, intercept, r_value, p_value, std_err = linregress(TPoints, SLFPoints)

predicted = intercept + slope * TPoints

print(r_value,p_value)
plt.figure(figsize=(8, 5))
plt.plot(TPoints, SLFPoints, 'o', label="Observations per Bin")
plt.plot(TPoints, predicted, 'r--', label=f"Linear Fit (R²={r_value**2:.3f}, Fit={slope:.3f}x+{intercept:.3f})")
plt.title("SLF Observations to AS Observations with Linear Fit")
plt.xlabel("Tree Observations")
plt.ylabel("SLF Observations")
plt.legend()
plt.grid(True)
plt.show()