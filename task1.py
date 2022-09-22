import csv

def classifyByConditions(filename='Trails.csv'):
    with open(filename) as fn:
        global inputDict
        inputDict = csv.DictReader(fn)
        conditionsDict = dict()
        for dictItem in inputDict:
            conditionStr = dictItem['CONDITION']
            trailStr = dictItem['TRAIL_NAME']
            if dictItem['CONDITION'] not in conditionsDict:
                conditionsDict[conditionStr] = []
            else:
                conditionsDict[conditionStr].append(trailStr)
        for dictItem in conditionsDict:
            print("Trails in ", dictItem,"Condition: \n")
            print(conditionsDict[dictItem])
classifyByConditions()