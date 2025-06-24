import csv

def getTotalYearlyEmissions(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        total_emissions = {} #2-54
        for i in range(2,55):
            total_emissions[header[i]] = 0.0
        for row in reader:
            for i in range(2, 55):
                emissions = float(row[i])
                total_emissions[header[i]] += emissions
    return total_emissions
