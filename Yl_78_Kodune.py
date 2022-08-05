#Ülesanne nr.78
#Halli kanga A meetrit maksab B eurot ja
#sinise kanga K meetrit maksab M eurot.
#Kumb kangas on kallim ja kui palju?

halliKangaMeetriHind = float(input("Sisesta halli kanga meetri hind: "))

while halliKangaMeetriHind <= 0:
    halliKangaMeetriHind = float(input("Sisesta 0-st suurem positiivne arv: "))
    
siniseKangaMeetriHind = float(input("Sisesta sinise kanga meetri hind: "))

while siniseKangaMeetriHind <= 0:
    siniseKangaMeetriHind = float(input("Sisesta 0-st suurem positiivne arv: "))

halliKangaKogus = float(input("Sisesta mitu meetrit halli kangast soovid: "))

while halliKangaKogus <= 0:
    halliKangaKogus = float(input("Sisesta 0-st suurem positiivne arv: "))
    
siniseKangaKogus = float(input("Sisesta mitu meetrit sinist kangast soovid: "))

while siniseKangaKogus <= 0:
    siniseKangaKogus = float(input("Sisesta 0-st suurem positiivne arv: "))
    
halliKangaLoppHind = halliKangaMeetriHind * halliKangaKogus
siniseKangaLoppHind = siniseKangaMeetriHind * siniseKangaKogus

print(halliKangaKogus, "meetrit halli kangast maksab", halliKangaLoppHind, " eurot.")
print(siniseKangaKogus, "meetrit sinist kangast maksab", siniseKangaLoppHind, " eurot.")

if halliKangaLoppHind > siniseKangaLoppHind:
    vahe = halliKangaLoppHind - siniseKangaLoppHind
    print("Hall kangas on ", vahe, " eurot kallim.")
elif siniseKangaLoppHind > halliKangaLoppHind:
    vahe = siniseKangaLoppHind - halliKangaLoppHind
    print("Sinine kangas on ", vahe, " eurot kallim.")
else:
    print("Halli ja sinise kanga hind on võrdne.")
