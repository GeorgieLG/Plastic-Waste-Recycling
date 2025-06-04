import matplotlib.pyplot as plt
#import pandas as pd
import csv


def csvtodict(filename):
    statecount = {}
    with open(filename, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            state = row['State']
            if state in statecount:
                statecount[state] += 1
            else:
                statecount[state] = 1
    return statecount

data = csvtodict('InfrastructureData/InfrastructureData_cleaned.csv')
dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}

x = dataSortedbyValue.keys()  # Get the states from the dictionary
y = dataSortedbyValue.values()  # Get the counts for each state

nodups = list(set(x))  # Remove duplicates from the state list
print(len(nodups))

plt.bar(x, y)
plt.title('Infrastructure Data by State')
plt.xlabel('State')
plt.ylabel('Value')  # Replace 'Value' with the actual column name you want to plot
plt.show()
plt.savefig('InfrastructureData/InfrastructureData_by_state.pdf')

print("State counts:", csvtodict('InfrastructureData/InfrastructureData_cleaned.csv'))
nodups = list(set(x))  # Remove duplicates from the state list
print(len(nodups))