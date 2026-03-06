numero1 = int(input("Digite seu primeiro numero:  "))
numero2 = int(input("Digite seu segundo numero:  "))
numero3 = int(input("Digite seu terceiro numero:  "))

if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero1 and numero2 > numero3:
    print(numero2)
else:
    print(numero3)