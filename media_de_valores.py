qtd = 0
soma= 0
media= 0
valor = float(input("digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1

    #entrada de valores
    valor = float(input("digite um valor: "))

#caso algum valor negativo for digitado o laço de repetiçao se encerra

media = soma / qtd

print ("\n Total da soma:" , soma)
print ("\n Quantidade de valores digitados :", qtd)
print ("\n Media de valores :", media)
