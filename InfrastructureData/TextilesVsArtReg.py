import csv

def csvtodict(filename):
    statecount = {}
    with open(filename, 'r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        for row in reader:
            state = row[11]
            if state in statecount:
                statecount[state] += 1
            else:
                statecount[state] = 1
                
    with open('InfrastructureData/2020PopulationData.csv', 'r', newline='') as popfile:
        popreader = csv.reader(popfile)
        next(popreader)
        for row in popreader:
            state = row[4]
            if state not in statecount:
                statecount[state] = 0
    return statecount

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

def getRegTextileCounts():
    stateReg = getStateReg('InfrastructureData/StateARTreg.csv')
    stateTextileCounts = csvtodict('InfrastructureData/TextileData.csv')
    regTextileCounts = {}
    for state in stateReg:
        reg = stateReg[state]
        if reg not in regTextileCounts:
            regTextileCounts[reg] = 0
        else:
            regTextileCounts[reg] += stateTextileCounts[state]
    return regTextileCounts


# data = csvtodict('InfrastructureData/TextileData.csv')
# dataSortedbyKey = {k: v for k, v in sorted(data.items(), key=lambda x: x[0])}
# print("State counts:", dataSortedbyKey)
print(getRegTextileCounts())