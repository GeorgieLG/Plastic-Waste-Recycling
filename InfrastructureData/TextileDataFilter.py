import csv

def filterTextileData(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        with open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            header = next(reader)
            writer.writerow(header)
            for row in reader:
                if row[9] == "Textiles Recycling Facility":
                    writer.writerow(row)


#filterTextileData('InfrastructureData/InfrastructureData_cleaned.csv', 'InfrastructureData/TextileData.csv')
