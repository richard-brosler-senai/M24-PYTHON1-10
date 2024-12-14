"""
Programa de teste de funções
Author: Richard Brosler
Version: 2024-12-14
"""
from click import clear
from funcoes import mostrar_titulo, fatorial,\
                    popular_lista, fatorial_rec

clear()
# Chamando usando argumentos nomeados
mostrar_titulo(num_col=50,titulo="Programa de Teste")
print(mostrar_titulo()) # retorno None
# Camando usando argumentos posicionais
print("Fatorial de 5=",fatorial(5))
# Criando uma lista
lista = [] # definindo uma lista vazia
popular_lista(lista)
print(lista)
# Diferença quando enviamos variaveis com valor
valor = 6
fatorial(valor)
print(valor)
# Usando o fatorial recursivo
print(fatorial_rec(5)) 
print(fatorial_rec(1000)) # estoura o limite de chamadas