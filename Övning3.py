#######################################################
# Klasser
class Student:
    def __init__(self, namn, ålder, favoritämne) -> None:
        self.namn = namn
        self.ålder = ålder
        self.favoritämne = favoritämne
        self.kurser = []

    def info(self):
        print(f"{self.namn} är {self.ålder} och har {self.favoritämne} som favoritämne!")

    def lägg_till_kurs(self, kurs):
        self.kurser.append(kurs)

    def hoppa_av_kurs(self, kurs):
        if kurs in self.kurser:
            self.kurser.remove(kurs)
        
        else:
            print(f"Varning!! Studenten går inte kursen:{kurs}")

    def går_kurser(self):
        print(f"{self.namn} går kurserna:")
        for kurs in self.kurser:
            print(f"\t{kurs}")

    def tar_kurs(self, kurs):
        if kurs in self.kurser:
            return True
        else:
            return False


#######################################################
# Stödfunktioner
def studenter_som_tar_kurs(kurs, lista_med_studenter):
    kurs_lista = []

    for student in lista_med_studenter:
        if student.tar_kurs(kurs):
            kurs_lista.append(student)

    return kurs_lista


def lägg_till_kurser(student):
    while True:
        kurs = input("Ange kurs för att lägga till eller 'q' för att avsluta: ")

        if kurs == 'q':
            break

        student.lägg_till_kurs(kurs)

#######################################################
# Main funktion
def main():
    skolans_elever = []

    while True:
        print("1. Skapa en student")
        print("2. Lägg till kurs")
        print("3. Skriv ut information")
        print("4. Skriv ut kurser")
        print("5. Ändra namn på student")
        print("6. Hämta alla som tar samma kurs")
        print("7. Avsluta")
        val = input("Gör ett val: ")

        if val == "1":
            namn = input("Ange elevens namn: ")
            ålder = input("Ange elvens ålder: ")
            favoritämne = input("Ange elvens favoritämne: ")

            ny_student = Student(namn, ålder, favoritämne)

            skolans_elever.append(ny_student)

        elif val == "2":
            student = input("Ange studentens namn: ")
            studenten = None
            
            for s in skolans_elever:
                if s.namn == student:
                    studenten = s

            if studenten != None:
                lägg_till_kurser(studenten)

            else:
                print("Fanns ingen student vid det namnet!")


        elif val == "3":
            for elev in skolans_elever:
                elev.info()
        
        elif val == "4":
            for elev in skolans_elever:
                elev.går_kurser()
        
        elif val == "5":
            gammalt_namn = input("Ange det gamla namnet: ")

            elev = None

            for elev in skolans_elever:
                if elev.namn == gammalt_namn:
                    elev = elev

            if elev != None:
                nya_namnet = input("Ange det nya namnet: ")

                elev.namn = nya_namnet

                print("Eleven har uppdaterats!")

            else: 
                print("Eleven finns inte! Vi går tillbara ")

        elif val == "6":
            kurs = input("Ange kurs:")
            studenter = studenter_som_tar_kurs(kurs, skolans_elever)  

            if not studenter:# <-- if studenter == []:

                print("Finnas inga studenter som tar den kursen!")

            else:
                print(f"Studenter som tar kursen {kurs} är:")
                for student in studenter:
                    print(f"{student.namn}")
                    
        
        elif val == "7":
            break

        else:
            print("Ogiltligt val!")


if __name__ == '__main__':
    main()