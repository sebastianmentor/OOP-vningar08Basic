import os
class Receptbok:
    def __init__(self) -> None:
        self.receptindex = {}


    def lägg_till_recept(self, receptnamn, recept):
        if self.finns_recept(receptnamn):
            print("Ett recept finns redan!")
            uppdatera = input("Vill du uppdatera receptet? (y/n): ")
            if uppdatera == "y":
                self.receptindex[receptnamn] = recept
                return
            
            print("Ingen uppdatering sker!")
        
        else:
            self.receptindex[receptnamn] = recept


    def finns_recept(self, receptnamn):
        if receptnamn in self.receptindex:
            return True
        else:
            return False

    def skriv_ut_recept(self, receptnamn):
        if self.finns_recept(receptnamn):
            print(receptnamn + ':')
            print(self.receptindex[receptnamn])


    def spara_recept(self, receptnamn, filnamn):
        if self.finns_recept(receptnamn):
            with open(filnamn, 'a', encoding="utf-8") as f:
                f.write(f"{receptnamn}:{self.receptindex[receptnamn]}\n")


    def spara_receptbok(self, filnamn):
        with open(filnamn, 'a', encoding='utf-8') as f:
            for namn, recept in self.receptindex.items():
                f.write(f"{namn}:{recept}\n")

    # Extra övning
    def läs_in_recept(self, filnamn):
        if not os.path.exists(filnamn):
            return 
        
        recepten = []
        with open(filnamn, 'r', encoding='utf-8') as f:
            for rad in f:
                recepten.append(rad.strip())

        if recepten:
            for recept in recepten:
                namn, receptet = recept.split(":")

                if self.finns_recept(namn):
                    with open("loggade_recept.txt", 'a', encoding="utf-8") as f:
                        f.write(f"{namn}:{receptet}\n")
                else:
                    self.lägg_till_recept(namn, receptet)


if __name__ == "__main__":
    receptbok = Receptbok()
    while True:
        print("1. Skapa ett recept")
        print("2. Kolla om recept finns")
        print("3. Skriv ut recept")
        print("4. Spara receptet")
        print("5. Skapa receptbok")
        print("6. Läs in recept")
        print("7. Avsluta")
        val = input("Gör ett val: ")

        if val == '1':
            recept_namn = input("Ange namnet på receptet: ")
            receptet = input("Skriv receptet: ")
            receptbok.lägg_till_recept(recept_namn, receptet)
            print("Ett recept är skapat och lades till i receptboken!")

        elif val == '2':
            namn = input("Ange receptnamn: ")
            if receptbok.finns_recept(namn):
                print("Receptet fanns!")
            else:
                print("Receptet fanns inte!")
        
        elif val == '3':
            namn = input("Ange receptnamn:")
            receptbok.skriv_ut_recept(namn)

        elif val == '4':
            namn = input("Ange receptnamn:")
            fil_namn = input("Ange filnamn: ")
            receptbok.spara_recept(namn, fil_namn)
            
        elif val == '5':
            fil_namn = input("Ange filnamnet för boken: ")
            receptbok.spara_receptbok(fil_namn)
        
        elif val == '6':
            fil_namn = input("Ange filnamn för inläsning: ")
            if not os.path.exists(fil_namn):
                print("Finns ingen fil att läsa från!")
            else:
                receptbok.läs_in_recept(fil_namn)

        elif val == '7':
            break

        else:
            print("Ogiltligt val!")
            for key, val in receptbok.receptindex.items():
                print(f"{key} | {val}")