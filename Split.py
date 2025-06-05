from os import mkdir

#Go through and split each name into the bins of years, then output to location
def split(inputFile, outputPath):
    inputLines = open(inputFile,'r',encoding='utf-8').readlines()
    #Generate an array of files for each year for the given output path
    years = []
    for i in range(2015,2025):
        outputName = outputPath+'/'+inputFile.split('/')[1].replace('.csv','')+str(i)+".csv"
        years.append(open(outputName,'w+',encoding='utf-8'))
    header = inputLines.pop(0)
    for y in years:
        y.write(header)
    #Itterate through the data and write into the fiels as bins, convert to comma separated
    for val in inputLines:
        broken = val.split(',')
        #Lazy, but it doesn't matter, was one of our first programs
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    tags = ['datafiles/BWData_Pruned.csv','datafiles/GrData_Pruned.csv','datafiles/HpData_Pruned.csv',\
        'datafiles/RMData_Pruned.csv','datafiles/SMData_Pruned.csv','datafiles/TOHData_Pruned.csv',\
        'datafiles/LFData_Pruned.csv','datafiles/LBData_Pruned.csv','datafiles/ASData_Pruned.csv']
    locs = ['datefiles/BWDataSplit','datefiles/GrDataSplit','datefiles/HpDataSplit','datefiles/RMDataSplit',\
        'datefiles/SMDataSplit','datefiles/TOHDataSplit','datefiles/LFDataSplit','datefiles/LBDataSplit','datefiles/ASDataSplit']
    #Make all the files in locs
    for l in locs:
        mkdir(l)
    #Call split on all the pruned files
    for t,l in zip(tags,locs):
        split(t,l)
main() 