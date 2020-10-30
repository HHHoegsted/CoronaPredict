import csv, os, json
from datetime import datetime

subdirs = [x[0] for x in os.walk('./data/')]
subdirs = subdirs[1:]

arrayresult = []
for dir in subdirs:
    filename = str(dir)+'/Cases_by_age.csv'

    array = []
    with open(filename) as csvfile:
        filereader = csv.reader(csvfile, delimiter=';')
        next(filereader)
        for row in filereader:
            array.append(row)

    array = array[:-1]

    totalcases = 0
    for item in array:
        totalcases += int(str(item[1]).replace('.', ''))
    date = dir[7:]
    arrayresult.append([date, totalcases])

for array in arrayresult:
    array[0] = (datetime.strptime(array[0], '%d%m%Y'))

arrayresult = sorted(arrayresult)
for array in arrayresult:
    array[0] = array[0].strftime('%d-%m-%Y')

print(json.dumps(arrayresult, sort_keys=True, indent=4))