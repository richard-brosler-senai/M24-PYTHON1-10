"""
Programa para demonstrar escopo de variáveis
Author: Richard Brosler
Version: 2024-12-14
"""
from click import clear
# Definindo uma função
def mostrar_valor():
    #vou usar a variavel do programa agora
    global valor, teste1
    valor = 5
    teste1 = 5 # Criando a variável teste1
    print(valor)

clear()
valor = 50
mostrar_valor()
print("Global",valor, teste1)