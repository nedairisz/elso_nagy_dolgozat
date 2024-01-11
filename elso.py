"""
a)	Kérj be 1 páros számot a felhasználótól. (1 pont)
Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)
A bekéréshez írj egy függvényt beker(), amely bekéri a kívánt feltételeknek megfelelő számot. . (1 pont)

b)	Az előző metódus felhasználásával - és kiegészítésével - kérj be 3 páros számot a felhasználótól. 
    A program minden lépésben írja ki, hogy hányadik számot kéri be,   az alábbi minta szerint: . (2 pont)
c)	Az előző metódusnak legyen visszatérési értéke, mely a bekért számmal tér vissza, és azt beleteszi egy listába! 
    Írj metódust, mely megkeresi a három bekért szám közül a legkisebbet! A legkisebb számot a program írja ki a konzolra és azt is, 
    hogy hányadiknak adta meg a felhasználó! . (2 pont)
"""

def beker():
    paros:int=int(input("Adj meg egy páros számot: "))
    while not(paros%2==0):
        paros:int=int(input("Ez nem páros. páros számot kérek: "))
    return paros

def harmat():
    lista=[]
    for i in range(0, 3, 1):
        paros:int=int(input(f"Kérem a {i+1}. páros számot: "))
        lista.append(paros)
        while not(paros%2==0):
            paros:int=int(input("Ez nem páros. Páros számot kérek: "))
    return lista

def legisebb(lista):
    lk_index=0
    min=0
    for i in range(0, len(lista), 1):
        if lista[lk_index]<lista[i]:
            lk_index=i
    return lk_index
