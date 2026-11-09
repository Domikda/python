import random #AI pomoc

Jméno_Petr = "Petr"
Příjmení_Petr = "Novák"
Jméno_Petr2 = "Petře"
Příjmení_Petr2 = "Nováku"
Věk_Petr = 30

Jméno_Karel = "Karel"
Příjmení_Karel = "Svoboda"
Jméno_Karel2 = "Karle"
Příjmení_Karel2 = "Svobodový"
Věk_Karel = 44

pozdrav_Petr_privitani = f"Dobrý den"
pozdrav_Petr = f"Jmenuji se {Jméno_Petr} {Příjmení_Petr} a je mi {Věk_Petr} let a vy?"
pozdrav_Petr2 = f"Také mě těší, že jsem vás potkal {Jméno_Karel2} {Příjmení_Karel2}."

pozdrav_Karel_privitani = f"Dobrý den"
pozdrav_Karel = f"Já jsem {Jméno_Karel} {Příjmení_Karel} a je mi {Věk_Karel} let a jsem rád, že jsem vás potkal {Jméno_Petr2} {Příjmení_Petr2}."
pozdrav_Karel2 = f"Já jsem {Jméno_Karel} {Příjmení_Karel} a je mi {Věk_Karel} let a jsem rád, že jsme se potkali."

random_choice = random.choice([pozdrav_Karel, pozdrav_Karel2]) #AI pomoc

print(pozdrav_Petr_privitani)
print(pozdrav_Karel_privitani)
print(pozdrav_Petr)
print(random_choice)
if random_choice == pozdrav_Karel:
    print(pozdrav_Petr2)