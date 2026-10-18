import random

summa = 0

lukumaara = int(input("Montako arpakuutiota heitetään? "))

for i in range(lukumaara):
    silmaluku = random.randint(1, 6)
    summa = summa + silmaluku

print("Silmälukujen summa on", summa)