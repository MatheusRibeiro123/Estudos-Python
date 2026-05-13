#Sistema qe verifica se um número é par ou ímpar, e dependendo do resultado, calcula a metade ou o dobro do número.
try:

    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"O número: {numero} é par , e a metade dele é {numero/2}.")
    else:
        print(f"O número: {numero} é ímpar, e o dobro dele é {numero*2}.") 

except ValueError:
    print("Valor inválido. Por favor, digite um número inteiro.")