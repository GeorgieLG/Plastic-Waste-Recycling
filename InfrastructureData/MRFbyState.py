import matplotlib.pyplot as plt
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

data = csvtodict('InfrastructureData/MRFdata.csv')
dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}

x = dataSortedbyValue.keys()  # Get the states from the dictionary
y = dataSortedbyValue.values()  # Get the counts for each state

f = plt.figure()
f.set_figwidth(15)

plt.bar(x, y)
plt.title('Number of MRFs by State')
plt.xlabel('State')
plt.ylabel('# of Sites')
plt.savefig('InfrastructureData/MRFdatabystate.pdf')
plt.show()

print("State counts:", dataSortedbyValue)
nodups = list(set(x))  # Remove duplicates from the state list
print(len(nodups))