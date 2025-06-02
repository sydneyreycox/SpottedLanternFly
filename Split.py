def split(inputFile, outputFile):
    inputLines = open(inputFile,'r',encoding='utf-8').readlines()
    split2015 = open(outputFile,'w+',encoding='utf-8')
    split2016 = open(outputFile,'w+',encoding='utf-8')
    split2017 = open(outputFile,'w+',encoding='utf-8')
    split2018 = open(outputFile,'w+',encoding='utf-8')
    split2019 = open(outputFile,'w+',encoding='utf-8')
    split2020 = open(outputFile,'w+',encoding='utf-8')
    split2021 = open(outputFile,'w+',encoding='utf-8')
    split2022 = open(outputFile,'w+',encoding='utf-8')
    split2023 = open(outputFile,'w+',encoding='utf-8')
    split2024 = open(outputFile,'w+',encoding='utf-8')
    split2025 = open(outputFile,'w+',encoding='utf-8')

    for val in inputLines:
        broken = val.split('\t')
        if(broken[29].startswith("2015")): 
            split2015.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2016")): 
            split2016.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2017")): 
            split2017.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2018")): 
            split2018.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2019")): 
            split2019.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2020")): 
            split2020.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2021")): 
            split2021.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2022")): 
            split2022.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2023")): 
            split2023.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2024")): 
            split2024.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
        elif(broken[29].startswith("2025")): 
            split2025.write(broken[0] + "," + broken[21]+ "," + broken[22] + "," + broken[29]+'\n')
            
split('datafiles/BWData_Pruned.csv','datafiles/BWData_Split.csv')
split('datafiles/GrData_Pruned.csv','datafiles/GrData_Split.csv')
split('datafiles/HpData_Pruned.csv','datafiles/HpData_Split.csv')
split('datafiles/RMData_Pruned.csv','datafiles/RMData_Split.csv')
split('datafiles/SMData_Pruned.csv','datafiles/SMData_Split.csv')
split('datafiles/TOHData_Pruned.csv','datafiles/TOHData_Split.csv')
split('datafiles/LFData_Pruned.csv','datafiles/LFData_Split.csv')