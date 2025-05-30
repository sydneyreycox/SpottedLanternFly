inputLines = open("LFData.csv",'r').readLines()
prunedLF = open('LFData_Pruned.csv','w+')
for val in inputLines:
  broken = val.split('\s')
  prunedLF.write(broken[0] + " " + broken[24] + broken[29]+'\n')