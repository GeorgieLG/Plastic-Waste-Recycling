import csv
import AnyInfraByState

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

#print(getPopDensity('InfrastructureData/2020PopulationData.csv'))

#print({k: v for k, v in sorted(AnyInfraByState.csvtodict('InfrastructureData/InfrastructureData_cleaned.csv').items(), key=lambda x: x[0])})

def getArrays():
    density = getPopDensity('InfrastructureData/2020PopulationData.csv')
    infra = {k: v for k, v in sorted(AnyInfraByState.csvtodict('InfrastructureData/InfrastructureData_cleaned.csv').items(), key=lambda x: x[0])}

    densObj = density.values()
    infraObj = infra.values()

    densityList = list(densObj)
    infraList = list(infraObj)
    return densityList, infraList

# densityList, infraList = getArrays()

# print("Population Density List:", densityList, "Length:", len(densityList), "\n")
# print("Infrastructure List:", infraList, "Length:", len(infraList), "\n")

