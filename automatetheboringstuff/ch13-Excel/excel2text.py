# Ch13 - Practice Project: Spreadsheet to Text Files
# Solution by SeungWon Bae

import openpyxl, sys, os

def quit(message):
    print(message)
    exit(0)

if len(sys.argv) == 2:
    try:
        filename = sys.argv[1]
    except:
        quit("Wrong argument type: please attach an Excel filename as command line argument")
else:
    quit("Insufficient arguments: please attach an Excel filename as command line argument")

print(f'Opening {filename}...')

try:
    wb = openpyxl.load_workbook(filename)
except:
    quit(f"Wrong filename: cannot open '{filename}'")

sheet = wb.active

filename = os.path.splitext(filename)[0]    # remove the extension

for i, column in enumerate(sheet.columns, 1):
    textfile = f'{filename}_{i}.txt'
    print(f'Writing {textfile}...')
    
    with open(textfile, 'w', encoding='utf8') as f:
        for row in column:
            f.write(f'{row.value}\n')
            
print('Done')