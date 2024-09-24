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


student1 = Student('Kalle', 22, 'Matematik', 'Kalkyl 1')
student2 = Student('Anna', 36, 'Filosofi', 'Engelska 7')

student1.info()
student2.info()

student1.går_kurs()
student2.går_kurs()