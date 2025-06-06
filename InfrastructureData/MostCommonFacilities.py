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

#print(mostCommonFacilities('InfrastructureData/InfrastructureData_cleaned.csv'))

