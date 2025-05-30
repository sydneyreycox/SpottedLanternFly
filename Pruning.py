inputLines = open("datafiles/LFData.csv",'r',encoding='utf-8').readlines()
prunedLF = open('datafiles/LFData_Pruned.csv','w+')
for val in inputLines:
  broken = val.split('\t')
  prunedLF.write(broken[0] + " " + broken[21]+ " " + broken[22] + " " + broken[29]+'\n')