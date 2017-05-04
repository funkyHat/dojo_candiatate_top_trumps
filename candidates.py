import csv

file = '/var/tmp/candidates/candidates-all.csv'

def parseCSV(file):
    data = {}
    with open(file, 'r') as f:
        r = csv.DictReader(f)
        for row in r:
            data[row['name']] = row
    return data

def initialise():
    mapping = parseCSV(file)
    honorific_set = set([i['honorific_prefix'].upper() for hv, i in mapping.items()])
    mapping = {}
    for val in honorific_set:
        count = len(val)
        mapping[val] = count
    return mapping

def getScore(title):
    mapping = initialise()
    return mapping[title]


print(getScore('MR'))
