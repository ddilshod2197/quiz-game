import random

class Quiz:
    def __init__(self):
        self.sovarlar = {
            "Matematika": {
                "1+1": 2,
                "2*2": 4,
                "5-3": 2
            },
            "Tarix": {
                "Rossiya 1917-yilda qanday voqea bo'ldi?": "Inqilob",
                "Borodin qanday urushda qatnashgan?": "Krim urushi",
                "Qrim urushi qachon bo'lgan?": "1853-1856"
            },
            "Fizika": {
                "Elektronning zaryadiga qanday qiymat berilgan?": "1,6*10^-19",
                "Ko'zga tashlanadigan nurning uzunligiga qanday qiymat berilgan?": "380-780 nm",
                "Ko'zga tashlanadigan nurning uzunligiga qanday qiymat berilgan?": "380-780 nm"
            }
        }

    def o'yinlash(self):
        sozlar = list(self.sovarlar.keys())
        soz = random.choice(sozlar)
        savollar = list(self.sovarlar[soz].keys())
        savol = random.choice(savollar)
        javob = input(f"{soz}: {savol} = ")
        if javob == str(self.sovarlar[soz][savol]):
            print("To'g'ri!")
        else:
            print(f"Xato! To'g'ri javob: {self.sovarlar[soz][savol]}")

    def boshlash(self):
        while True:
            print("1. O'yinlash")
            print("2. Chiqish")
            tanlov = input("Tanlovni tanlang: ")
            if tanlov == "1":
                self.o'yinlash()
            elif tanlov == "2":
                break
            else:
                print("Xato tanlov! Qaytadan urinib ko'ring.")

quiz = Quiz()
quiz.boshlash()
