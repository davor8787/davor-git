osoba=["Sofija",25,"plava",False ]
for indeks in range(len(osoba)):
    print(osoba[indeks])

for osobina in osoba:
    print(osobina)

for indeks, vrednost in enumerate( osoba):
    print("Indeks",indeks, "Stavka",vrednost)
automobili=["opel","citroen","jugo","kia","bmv"]
for pozicija, auto in enumerate(automobili):
    print("pOZICIJA",pozicija,"Auto",auto)
automobili.append("Mwrcedes")
print(automobili)
brojevi=[1,2,3,4,5,6]
brojevi1=[]
brojevi2=[]
for i in range(len(brojevi)):
    if i ==1 or i==2 or i==3:
        brojevi1.append(automobili[i])
brojevi2 = brojevi[1:4]
print(brojevi2)

