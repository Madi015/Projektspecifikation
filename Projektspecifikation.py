import datetime
import json
Madi  = []
David = []
Mia   = []

with open('in_ut.json', 'r') as filereader:
    Data = filereader.read()
    allData = json.loads(Data)
for X_dic in allData:
    if X_dic["namn"] == "Madi":
        print(X_dic)
          