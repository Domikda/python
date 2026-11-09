import math 
#proměnné a řetězce
jmeno = "Dominik"
vek = 15
print(f"Jmenuji se {jmeno} a je mi {vek} let.")

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
numbers.sort()
print(f"Seřazený seznam čísel: {numbers}")
print(f"První prvek seznamu: {numbers[0]}")
print(f"Poslední prvek seznamu: {numbers[-1]}")

#Slovníky a množiny

student = {
    "jmeno": "Dominik",
    "vek": 15,
    "predmety": ["Matematika", "Fyzika", "Informatika"]
}

student = {}
student [vek]= 25
student ["jmeno"] = "Dominik"
student ["predmety"] = ["Matematika", "Fyzika", "Informatika"]
print ("student: ", student)

data = {3,3,3,4,5,6,7,8,8,9}
unique_data = set(data)
print("Unikátní data: ", unique_data)

for i in range(1, 20):
    if i % 2 == 0:
        print("Je dělitelné 2")
    elif i % 5 == 0:
        print("Je dělitelné 5")
    else:
        print(i)

def vypocet_obvodu_obdelniku(delka, sirka):
    obvod = 2 * (delka + sirka)
    return obvod

delka = 5
sirka = 3
print(f"Obvod obdelníku s délkou {delka} a šířkou {sirka} je: {vypocet_obvodu_obdelniku(delka, sirka)}")

def vypocet_obvodu_obdelniku(delka, sirka=None):
    if sirka is None:
        sirka = delka
    return 2 * (delka + sirka)
    

delka = 5
sirka = 3
print(f"Obvod obdelníku s délkou {delka} a šířkou {sirka} je: {vypocet_obvodu_obdelniku(delka, sirka)}")
