import csv
import matplotlib.pyplot as plt

def mostCommonFacilities(input_file):
    facCount = {}
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            facility = row[9]
            if facility in facCount:
                facCount[facility] += 1
            else:
                facCount[facility] = 1
    sorted_facilities = {k: v for k, v in sorted(facCount.items(), key=lambda x: x[1], reverse=True)}
    return sorted_facilities

print(mostCommonFacilities('InfrastructureData/InfrastructureData_cleaned.csv'))

facilities = mostCommonFacilities('InfrastructureData/InfrastructureData_cleaned.csv')

x = facilities.keys() # Get the facilities from the dictionary
y = facilities.values() # Get the counts for each facility
f = plt.figure()
f.set_figwidth(10)

plt.barh(x, y)
plt.title('Most Common Facilities')
plt.ylabel('Facility Type')
plt.xlabel('# of Sites')
plt.subplots_adjust(left=.25, bottom=None, right=.883, top=None, wspace=None, hspace=None)
plt.savefig('InfrastructureData/MostCommonFacilities.pdf')
plt.show()