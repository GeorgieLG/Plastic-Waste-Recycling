import csv

def get_recycling_percentage_by_state(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        recycling_data = {}
        
        for row in reader:
            state = row[0]
            recycling_percentage = int(row[2])
            recycling_data[state] = recycling_percentage
        
        #sorted_data = {k: v for k, v in sorted(recycling_data.items(), key=lambda x: x[0])}
    
    return recycling_data

#print(get_recycling_percentage_by_state('InfrastructureData/RecyclingPercentageByState.csv'))

