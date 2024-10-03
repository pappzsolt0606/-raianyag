diaknev = int(input("hány diákot szeretnél hozzáadni?"))
# diakjegy = int(input("1","2","3","4","5"))
#except:
#    print("rossz az input")

diak = []
jegyek = []

for i in range(diaknev):
    nev = (input("Kérek egy nevet"))
    jegy = int(input("Kérek egy jegyet"))
    diak.append((nev,jegy))

kerdezo = input("Szeretnéd látni az összes diákot? (igen/nem):  ")
if kerdezo == "igen":
    for x,y in diak:
        print(x,y)
        
for a in diak:
    jegyek.append(a[1])
    
atlag = sum(jegyek)/len(jegyek)
atlagkerdezo = input("Szeretnéd tudni az átlagos jegyet? (igen/nem):  ")
if atlagkerdezo == "igen":
        print(atlag)

legkerdezo = input("Szeretnéd tudni a legmagasabb és legalacsonyabb jegyet? (igen/nem):  ")
if legkerdezo == "igen":
        print(f"nagy: {max(jegyek)} kicsi: {min(jegyek)}")
    
diaktavolito = input("Szeretnél eltávolítani egy diákot? (igen/nem):  ")
if diaktavolito == "igen":
    torlendo = input("Kérek egy diákot")
    db = 0
    for t in diak:
        if torlendo.lower() == t[0].lower():
            diak.pop(db)
    db = db+1
print(diak)