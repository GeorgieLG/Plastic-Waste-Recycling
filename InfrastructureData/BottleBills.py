import csv
import GetStatAbbr
import LandfillTippingFees

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

def getBottleBills(inputfile):
    bottleBills = {}
    with open(inputfile, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            bottleBills[row[9]] = row[2]

    return bottleBills

def bottleBillvsTippingFees():
    retVar = {}
    bottleBills = getBottleBills('RecyclingMarketFactors/CSVData/BottleBillsbyState_cleaned.csv')
    tippingFees = LandfillTippingFees.getTippingFees('RecyclingMarketFactors/CSVData/LandfillTippingFees_cleaned.csv')

    billCounts = {}
    for state in bottleBills:
        bill = bottleBills[state]
        if bill not in billCounts:
            billCounts[bill] = 1
        else:
            billCounts[bill] += 1
    
    for state in bottleBills:
        bill = bottleBills[state]
        fee = tippingFees[state]
        if bill not in retVar:
            retVar[bill] = fee
        else:
            retVar[bill] += fee

    for bill in retVar:
        retVar[bill] /= billCounts[bill]
    return retVar


#getStateAbbr('RecyclingMarketFactors/CSVData/BottleBillsbyState.csv', 'RecyclingMarketFactors/CSVData/BottleBillsbyState_cleaned.csv')

#print(bottleBillvsTippingFees())