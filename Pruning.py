def prune(inputFile, outputFile):
    inputLines = open(inputFile,'r',encoding='utf-8').readlines()
    prunedLF = open(outputFile,'w+',encoding='utf-8')
    for val in inputLines:
        broken = val.split('\t')
        if(not "" in [broken[0],broken[21],broken[22],broken[29]]): 
            prunedLF.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
prune('datafiles/BW Data.csv','datafiles/BWData_Pruned.csv')
prune('datafiles/Grape Data.csv','datafiles/GrData_Pruned.csv')
prune('datafiles/Hops Data.csv','datafiles/HpData_Pruned.csv')
prune('datafiles/RM Data.csv','datafiles/RMData_Pruned.csv')
prune('datafiles/SM Data.csv','datafiles/SMData_Pruned.csv')
prune('datafiles/TOH Data.csv','datafiles/TOHData_Pruned.csv')
prune('datafiles/LF Data.csv','datafiles/LFData_Pruned.csv')
prune('datafiles/ASData.csv','datafiles/ASData_Pruned.csv')
#prune('datafiles/LB Data.csv','datafiles/LBData_Pruned.csv')
print('finished')