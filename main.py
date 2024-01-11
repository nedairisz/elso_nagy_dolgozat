import elso
import masodik
import harmadik

"""
print("1. FELADAT")
paros=elso.beker()
print(paros)
print()
print()"""

lista=elso.harmat()
print(lista)
lk_index=elso.legisebb(lista)
print(f"A legkisebb szám: {lk_index}, helye: {lista[lk_index]} ")
print()
print()

print("2. FELADAT")
lista=masodik.veletlenek()
print(lista)
szamlalo=masodik.ketjegyuek_szama(lista)
print(f"{szamlalo} db kétjegyű szám van a listában!")
osszeg=masodik.paros_osszege(lista)
print(f"A listában lévő páros számok összege: {osszeg}")
osszesen=masodik.paratlan_osszege(lista)
print(f"A listában lévő páratlan számok összege: {osszesen}")
if osszesen>osszeg:
    print(f"A páratlanok összege {osszesen} > nagyobb a párosak összegénél {osszeg}")
else:
    print(f"A párosak összege {osszeg} > nagyobb a páratlanok összegénél {osszesen}")
print()
print()

print("3. FELADAT")
lista=harmadik.beolvas()
print(f"{len(lista)} db csapat van.")
ny_lista=harmadik.NY(lista)
print(ny_lista)
for i in range(0, len(ny_lista),1):
    index=ny_lista[i]
    print(f"{lista[index].nev}: {lista[index].cspat} db csapat")
