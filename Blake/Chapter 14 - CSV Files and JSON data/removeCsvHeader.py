#! python3
# removeCsvHeader.py .py - Program that removes the header from all CSV's in the cwd.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every CSV file in the cwd.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file.
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    # Write to the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
