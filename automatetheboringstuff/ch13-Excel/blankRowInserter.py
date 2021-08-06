# Ch13 Practice Project - Blank Row Inserter
# Solution by SeungWon Bae

import openpyxl, sys

def quit(message):
    print(message)
    exit(0)

if len(sys.argv) == 4:
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        filename = sys.argv[3]
    except:
        quit("Wrong argument type: please attach two numbers and a Excel filename as command line arguments")
else:
    quit("Insufficient arguments: please attach two numbers and a Excel filename as command line arguments")

print(f'Opening {filename}...')

try:
    wb = openpyxl.load_workbook(filename)
except:
    quit(f"Wrong filename: cannot open '{filename}'")

sheet = wb.active

print(f'Inserting {m} blank rows starting at row {n}...')

if sheet.max_row >= n:
    sheet.insert_rows(n, m)

wb.save(f'blankInserted_{filename}')

print('Done')