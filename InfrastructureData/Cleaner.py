import csv

#Simple script to remove duplicate rows from a CSV file
def removeDuplicateRows(input_file, output_file):
    seen = set()
    with open(input_file, 'r', newline='') as infile:
        with open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            for row in reader:
                row_tuple = tuple(row)  # Convert list to tuple for immutability
                if row_tuple not in seen:
                    seen.add(row_tuple)
                    writer.writerow(row)

#Parses address data and adds a column for the state
def getState(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        with open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ['State']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                address = row.get('Address', '')
                addressList = address.split(',')
                length = len(addressList)
                state = addressList[length - 2]
                state = state.strip() #Removes whitespace
                state = state[0:2].upper() #Gets only first 2 characters to eliminate typos
                row['State'] = state
                writer.writerow(row)


#removeDuplicateRows('InfrastructureData/InfrastructureData.csv', 'InfrastructureData/InfrastructureData_cleaned.csv')
#getState('InfrastructureData/InfrastructureData.csv', 'InfrastructureData/InfrastructureData_cleaned.csv')
