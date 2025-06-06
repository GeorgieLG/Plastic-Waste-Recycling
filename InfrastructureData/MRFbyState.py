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
    return statecount

# def main():
#     data = csvtodict('InfrastructureData/MRFdata.csv')
#     dataSortedbyValue = {k: v for k, v in sorted(data.items(), key=lambda x: x[1], reverse=True)}

#     x = dataSortedbyValue.keys()  # Get the states from the dictionary
#     y = dataSortedbyValue.values()  # Get the counts for each state

#     f = plt.figure()
#     f.set_figwidth(15)

#     plt.bar(x, y)
#     plt.title('Number of MRFs by State')
#     plt.xlabel('State')
#     plt.ylabel('# of Sites')
#     plt.savefig('InfrastructureData/MRFdatabystate.pdf')
#     plt.show()

#     print("State counts:", dataSortedbyValue)
#     nodups = list(set(x))  # Remove duplicates from the state list
#     print(len(nodups))