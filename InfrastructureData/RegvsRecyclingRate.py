import csv

def getStateReg(filename):
    stateReg = {}
    with open(filename, 'r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        for row in reader:
            state = row[0]
            reg = row[2]
            stateReg[state] = reg
    stateRegSorted = {k: v for k, v in sorted(stateReg.items(), key=lambda x: x[0])}
    return stateRegSorted

def get_recycling_percentage_by_state(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        recycling_data = {}
        
        for row in reader:
            state = row[0]
            recycling_percentage = int(row[2])
            recycling_data[state] = recycling_percentage
        
        sorted_data = {k: v for k, v in sorted(recycling_data.items(), key=lambda x: x[0])}
    
    return sorted_data

def getAvgPercentageByReg():
    regulation = getStateReg('InfrastructureData/CSVData/StateARTreg.csv')
    recycling_percentage = get_recycling_percentage_by_state('InfrastructureData/CSVData/RecyclingPercentageByState.csv')
    reg_avg_percentage = {}

    countMan = 0
    totalMan = 0
    for state in regulation:
        reg = regulation[state]
        if reg == 'MAN':
            countMan += 1
            totalMan += recycling_percentage[state]
    reg_avg_percentage['MAN'] = totalMan / countMan

    countSW = 0
    totalSW = 0
    for state in regulation:
        reg = regulation[state]
        if reg == 'SW':
            countSW += 1
            totalSW += recycling_percentage[state]
    reg_avg_percentage['SW'] = totalSW / countSW

    return reg_avg_percentage