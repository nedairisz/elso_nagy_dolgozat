"""
A stadionok.txt forrásállomány, Forma-1-es verseny pilótáinak adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használd!
A stadionok.txt állomány szerkezete:
•	a stadion neve: Pl.: Metropolitan Park
•	a stadion helyszínének városa: Pl.: New York
•	a stadionnak hányas csapata: Pl.: 1
•	mikor léptek előszőr pályára: pl.: 1984-05-13
•	mikor léptek utoljára pályára: pl.: 1985-08-23
                
d)	Olvasd be a stadionok.txt fájlból az a stadionok adatait és tárolja el megfelelő nevű listákban! 
    Ügyelj arra, hogy az állományok első sora az adatok fejlécét tartalmazza! (10 pont)
e)	Írasd ki a csapatok darabszámát a konzolra!(1p)
f)	Határozd meg és írd ki a minta szerint, hogy mely csapatok találhatók New York-ban! 
    A kiírásban a stadion neve és a csapatok száma szerepeljen (5p)
"""
from Stadion import Stadion

def beolvas():
    fajl=open("stadionok.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close()

    lista=[]
    for i in range(0,len(nyers_lista), 1):
        sorok=nyers_lista[i]
        sor_tag=sorok.strip().split(";")
        nev=sor_tag[0]
        varos=sor_tag[1]
        csapat=sor_tag[2]
        elso=sor_tag[3]
        utolso=sor_tag[4]
        stadion=Stadion(nev, varos, csapat, elso, utolso)
        lista.append(stadion)
    return lista

def NY(lista):
    ny_lista=[]
    for i in range(0, len(lista),1):
        if lista[i].varos=="New York":
            ny_lista.append(i)    
    return ny_lista