import csv

#Creates (or modifies) a CSV file to only include rows that have 'MRF' in the 'Type' column
def filterMRFdata(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        with open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            header = next(reader)
            writer.writerow(header)
            for row in reader:
                if row[9] == "MRF":
                    writer.writerow(row)
