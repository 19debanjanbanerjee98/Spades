import json
from random import randint, uniform

def parse_json(address):
    with open(address) as data_file:    
        data = json.load(data_file)
    return data

# address = str(input('Enter Address: '))
address = 'hydraulic-fluid.json'
schema = parse_json(address)

properties = schema['properties']
no_of_properties = len(properties)

dataset_titles = []
dataset_type = []
dataset_values = ["Poor", "Fair", "Good", "Excellent"]
dataset_max = []
dataset_min = []
probability_weightage = []

for i in list(properties.keys()):
    dataset_titles.append(i)
    dataset_type.append(properties[i]['type'])
    
    if properties[i]['type'] == 'string':
        dataset_max.append(None)
        dataset_min.append(None)
    elif properties[i]['type'] == 'number':
        dataset_max.append(float(properties[i]['maximum']))
        dataset_min.append(float(properties[i]['minimum']))
    else:
        dataset_max.append(int(properties[i]['maximum']))
        dataset_min.append(int(properties[i]['minimum']))
        

n = len(dataset_titles)
l = 50 #no. of fluids to be generated
f = open('outpu.csv', 'w')
f.write("sl. no.")
for i in range(n):
    f.write(","+dataset_titles[i])
for i in range(l):
    f.write('\n')
    f.write(str(i+1));
    for j in range(n):
        if dataset_type[j] == 'number' or dataset_type[j] == 'integer':
            f.write(",")
            f.write(str(randint(dataset_min[j], dataset_max[j])))
        elif dataset_type[j] == 'string':
            f.write(",")
            f.write(dataset_values[randint(0, len(dataset_values) - 1)])
f.close()