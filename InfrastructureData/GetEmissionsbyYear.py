import csv

def get_emissions_by_year(file_path, year):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for i in range(len(header)):
            if header[i] == year:
                col = i
        emissions_data = {}
        for row in reader:
            state = row[0]
            emissions = float(row[col])
            emissions_data[state] = emissions
        sorted_data = {k: v for k, v in sorted(emissions_data.items(), key=lambda x: x[0])}
    return sorted_data

    

#print(get_emissions_by_year('InfrastructureData/LongTermEmissionsData.csv', '2020'))
