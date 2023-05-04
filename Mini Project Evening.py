class Airline():
    def __init__(self, id, name, planes):
        self.id = id
        self.name = name
        self.planes = planes
        
        if not isinstance(id, str):
            raise Exception("L'attribut id doit être un string")
        
        if not isinstance(name, str):
            raise Exception("L'attribut name doit être un string")

        if not isinstance(planes, list) and all(isinstance(item, Airplane) for item in Airplane):
            raise Exception("L'attribut planes doit être une liste de type de Airplane")
import random 
class Airplane():
    def __init__(self, id, current_location, company, next_flights):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = next_flights
        
        if not isinstance(id, int):
            raise Exception("L'attribut id doit être un entier")
        
        if not isinstance(current_location, str) and all(isinstance(item, Airport) for item in Airport):
            raise Exception("L'attribut doit être un attribut de type Airplane")  
        
        if not isinstance(company, str) and all(isinstance(item, Airline) for item in Airline):
            raise Exception("L'attribut doit être un objet de type Airline") 
        
        if not isinstance(next_flights, list)and all(isinstance(item, Flight) for item in Flight):
            raise Exception("L'attribut doit être un objet de type Flight") 

    def fly(self, destination):
        print("l'avion vole en destination de",destination)
        
    def location_on_date(self, date):
       emplacement = ["en Allemagne", "en Espagne", "en France", "au TOGO", "au Japon", "en Russie"]
       choix = random.choice(emplacement)
       print(f"Le {date}, l'avion sera {choix}")
       
    def available_on_date(self, date, location):
        disponibilité = [True, False]
        vol = random.choice(disponibilité)
        planning_vol = [2023/5/12, 2023/5/11, 2023/5/5, 2023/5/7]
        if date not in planning_vol and vol == False:
            return True
        else:
            return False
import datetime
class Flight():   
        def __init__(self, date, destination, origin, plane, id):
            self.date = date
            self.destination = destination
            self.origin = origin
            self.plane = plane
            self.id = id
            if  not isinstance(date, datetime.date):
                raise Exception("L'attribut doit être une date")
                
            if not isinstance(destination, str)and all(isinstance(Airport) for item in Airport):
                raise Exception("L'attribut doit être un attribut de type Airport")
            
            if not isinstance(origin, str)and all(isinstance(Airport) for item in Airport):
                raise Exception("L'attribut doit être un attribut de type Airport")
            
            if not isinstance(plane, str)and all(isinstance(Airplane) for item in Airplane):
                raise Exception("L'attribut doit être un attribut de type Airplane")
            
            if not isinstance(id, str):
                raise Exception("L'attribut doit être un attribut de type String")
            

        def take_off(self):
            #MESSAGE ADRESSEE PAR LA TOUR DE COMMANDE A TOUS LES PILOTES EN ACTIVITE DE LA COMPAGNIE
            decoller = input("Veuillez svp renseigner si un avion est en train de décoller(Yes/No):")
            decoller.lower()
            if decoller == "yes":
               print("L'avion est en train de décoller, le Boeing 3 de la ligne 12 est en train de décoller ")
            if decoller == "no":
                print("Aucun appareil n'est en activité")

        def land(self):
            #MESSAGE ADRESSEE PAR LA TOUR DE COMMANDE A TOUS LES PILOTES EN ACTIVITE DE LA COMPAGNIE
            atterrir = input("Veuillez svp renseigner si un avion est en train d'atterir(Yes/No):")
            atterrir.lower()
            if atterrir == "yes":
               print("L'appareil a atteri")
            if atterrir == "no":
                print("L'appareil n'a pas encore atteri")
class Airport():
    def __init__(self, city, planes, scheduled_departures, scheduled_arrivals):
        self.city = city
        self.planes = planes
        self.scheduled_departures = scheduled_departures
        self.scheduled_arrivals = scheduled_arrivals
        
        if not isinstance(city, str):
                raise Exception("L'attribut doit être un attribut de type String")
            
        if not isinstance(planes, list) and all((item, Airplane) for item in Airplane):
                raise Exception("L'attribut doit être un attribut de type Airplane")
            
        if not isinstance(scheduled_departures, list) and all((item, Flight) for item in Flight):
                raise Exception("L'attribut doit être un attribut de type Flight")
            
        if not isinstance(scheduled_arrivals, list) and all((item, Flight) for item in Flight):
                raise Exception("L'attribut doit être un attribut de type Flight")
       
    def schedule_flight(self, destination, datetime):
            #MESSAGE ADRESSE AUX CENTRES D'INFORMATIONS D'AUTRES COMPAGNIES AERONAUTIQUES
            demande = input(f"Y'a t'il un apprareil libre pour un potentiel vol sur {destination} à la date suivante {datetime}?(Yes/No): ")
            demande.lower()
            if demande == "yes":
                vol_prévue = {"depart": "LOME",
                  "arrivée": destination, 
                  "date":  datetime,
                  "heure de départ": random.randrange(0, 23)
                  }
                print(vol_prévue)
            else:
                print("Aucun appareil n'est libre pour effectuer ce voyage")
            
            
    def info(self, start_date, end_date) :
            vol2 = {"depart": "LOME",
                  "arrivée": "GERMANY",
                  "date": 2023/5/6,
                  "heure de départ": "9am",
                }

vol1 = Flight(datetime.date(2023, 1, 1), "PEKIN", "LOME", "Boeing3", "PEKIN,ligne12,2023/5/6")
vol2 = Flight(datetime.date(2023, 1, 2), "TOKYO", "LOME", "Boeing1", "TOKYO,ligne1,2023/5/6")
vol3 = Flight(datetime.date(2023, 1, 3), "DAKAR", "LOME", "Boeing5", "DAKAR,ligne5,2023/5/6")
vol4 = Flight(datetime.date(2023, 1, 4), "ACCRA", "LOME", "Boeing7", "ACCRA,ligne8,2023/5/6")
vol1.take_off()
vol1.land()

appareil1 = Airplane(123,"AIL", "Boeing2", list((vol1, vol2)))
appareil2 = Airplane(124,"AIL", "Boeing8", list((vol3, vol4)))
appareil1.fly("BERLIN")
appareil1.location_on_date(datetime.date(2023, 1, 1))

ligne1 = Airline("122", "Boeing1", list((appareil1, appareil2)))

Aeroport = Airport("TORONTO", list((appareil1, appareil2)), list((vol1,vol2)), list((vol3, vol4)))
Aeroport.schedule_flight("KARA", datetime.date(2023, 1, 5))
Aeroport.schedule_flight("MONTREAL", datetime.date(2023, 1, 9))