python_devs = {"Pepa", "Jirka", "Honza", "Marek",}
java_devs = {"Romana", "Petr", "Karel",}

# Operace sjednocení (NEBO)
vsichni_devs = python_devs | java_devs
print("všichni vývojáři (sjednocení):",vsichni_devs)
print(20*"=")
# Operace průniku
Polygot_devs = python_devs & java_devs
print("vývojáři, kteří ovládají oba jazyky (průnik):", Polygot_devs)
# Operace rozdíl (-)
vsichni_devs = python_devs | java_devs
print ("všichni vývojáři (rozdíl)")