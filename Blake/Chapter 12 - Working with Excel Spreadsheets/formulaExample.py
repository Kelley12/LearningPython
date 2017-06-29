#! python3
# formulaExample.py

import openpyxl

# Write a formula to a spreadsheet
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)'
wb.save('writeFormula.xlsx')
