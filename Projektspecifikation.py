from datetime import datetime, timedelta
import json
#TODO Maste vara en dynamisk. alltsa programmet ska kunna skapa en till peron ifall finns mer folk i json fil.
Madi  = []
David = []
Mia   = []

class person:
    def __init__(self, arbetstid, skatt = 0, semseter = 0, bruttolon = 0, timmlon= 150, nettolon = 0 ):
        self.arbetstid = arbetstid
        self.skatt = skatt
        self.semester = semseter
        self.bruttolon = bruttolon
        self.timmlon = timmlon
        self.nettolon = nettolon
    def bruttoLonBerakning(self):
        self.bruttolon = self.arbetstid * self.timmlon
        return self.bruttolon
    def skattberakning(self):
        self.skatt = self.bruttolon * 0.30
        return self.skatt
    def NettoLonBerakning(self):
        self.nettolon = self.bruttolon - self.skatt
        return self.nettolon
    def Semester(self):
        self.semester = self.bruttolon * 0.12
        return self.semester
    def __repr__(self):
        print("------------------------------------------------------------------------")
        print(f"Arbetstimmar                        |                   {self.arbetstid}")
        print(f"bruttolön                           |                   {self.bruttolon}")
        print(f"Skatt                               |                   {self.skatt}")
        print(f"NettoLön                            |                   {self.nettolon}")
        print(f"Sparad semseter                     |                   {self.semester}")
        print(f"                                    |                                   ")
        print("------------------------------------------------------------------------")
        print(f"Att betala                          |                   {self.nettolon}")
        print("------------------------------------------------------------------------") 

with open('in_ut.json', 'r') as filereader:
    Data = filereader.read()    #read the file
    allData = json.loads(Data)  #convert to json
for X_dic in allData:
    if X_dic["namn"] == "Madi":     # valja en person
        inTime = datetime.strptime(X_dic["incheckning"], '%Y-%m-%dT%H:%M:%S')
        utTime = datetime.strptime(X_dic["utcheckning"], '%Y-%m-%dT%H:%M:%S')
        # Rakna ut antal timmar
        #TODO skapa en metod har.
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
#TODO maste vara en list som innehaller alla personals arbete.
MadisArbete = timedelta(hours=0, minutes=0, seconds=0)
MiasArbete = timedelta(hours=0, minutes=0, seconds=0)
DavidsArbete = timedelta(hours=0, minutes=0, seconds=0)
for tid in Madi:
    MadisArbete += tid
Timmar = MadisArbete.total_seconds() //3600                      # har raknar jag antal timmar
MinuterIProcent = (MadisArbete.total_seconds()%3600)/3600        #har tar jag resten som ar kvar och rakna det i procent.
summaForMadi = Timmar+MinuterIProcent
print(summaForMadi)
for tid in Mia:
    MiasArbete += tid
Timmar = MiasArbete.total_seconds() //3600                      # har raknar jag antal timmar
MinuterIProcent = (MiasArbete.total_seconds()%3600)/3600        #har tar jag resten som ar kvar och rakna det i procent.
summaForMia = Timmar+MinuterIProcent
print(summaForMia)
for tid in David:
    DavidsArbete += tid
Timmar = DavidsArbete.total_seconds() //3600                      # har raknar jag antal timmar
MinuterIProcent = (DavidsArbete.total_seconds()%3600)/3600        #har tar jag resten som ar kvar och rakna det i procent.
summaForDavid = Timmar+MinuterIProcent
print(summaForDavid)
MADI = person(summaForMadi)
MADI.bruttolon = MADI.bruttoLonBerakning()
MADI.skatt     = MADI.skattberakning()
MADI.nettolon = MADI.NettoLonBerakning()
MADI.semester = MADI.Semester()
MADI.__repr__()
MIA = person(summaForMia)
MIA.bruttolon = MIA.bruttoLonBerakning()
MIA.skatt     = MIA.skattberakning()
MIA.nettolon = MIA.NettoLonBerakning()
MIA.semester = MIA.Semester()
MIA.__repr__()
DAVID = person(summaForDavid)
DAVID.bruttolon = DAVID.bruttoLonBerakning()
DAVID.skatt     = DAVID.skattberakning()
DAVID.nettolon = DAVID.NettoLonBerakning()
DAVID.semester = DAVID.Semester()
DAVID.__repr__()