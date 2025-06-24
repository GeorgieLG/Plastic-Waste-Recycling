import csv
import AnyInfraByState

def getPopulation(filename):
    statePopulation = {}
    with open(filename, 'r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        for row in reader:
            state = row[4]
            if state in statePopulation:
                statePopulation[state] += int(row[1])
            else:
                statePopulation[state] = int(row[1])
    return {k: v for k, v in sorted(statePopulation.items(), key=lambda x: x[0])}  # Sort by state abbrev in alphabetical order

def getArrays():
    population = getPopulation('InfrastructureData/CSVData/2020PopulationData.csv')
    infra = {k: v for k, v in sorted(AnyInfraByState.csvtodict('InfrastructureData/CSVData/InfrastructureData_cleaned.csv').items(), key=lambda x: x[0])}

    popObj = population.values()
    infraObj = infra.values()

    populationList = list(popObj)
    infraList = list(infraObj)
    return populationList, infraList


