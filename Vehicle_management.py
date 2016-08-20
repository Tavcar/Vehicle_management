# -*- coding: utf-8 -*-

class Vehicle(object):
    def __init__(self, brand, model, distance, service_date):
        self.brand = brand
        self.model = model
        self.distance = distance
        self.service_date = service_date

def main():
    vozila_file = open("vozila.txt", "r+")
    vozila_list = []

    for vozilo in vozila_file:
        brand, model, distance, service_date = vozilo.split(";")
        vozilo = Vehicle(brand, model, distance, service_date)
        vozila_list.append(vozilo)

    izbira = raw_input("Bi radi:\n a) videli list vseh vozil,\n b) uredili prevožene kilometre/datum servisa ali\n c) dodali novo vozilo?\n (a, b ali c): ")
    print(" ")

    if izbira.lower() == "a":
        izpis_vozil(vozila_list)

    elif izbira.lower() == "b":
        uredi(vozila_list)

    elif izbira.lower() == "c":
        dodaj_vozilo(vozila_list)

    shrani(vozila_list, vozila_file)
    vozila_file.close()


def shrani(vozila_list, vozila_file):
    vozila_file.close()
    vozila_file = open("vozila.txt", "w")
    for vozilo in vozila_list:
        vozila_file.write(vozilo.brand + ";" + vozilo.model + ";" + vozilo.distance + ";" + vozilo.service_date)

def izpis_vozil(vozila_list):
    for vozilo in vozila_list:
        print "Znamka: " + vozilo.brand
        print "Model: " + vozilo.model
        print "Prevoženi km: " + vozilo.distance
        print "Datum servisa: " + vozilo.service_date

def uredi(vozila_list):
     for vozilo in vozila_list:
        print "\n" + vozilo.brand + " " + vozilo.model
        dopisi = raw_input("Želite urediti podatke vozila? (km/datum/oboje/ne): ")

        if dopisi.lower() == "km":
            print "Prevoženi km: " + vozilo.distance
            vozilo.distance = raw_input("Dodajte število prevoženih kilometrov: ")

        elif dopisi.lower() == "datum":
            print "Datum servisa: " + vozilo.service_date
            vozilo.service_date = raw_input("Datum servisa: ")+ "\n"

        elif dopisi.lower() == "oboje":
            print "Prevoženi km: " + vozilo.distance
            vozilo.distance = raw_input("Dodajte število prevoženih kilometrov: ")
            print "Datum servisa: " + vozilo.service_date
            vozilo.service_date = raw_input("Datum servisa: ") + "\n"

def dodaj_vozilo(vozila_list):
    vozilo_brand = raw_input("Dodajte znamko vozila: ")
    vozilo_model = raw_input("Dodajte model vozila: ")
    vozilo_prevozeni_km = raw_input("Dodajte število prevoženih kilometrov: ")
    vozilo_datum_servisa = raw_input("Datum servisa: ")

    vozilo = Vehicle(brand="\n" + vozilo_brand, model=vozilo_model, distance=vozilo_prevozeni_km, service_date=vozilo_datum_servisa)
    vozila_list.append(vozilo)
    print "Vozilo uspešno dodano!"


if __name__ == "__main__":
        main()
        print("Konec")