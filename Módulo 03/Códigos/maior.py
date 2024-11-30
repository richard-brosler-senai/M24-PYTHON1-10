maior_numero = -999_999_999
numero = 0
while numero != -1:
    numero = int(input("Digite um número (-1 = fim): "))
    if numero > maior_numero:
        maior_numero = numero
print("O maior número foi", maior_numero)
print("Fim do programa")