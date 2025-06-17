import matplotlib.pyplot as plt
import csv

#Parse csv file and return a dictionary with state as key and count of MRFs as value
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

# data = csvtodict('InfrastructureData/MRFdata.csv')
# dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}
# print("State counts:", dataSortedbyValue)