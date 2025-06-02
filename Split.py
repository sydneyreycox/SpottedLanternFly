from os import mkdir

def split(inputFile, outputPath):
    inputLines = open(inputFile,'r',encoding='utf-8').readlines()
    years = []
    for i in range(2015,2025):
        outputName = outputPath+'/'+inputFile.split('/')[1].replace('.csv','')+str(i)+".csv"
        years.append(open(outputName,'w+',encoding='utf-8'))
    header = inputLines.pop(0)
    for y in years:
        y.write(header)


    for val in inputLines:
        broken = val.split(',')
        if(broken[3].startswith("2015")): 
            years[0].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])
        elif(broken[3].startswith("2016")): 
            years[1].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])
        elif(broken[3].startswith("2017")): 
            years[2].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])
        elif(broken[3].startswith("2018")): 
            years[3].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])
        elif(broken[3].startswith("2019")): 
            years[4].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])
        elif(broken[3].startswith("2020")): 
            years[5].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])
        elif(broken[3].startswith("2021")): 
            years[6].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])
        elif(broken[3].startswith("2022")): 
            years[7].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])
        elif(broken[3].startswith("2023")): 
            years[8].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])
        elif(broken[3].startswith("2024")): 
            years[9].write(broken[0] + "," + broken[1]+ "," + broken[2] + "," + broken[3])

def main():
    tags = ['datafiles/BWData_Pruned.csv','datafiles/GrData_Pruned.csv','datafiles/HpData_Pruned.csv',\
        'datafiles/RMData_Pruned.csv','datafiles/SMData_Pruned.csv','datafiles/TOHData_Pruned.csv',\
        'datafiles/LFData_Pruned.csv']
    locs = ['datefiles/BWDataSplit','datefiles/GrDataSplit','datefiles/HpDataSplit','datefiles/RMDataSplit',\
        'datefiles/SMDataSplit','datefiles/TOHDataSplit','datefiles/LFDataSplit']
    for l in locs:
        mkdir(l)
    for t,l in zip(tags,locs):
        split(t,l)
main() 