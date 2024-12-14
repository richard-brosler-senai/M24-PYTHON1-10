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

def fatorial(valor):
    # 5! = 5x4x3x2x1 = 120
    res = 1
    for i in range(valor,1,-1):
        res *= i # res = res * i
    valor = 60
    return res

def popular_lista(lista):
    for i in range(5):
        lista.append(i)

def fatorial_rec(valor):
    if valor < 2:
        return 1
    return valor * fatorial_rec(valor - 1)

if __name__ == "__main__":
    mostrar_titulo("Programa de teste",50)
