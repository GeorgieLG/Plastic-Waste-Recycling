import csv

def readStates(filename):
    states = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            states[row[0]] = row[4]
    return states

#print(readStates('InfrastructureData/CSVData/2020PopulationData.csv'))
