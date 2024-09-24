class Student:
    def __init__(self, namn, ålder, favoritämne, kurs) -> None:
        self.namn = namn
        self.ålder = ålder
        self.favoritämne = favoritämne
        self.kurs = kurs

    def info(self):
        print(f"{self.namn} är {self.ålder} och har {self.favoritämne} som favoritämne!")

    def går_kurs(self):
        print(f"{self.namn} går kursen {self.kurs}.")


def main():
    skolans_elever = []

    while True:
        print("1. Skapa en student")
        print("2. Skriv ut information")
        print("3. Skriv ut kurser")
        print("4. Ändra namn på student")
        print("5. Avsluta")
        val = input("Gör ett val: ")

        if val == "1":
            namn = input("Ange elevens namn: ")
            ålder = input("Ange elvens ålder: ")
            favoritämne = input("Ange elvens favoritämne: ")
            kurs = input("Ange elevens kurs: ")

            ny_student = Student(namn, ålder, favoritämne, kurs)

            skolans_elever.append(ny_student)

        elif val == "2":
            for elev in skolans_elever:
                elev.info()
        
        elif val == "3":
            for elev in skolans_elever:
                elev.går_kurs()
        
        elif val == "4":
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
        
        elif val == "5":
            break

        else:
            print("Ogiltligt val!")


if __name__ == '__main__':
    main()