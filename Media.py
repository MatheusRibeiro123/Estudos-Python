notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

#Calcular a media das duas notas

mediafinal = (notaA + notaB) / 2


#verificação 

print(f"Sua nota final é: " ,mediafinal)

if mediafinal >= 7.0:
    print("A media : %.1f - aprovado" %mediafinal )
else : print("A media : %.1f - reprovado" %mediafinal)