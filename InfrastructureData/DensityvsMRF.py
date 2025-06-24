import csv
import MRFbyState

#Parse csv file and return a dictionary with state as key and population density as value
def getPopDensity(filename):
    statePopDensity = {}
    with open(filename, 'r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        for row in reader:
            state = row[4]
            if state in statePopDensity:
                statePopDensity[state] += round(float(row[3]), 3)
            else:
                statePopDensity[state] = round(float(row[3]), 3)
    return {k: v for k, v in sorted(statePopDensity.items(), key=lambda x: x[0])} #Sort by state abbrev in alphabetical order

def getArrays():
    density = getPopDensity('InfrastructureData/CSVData/2020PopulationData.csv')
    MRF = {k: v for k, v in sorted(MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv').items(), key=lambda x: x[0])}

    densObj = density.values()
    MRFObj = MRF.values()

    densityList = list(densObj)
    MRFList = list(MRFObj)
    return densityList, MRFList





            