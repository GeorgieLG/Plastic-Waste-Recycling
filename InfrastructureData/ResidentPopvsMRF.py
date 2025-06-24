import csv
import MRFbyState

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
    mrf = {k: v for k, v in sorted(MRFbyState.csvtodict('InfrastructureData/CSVData/MRFdata.csv').items(), key=lambda x: x[0])}

    popObj = population.values()
    mrfObj = mrf.values()

    populationList = list(popObj)
    mrfList = list(mrfObj)
    return populationList, mrfList