#          0      1     2    3
osoba= ["Sofija",20,"plava",True]
print(osoba)
print(osoba[0])
print("Godine su:", osoba[1])
kurs= "python"
print(kurs[0])
print(kurs[1])

for x in range(len(kurs)):
    print("na poziciji:",x , kurs[x])
# len(senkvenca prebroji koliko ima članova)

ustanova= "It academy"
for indeks in range(len(ustanova)):
    print(ustanova[indeks])
primer="zadatak1 "
for x in range(len(primer)):
    print(primer[x])

korisnicko_ime= "admin"
uneto_korisnicko_ime =input("Unesi korisnicko ime")
if korisnicko_ime==uneto_korisnicko_ime.lower():
    print("Dobro dosli:")
else:
    print("Pogresni podaci:")
#lower pretvara u mala slova 
#upper pretvara u velika slova
    

    

    

