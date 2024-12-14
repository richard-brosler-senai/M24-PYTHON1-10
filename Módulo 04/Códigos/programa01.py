"""
Programa de teste de funções
Author: Richard Brosler
Version: 2024-12-14
"""
from click import clear
from funcoes import mostrar_titulo, fatorial

clear()
# Chamando usando argumentos nomeados
mostrar_titulo(num_col=50,titulo="Programa de Teste")
print(mostrar_titulo()) # retorno None
# Camando usando argumentos posicionais
print("Fatorial de 5=",fatorial(5))