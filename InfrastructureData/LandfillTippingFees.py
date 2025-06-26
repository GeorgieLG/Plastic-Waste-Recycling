import csv
import GetStatAbbr
import RegvsRecyclingRate

def getTippingFees(inputfile):
    tippingFees = {}
    with open(inputfile, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if row[5] != '' and row[2] != '':
                tippingFees[row[5]] = float(row[2])
    return tippingFees

def getStateAbbr(input, output):
    states = GetStatAbbr.readStates('InfrastructureData/CSVData/2020PopulationData.csv')
    with open(input, 'r', newline='') as infile:
        with open(output, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            header = next(reader)
            writer.writerow(header + ['StateAbbr'])
            for row in reader:
                if row[1] != '' and row[1] != 'District of Columbia':
                    writer.writerow(row + [states[row[1]]])

def regvsTippingFees():
    retVar = {}
    tippingFees = getTippingFees('RecyclingMarketFactors/CSVData/LandfillTippingFees_cleaned.csv')
    regData = RegvsRecyclingRate.getStateReg('InfrastructureData/CSVData/StateARTreg.csv')

    regCounts = {}

    with open('InfrastructureData/CSVData/StateARTreg.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if row[2] not in regCounts:
                regCounts[row[2]] = 1
            else:
                regCounts[row[2]] += 1

    for state in tippingFees:
        fee = tippingFees[state]
        reg = regData[state]
        if reg not in retVar:
            retVar[reg] = fee
        else:
            retVar[reg] += fee
    
    for reg in retVar:
        retVar[reg] /= regCounts[reg]
    return retVar

#getStateAbbr('RecyclingMarketFactors/CSVData/LandfillTippingFees.csv', 'RecyclingMarketFactors/CSVData/LandfillTippingFees_cleaned.csv')
#print(regvsTippingFees())