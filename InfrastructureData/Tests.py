import csv

states = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
    "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
    "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
    "WV", "WY", "DC", "AS", "GU", "PR", "VI"]
#Checks to make sure that states were properly parsed from the address data
def checkStates(input_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        next(reader) # Skip header row
        
        states = states.copy()
        
        for row in reader:
            upperState = row[11].upper()
            if(upperState not in states):
                print("State not found in the list of valid states. Entry: " + str(row[11]) + " Row #: " + str(reader.line_num))
                return -1
        
    return 1

def findUnlistedStates(input_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip header row
        
        retList = states.copy()

        for row in reader:
            upperState = row[11].upper()
            if upperState in states:
                if upperState in retList:
                    retList.remove(upperState)
        
        return retList

#checkStates('InfrastructureData/InfrastructureData_cleaned.csv')
#print(findUnlistedStates('InfrastructureData/InfrastructureData_cleaned.csv'))