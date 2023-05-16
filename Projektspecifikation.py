from datetime import datetime, timedelta
import json
Madi  = []
David = []
Mia   = []

with open('in_ut.json', 'r') as filereader:
    Data = filereader.read()
    allData = json.loads(Data)
for X_dic in allData:
    if X_dic["namn"] == "Madi":
        inTime = datetime.strptime(X_dic["incheckning"], '%Y-%m-%dT%H:%M:%S')
        utTime = datetime.strptime(X_dic["utcheckning"], '%Y-%m-%dT%H:%M:%S')
        # Rakna ut antal timmar
        diffTime = timedelta(hours=(utTime.hour - inTime.hour), minutes=(utTime.minute - inTime.minute), seconds=(utTime.second - inTime.second))
        # addera till en list som tillhor samma person 
        Madi.append(diffTime)
    elif X_dic["namn"] == "David":
        inTime = datetime.strptime(X_dic["incheckning"], '%Y-%m-%dT%H:%M:%S')
        utTime = datetime.strptime(X_dic["utcheckning"], '%Y-%m-%dT%H:%M:%S')
        diffTime = timedelta(hours=(utTime.hour - inTime.hour), minutes=(utTime.minute - inTime.minute), seconds=(utTime.second - inTime.second))
        David.append(diffTime)
    elif X_dic["namn"] == "Mia":
        inTime = datetime.strptime(X_dic["incheckning"], '%Y-%m-%dT%H:%M:%S')
        utTime = datetime.strptime(X_dic["utcheckning"], '%Y-%m-%dT%H:%M:%S')
        diffTime = timedelta(hours=(utTime.hour - inTime.hour), minutes=(utTime.minute - inTime.minute), seconds=(utTime.second - inTime.second))
        Mia.append(diffTime)
    else:
        print("Personen finns inte med i vår system.")
