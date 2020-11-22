import json

# read file
with open('FrontDoorLight.json', 'r') as jsonfile:
    myjson = jsonfile.read()

# parse file
mydata = json.loads(myjson)

# Prints the entire JSON
print(mydata)

# Prints the node "FrontDoorLight"
print(mydata['FrontDoorLight'])

# Prints the node "FrontDoorLight" --> "On"
print(mydata['FrontDoorLight']['on'])

