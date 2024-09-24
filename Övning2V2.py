###########################################################
#------------------------ Klasser ------------------------#
###########################################################

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

###########################################################
#--------------------- Funktioner ------------------------#
###########################################################

def skriv_ut_info(lista_med_studenter):
    for student in lista_med_studenter:
        student.info()

def skriv_ut_kurser(lista_med_studenter):
    for student in lista_med_studenter:
        student.går_kurs()

def skapa_student():
    namn = input("Ange studentens namn: ")
    ålder = input("Ange studentens ålder: ")
    if not ålder.isdigit():
        print("Ogiltlig ålder!")
        return None
    
    favoritämne = input("Ange studentens favoritämne: ")
    kurs = input("Ange studentens kurs: ")

    return Student(namn, ålder, favoritämne, kurs)


def hämta_student(namn, lista_med_studenter):
    for student in lista_med_studenter:
        if student.namn == namn:
            return student
    else:
        return None

def ändra_namn(student, nytt_namn):
    student.namn = nytt_namn


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
            ny_student = skapa_student()
            if ny_student != None:
                skolans_elever.append(ny_student)
            else:
                print("Det gick inte att skapa en student!")

        elif val == "2":
            skriv_ut_info(skolans_elever)
        
        elif val == "3":
            skriv_ut_kurser(skolans_elever)
        
        elif val == "4":
            gammalt_namn = input("Ange det gamla namnet: ")
            student = hämta_student(gammalt_namn, skolans_elever)
            if student != None:
                nytt_namn = input("Ange nytt namn: ")
                ändra_namn(student, nytt_namn)
                print("Eleven har uppdaterats!")

            else:
                print("Eleven finns inte! Vi går tillbara ")
        
        elif val == "5":
            break

        else:
            print("Ogiltligt val!")


###########################################################
#--------------------- Entrypoint ------------------------#
###########################################################

if __name__ == '__main__':
    main()