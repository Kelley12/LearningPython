#! python3
# excelToCSV.py - Loops through all excel files in a given folder and converts them to CSV.
# If an excel file contains multiple sheets, it creates a CSV for each.

import sys, os, openpyxl, csv

# Get the excel file location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: py excelToCSV.py workingDirectory')
    sys.exit()

excelFileDirectory = sys.argv[1]

for excelFile in os.listdir(excelFileDirectory):
    # Load each excel workbook
    if excelFile.lower().endswith('.xlsx'):
        print("Converting Excel file %s to CSV..." % excelFile)
        fileName = os.path.splitext(excelFile)[0]
        wb = openpyxl.load_workbook(os.path.join(excelFileDirectory, excelFile))
        for sheetName in wb.get_sheet_names():
            sheet = wb.get_sheet_by_name(sheetName)

            # Create CSV file from the sheet
            csvFileName = fileName + '_' + sheetName + '.csv'
            # Create the csv.writer object for this CSV file.
            csvFileObj = open(os.path.join(excelFileDirectory, csvFileName), 'w', newline='')
            csvWriter = csv.writer(csvFileObj)
            print("\tCreating CSV %s..." % csvFileName)

            # Loop through every row in the sheet.
            for rowNum in range(1, sheet.max_row + 1):
                rowData = []    # append each cell to this list
                # Loop through each cell in the row.
                for colNum in range(1, sheet.max_column + 1):
                    # Append each cell's data to rowData.
                    rowData.append(sheet.cell(row=rowNum, column=colNum).value)

                # Write the rowData list to the CSV file.
                csvWriter.writerow(rowData)
            csvFileObj.close()
            
