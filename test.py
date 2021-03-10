# Melissa Ribeiro - Deeper Systems 
# 03/10/2021

import json

#loading data
with open('source_file_2.json') as file:
  dataset = json.load(file)

dataset = sorted(dataset, key=lambda k: k.get('priority', 0), reverse=False)
watchers = {}
managers = {}

#
for data in dataset:
    watcher = data["watchers"]
    for key in watcher:
        watchers.setdefault(key, []).append(data["name"])
    manager = data["managers"]
    for key in manager:
        managers.setdefault(key, []).append(data["name"])

#create files
with open('watchers.json', 'w') as json_file:
  json.dump(watchers, json_file)

with open('managers.json', 'w') as json_file:
  json.dump(managers, json_file)