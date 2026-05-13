import random

Numero_sorteado = random.randint(1, 100)
tentativas = 0
acertou = False
while not acertou:
    try:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1
        if palpite < Numero_sorteado:
            print("Muito baixo.")
        elif palpite > Numero_sorteado:
            print("Muito alto.")
        else:
            acertou = True
            print(f"Parabéns! Você acertou o número {Numero_sorteado} em {tentativas} tentativas.")
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")