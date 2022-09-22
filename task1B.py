import csv

def trailsAfter2K(filename='Trails.csv'):
    with open(filename) as fn:
        global inputDict
        inputDict = csv.DictReader(fn)
        listOfTrails = []
        for dictItem in inputDict:
            instYear = dictItem['INST_YEAR']
            if not instYear == '':
                if int(instYear) > 2000:
                    listOfTrails.append(dictItem['TRAIL_NAME']) if not dictItem['TRAIL_NAME'] == 'UNKNOWN NAME' else listOfTrails.append(str('trail ID - '+dictItem['TRAIL_ID'])) 
    print("Trails Installed after the year 2000")
    setOfTrails = set(listOfTrails)
    for item in setOfTrails:
        print(item)

trailsAfter2K()