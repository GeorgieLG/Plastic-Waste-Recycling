import csv

def getRates(inputfile):
    rates = {}
    statePercentage = {}
    with open(inputfile, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if row[11] != '':
                if row[11] not in rates:
                    if row[6] != '' and row[7] != '':
                        rates[row[11]] = [float(row[6]), float(row[7])]
                else:
                    if row[6] != '' and row[7] != '':
                        rates[row[11]][0] += float(row[6])
                        rates[row[11]][1] += float(row[7])
    for state in rates:
        statePercentage[state] = (rates[state][1] / rates[state][0]) * 100
                                               
    return statePercentage

def getTotalUSRate(statePercentage):
    counter = 0
    total = 0
    for state in statePercentage:
        counter += 1
        total += statePercentage[state]
    
    return (total / counter)
