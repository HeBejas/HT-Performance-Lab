import json

with open('values.json', 'r') as file:
    valuesJson = json.load(file)
    
valuesData = {}
for item in valuesJson["values"]:
    valuesData[item["id"]] = item["value"]

with open('tests.json', 'r') as file:
    testsData = json.load(file)
    
ids = []

def fill_values(data):
    for test in data:
        if 'id' and 'value' in test:
            test['value'] = valuesData.get(test['id'])
        if 'values' in test:
            fill_values(test['values'])
        
fill_values(testsData['tests'])

with open('report_path.json', 'w') as f:
    json.dump(testsData, f, indent=1)
