#Ingatlanos megbízási-kalkulátor
"""
m2=float(input("Alepterület m²-ben megadva: "))
ar=float(input("Hirdetési ár: "))
jut=float(input("Jutalék százalékban megadva: "))
m2ar=float(input("Felbecsült piaci ár m²-ben megadva:"))

juti=ar/100*jut
afa=juti/100*27

print ("Hirdtési ár alapján kalkulált m²-ár:", ar//m2,"-Ft/m².")

print ("Jutalék nettó:",juti,"Ft")

print ("Áfa(27%):",afa,"Ft")

print ("Jutalék bruttó:",juti+afa,"Ft")

print ("Ingatlan értéke a becsült m² ár alapján:",m2ar*m2,"Ft")
"""

#Számológép_alap
"""
print("Kérem az első számot:")
szam1 = float(input())

print("Kérem az második számot:")
szam2 = float(input())

print("Válassza ki a műveletet (+, -, *, /):")
muvelet = input()

if muvelet == "+":
  eredmeny = szam1 + szam2
elif muvelet == "-":
  eredmeny = szam1 - szam2
elif muvelet == "*":
  eredmeny = szam1 * szam2
elif muvelet == "/":
  eredmeny = szam1 / szam2
else:
  print("Hibás művelet!")

print("Eredmény: ", eredmeny)
"""

#Euro FT váltó
"""
arfolyam=(input ("Kérem adja meg az aktuális napi árfolyamot:"))
arfolyam=int (arfolyam)
mennyiseg=(input ("Kérem adja meg, mennyi ft-ot szeretne átváltani:"))
mennyiseg=int(mennyiseg)
print (mennyiseg,'-Ft \n Összesen:',arfolyam*mennyiseg,'€')
"""


