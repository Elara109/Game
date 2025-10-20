import random

kortlek = [
    ("Super Strength",8)
    ("Super Speed", 7)
    ("Elemental Control", 9)
    ("Technopathy", 10)
    ("Intangibility and Invisibility", 8)
    ("Shapeshifting", 8)
    ("Telekinesis", 7)
    ("Deflection", 10)
]
prayer1 = 0
player2 = 0

for runda in range(7):
    print(f"\n Runda {runda+1}")

    kort1 = random.choice(kortlek)
    kort2 = random.choice(kortlek)

    print("spelare 1 drar:", kort1)
    print("spelare 2 drar:", kort2)

    if kort1[1] > kort2[1]:
        print("spelare 1 van rundan! YAYA")
        poäng1 += 1
    elif kort2[1] > kort1[1]:
        print("spelare 2 van!")
        poäng2 += 1
    else:
        print("Oavgjort")
