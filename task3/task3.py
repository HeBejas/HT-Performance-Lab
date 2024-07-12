import json
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Неверное количество аргументов')
    else:
        valuesInput = sys.argv[1]
        testsInput = sys.argv[2]
        reportInput = sys.argv[3]
        
with open(valuesInput, 'r') as file:
    valuesJson = json.load(file)
    
valuesData = {}
for item in valuesJson["values"]:
    valuesData[item["id"]] = item["value"]

with open(testsInput, 'r') as file:
    testsData = json.load(file)
    
ids = []

def fill_values(data):
    for test in data:
        if 'id' and 'value' in test:
            test['value'] = valuesData.get(test['id'])
        if 'values' in test:
            fill_values(test['values'])
        
fill_values(testsData['tests'])

with open(reportInput, 'w') as f:
    json.dump(testsData, f, indent=1)
