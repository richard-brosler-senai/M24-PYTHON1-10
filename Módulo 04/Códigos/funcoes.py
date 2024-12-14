"""
Funções uteis para os sistemas
Author: Richard Brosler
Version: 2024-12-14
"""
def mostrar_titulo(titulo = "Programa", num_col = 40):
    # Ajustando para ficar par no tamanho do texto
    if len(titulo) % 2 != 0:
        titulo += " "
    
    num_esp = (num_col - len(titulo)) // 2
    espacos = " " * num_esp
    print("+" + "-" * num_col + "+")
    print("|" + espacos + titulo + espacos + "|")
    print("+" + "-" * num_col + "+")

if __name__ == "__main__":
    mostrar_titulo("Programa de teste",50)
