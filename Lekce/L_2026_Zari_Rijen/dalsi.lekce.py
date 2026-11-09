for i in range(2, 100):
    for x in range(2, i):
        print(f"Kontrolující číslo {i} dělené {x}")
        if i % x == 0:      #modulo, zbytek po dělení
            break
        else:
         print(f"{i} ========= JE PRVOČÍSLO =====")
