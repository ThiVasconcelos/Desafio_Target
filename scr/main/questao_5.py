string_normal = input("Digite um texto para ser invertido: ") 


conjunto_caracteres = list(string_normal)

i = 0
j = len(conjunto_caracteres) - 1

while i < j:
    conjunto_caracteres[i], conjunto_caracteres[j] = conjunto_caracteres[j], conjunto_caracteres[i]
    i += 1
    j -= 1


string_invertida = ''.join(conjunto_caracteres)

print("O texto invertida é:", string_invertida)
