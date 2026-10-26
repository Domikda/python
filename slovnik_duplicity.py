cislo_list = [1,1,2,2,4,4,5,5,5,6,6,7,7,8,8]
unikatni_cisla = set(cislo_list)
print("unikátní čísla:", unikatni_cisla)
print(f"původní čísla: {cislo_list}")

prazdna_mnozina = set()
prazdna_mnozina.add(150)
prazdna_mnozina.add(90)

print("množina po přidání prvků:", prazdna_mnozina)

if 3 in unikatni_cisla:
    print("číslo 3 je v množině unikátních čísel.")
else:
     print("číslo 3 ---NENÍ--- v množině unikátních čísel.")
     