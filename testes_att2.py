#Sistema que conta o número de vogais em uma palavra e quantas vezes cada vogal aparece.

user_word = str(input("Digite uma palavra: "))
numero_de_vogais = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for letra in user_word:
    if letra.lower() in "aeiou":
        numero_de_vogais += 1

        if letra.lower() == "a":
            a += 1
        elif letra.lower() == "e":
            e += 1
        elif letra.lower() == "i":
            i += 1
        elif letra.lower() == "o":
            o += 1
        elif letra.lower() == "u":
            u += 1

print(f"A palavra: {user_word} tem {numero_de_vogais} vogais.")
print(f"A letra 'a' aparece {a} vezes.")
print(f"A letra 'e' aparece {e} vezes.")
print(f"A letra 'i' aparece {i} vezes.")
print(f"A letra 'o' aparece {o} vezes.")
print(f"A letra 'u' aparece {u} vezes.")



