from datetime import datetime, timedelta
import json
import matplotlib.pyplot as plt
import numpy as np

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
        print(f"bruttol�n                           |                   {self.bruttolon}")
        print(f"Skatt                               |                   {self.skatt}")
        print(f"NettoL�n                            |                   {self.nettolon}")
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
        print("Personen finns inte med i v�r system.")
#TODO maste vara en list som innehaller alla personals arbete.
MadisArbete = timedelta(hours=0, minutes=0, seconds=0)
MiasArbete = timedelta(hours=0, minutes=0, seconds=0)
DavidsArbete = timedelta(hours=0, minutes=0, seconds=0)
for tid in Madi:
    MadisArbete += tid
Timmar = MadisArbete.total_seconds() //3600                      # har raknar jag antal timmar
MinuterIProcent = (MadisArbete.total_seconds()%3600)/3600        #har tar jag resten som ar kvar och rakna det i procent.
summaForMadi = Timmar+MinuterIProcent
for tid in Mia:
    MiasArbete += tid
Timmar = MiasArbete.total_seconds() //3600                      # har raknar jag antal timmar
MinuterIProcent = (MiasArbete.total_seconds()%3600)/3600        #har tar jag resten som ar kvar och rakna det i procent.
summaForMia = Timmar+MinuterIProcent
for tid in David:
    DavidsArbete += tid
Timmar = DavidsArbete.total_seconds() //3600                      # har raknar jag antal timmar
MinuterIProcent = (DavidsArbete.total_seconds()%3600)/3600        #har tar jag resten som ar kvar och rakna det i procent.
summaForDavid = Timmar+MinuterIProcent
MADI = person(summaForMadi)
MADI.bruttolon = MADI.bruttoLonBerakning()
MADI.skatt     = MADI.skattberakning()
MADI.nettolon = MADI.NettoLonBerakning()
MADI.semester = MADI.Semester()
MIA = person(summaForMia)
MIA.bruttolon = MIA.bruttoLonBerakning()
MIA.skatt     = MIA.skattberakning()
MIA.nettolon = MIA.NettoLonBerakning()
MIA.semester = MIA.Semester()
DAVID = person(summaForDavid)
DAVID.bruttolon = DAVID.bruttoLonBerakning()
DAVID.skatt     = DAVID.skattberakning()
DAVID.nettolon = DAVID.NettoLonBerakning()
DAVID.semester = DAVID.Semester()

# figuren
persons = ['Madi', 'David', 'Mia']
netto_lon = [MADI.nettolon, DAVID.nettolon, MIA.nettolon]
Skatten = [MADI.skatt, DAVID.skatt, MIA.skatt]
Smester = [MADI.semester, DAVID.semester, MIA.semester]
fig, ax = plt.subplots()
bar_width = 0.2

bar_positions_salary = np.arange(len(persons)) - bar_width
bar_positions_tax = np.arange(len(persons))
bar_positions_holiday = np.arange(len(persons)) + bar_width

ax.bar(bar_positions_salary, netto_lon, bar_width, label='Netto l�n', color='blue')
ax.bar(bar_positions_tax, Skatten, bar_width, label='Skatt', color='red')
ax.bar(bar_positions_holiday, Smester, bar_width, label='Semester ers�ttning', color='green')

ax.set_xlabel('Namn f�r varje anst�ld')
ax.set_ylabel('Kronor')
ax.set_title('Figuren j�mf�r inkomster f�r tre anst�lda')

ax.set_xticks(np.arange(len(persons)))
ax.set_xticklabels(persons)

ax.legend()

kommand = True
print('Detta program läser av in- och utceckningar för tre anstälda och \noch räknar ut lön spec och kan jämför olika inkomster. ')
print('skriv help för help')
while kommand != 'quit':
    kommand = input('skriv ett kommand:')
    if kommand == 'help':
            print('lön:            för att skriva ut lön spes för en person')
            print('inkomster:      för att se figuren')
            print('quit:           för att stänga av programmet.')
    elif kommand == 'lön':
        person = input('skriv namnet: ')
        if person == 'Madi':
            print(f'lönespecifikation för {person} är : ')
            MADI.__repr__()
        elif person == 'Mia':
            print(f'lönespecifikation för {person} är : ')
            MIA.__repr__()
        elif person == 'David':
            print(f'lönespecifikation för {person} är : ')
            DAVID.__repr__()
        else:
            print(f'Vi har ingen anställd som heter {person}')
    elif kommand == 'inkomster':
        plt.show()