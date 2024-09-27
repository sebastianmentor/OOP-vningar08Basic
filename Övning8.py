import os
import time
class Shoppingkorg:

    def __init__(self, max_kapacitet) -> None:
        self.max_kapacitet = max_kapacitet
        self.varukorg = []


    def lägg_till_vara(self, namn, vikt, pris):
        """Returnerar True om varan lades till, annars False"""
        if type(vikt) != float or type(pris) not in [float, int]:
            return False
        
        vara = {"namn":namn,
                "vikt":vikt,
                "pris":pris}
        
        self.varukorg.append(vara)
        return True
    

    def summera_varukorg(self):
        summa = 0.0
        for vara in self.varukorg:
            summa += vara['pris']
        return round(summa, ndigits=2)
    

    def ta_bort_vara(self, namn):
        index_att_ta_bort = []
        for index, vara in enumerate(self.varukorg):
            if vara['namn'] == namn:
                index_att_ta_bort.append(index)

        if not index_att_ta_bort:
            print(f"Finns inga {namn} i varukorgen!")
            return None

        self.varukorg.pop(index_att_ta_bort[0])
        print(f"En {namn} togs bort ur varukorgen")

        x_antal = len(index_att_ta_bort[1:])
        if x_antal > 0:
            # print(f"Det finns {x_antal} många av {namn} kvar i varukorgen!")
            print(f"Det finns {x_antal} {namn} kvar i varukorgen!")


    def töm_varukorg(self):
        self.varukorg.clear()

    
    def skriv_ut_varukorg(self):
        print(f"_________________________________")
        print(f"Namn            |Vikt    |Pris   ")
        for vara in self.varukorg:
            s = f"{vara['namn']:<15}|{vara['vikt']:<8}|{vara['pris']:<8}"
            print(s)


def rensa_skärm():
    if os.name == "nt":
        os.system("cls")

    elif os.name == "posix":
        os.system("clear")

def print_header():
    print(f"_________________________________")
    print(f"*********************************")
    print(f"*         Lindas Handel         *")
    print(f"*********************************")
    print(f"‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def print_produkter(produkter):
    print(f"_________________________________")
    print(f"*********************************")
    print(f"*           Produkter           *")
    print(f"*********************************")
    print(f"ID|Namn            |Vikt    |Pris")
    print(f"‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    for id, vara in produkter.items():
        s = f"{id:<2}|{vara['namn']:<15}|{vara['vikt']:<8}|{vara['pris']:<8}"
        print(s)

def print_hej_då(speed):
    print_header()
    hej_då = f""+\
    f"Vi på Lindas handel tackar dig \n"+\
    f"för att du tog dig tid att shoppa\n"+\
    f"hos oss och hoppas se dig snart\n"+\
    f"igen! Ha en trevlig fortsättning."

    for char in hej_då:
        print(char, end='', flush=True)
        time.sleep(speed)

    time.sleep(2)
    rensa_skärm()

def main(produkter_med_emoji):
    varukorg = Shoppingkorg(30)

    while True:
        rensa_skärm()
        print_header()
        print("1. Lägg till vara")
        print("2. Summera varukorg")
        print("3. Ta bort vara")
        print("4. Töm varukorg")
        print("5. Visa varukorg")
        print("6. Visa produkter")
        print("7. Avsluta")
        val = input("Välj ett alternativ: ")
        if val == "1":
            produkt_id = input("Ange produktid: ")
            if produkt_id in produkter_med_emoji:
                namn = produkter_med_emoji[produkt_id]['namn']
                vikt = produkter_med_emoji[produkt_id]['vikt']
                pris = produkter_med_emoji[produkt_id]['pris']
                varukorg.lägg_till_vara(namn, vikt, pris)
                # Advanced
                # produkt = produkter_med_emoji[produkt_id]
                # varukorg.lägg_till_vara(**produkt) 
                print(f"{namn} lades till i varukorgen")
                time.sleep(2)

        elif val == "2":
            rensa_skärm()
            varukorg.skriv_ut_varukorg()
            print(f"Total summa: {varukorg.summera_varukorg()}")
            input("Tryck enter för att gå tillbaka!")
            

        elif val == "3":
            produkt_id = input("Ange produktid att ta bort: ")
            if produkt_id in produkter_med_emoji:
                varukorg.ta_bort_vara(produkter_med_emoji[produkt_id]["namn"])
            else:
                print("Ogiltligt produktid")

            input("Tryck enter för att gå tillbaka!")    


        elif val == "4":
            rensa_skärm()
            töm_varukorg = input("Är du säker på att du vill tömma varukorgen?(y/n): ")
            if töm_varukorg == 'y':
                varukorg.töm_varukorg()
            else:
                input("Bra val! Fortsätt handla genom att trycka enter!!")


        elif val == "5":
            rensa_skärm()
            varukorg.skriv_ut_varukorg()
            input("Tryck enter för att gå tillbaka!")


        elif val == "6":
            rensa_skärm()
            print_produkter(produkter_med_emoji)
            input("Tryck enter för att gå tillbaka!")


        elif val == "7":
            rensa_skärm()
            print_hej_då(0.05)
            break
            
        else:
            rensa_skärm()
            print("Ogiltligt alternativ!!")
            input("Tryck enter för att gå tillbaka!")



if __name__ == "__main__":
    produkter_med_emoji = {
    "1": {"namn": "Brödlimpa 🥖", "vikt": 0.5, "pris": 19.90},
    "2": {"namn": "Smör 🧈", "vikt": 0.4, "pris": 45.0},
    "3": {"namn": "Ost 🧀", "vikt": 0.3, "pris": 60.0},
    "4": {"namn": "Mjölk 🥛", "vikt": 1.0, "pris": 12.90},
    "5": {"namn": "Ägg 🥚", "vikt": 0.6, "pris": 24.90},
    "6": {"namn": "Kaffe ☕", "vikt": 0.25, "pris": 89.0},
    "7": {"namn": "Socker 🍬", "vikt": 1.0, "pris": 29.90},
    "8": {"namn": "Pasta 🍝", "vikt": 0.5, "pris": 19.90},
    "9": {"namn": "Kiwi  🥝", "vikt": 0.2, "pris": 9.90},
    "10": {"namn": "Bananer 🍌", "vikt": 1.2, "pris": 19.90},
    "11": {"namn": "Tomater 🍅", "vikt": 0.5, "pris": 29.90},
    "12": {"namn": "Kycklingfilé 🍗", "vikt": 1.0, "pris": 99.0},
    "13": {"namn": "Fläskkotlett 🍖", "vikt": 0.8, "pris": 79.0},
    "14": {"namn": "Potatis 🥔", "vikt": 2.0, "pris": 39.90},
    "15": {"namn": "Äpplen 🍏", "vikt": 1.0, "pris": 29.90},
    "16": {"namn": "Yoghurt 🍶", "vikt": 1.0, "pris": 25.0},
    "17": {"namn": "Honung 🍯", "vikt": 0.35, "pris": 59.90},
    "18": {"namn": "Knäckebröd 🍞", "vikt": 0.5, "pris": 25.90},
    "19": {"namn": "Jordgubbar 🍓", "vikt": 0.4, "pris": 49.90},
    "20": {"namn": "Choklad 🍫", "vikt": 0.2, "pris": 22.90},
    }

    # Starta programmet!!
    main(produkter_med_emoji)