# Ülesanne nr.29
# Et küpsised oleks muredad, lisatakse neile küpsetuspulbrit, milles on
# söögisoodat -25%, sidrunhapet -15% ning jahu -60%. Kui palju soodat,
# sidrunhapet ja jahu on vaja et valmistada A gr küpsetuspulbrit?

kogus = float(input("Mitu grammi küpsetuspulbrit soovid valmistada ? "))

while kogus <= 0:
    kogus = float(input("Sisesta 0-st suurem positiivne number."))
    
sooda = kogus * 0.25
sidrunhape = kogus * 0.15
jahu = kogus * 0.60


print("Selleks et et valmistada ", kogus, "grammi küpsetuspulbrit on vaja:")
print(sooda, "grammi soodat,")
print(sidrunhape, "grammi sidrunhapet,")
print(jahu, "grammi jahu.")

    