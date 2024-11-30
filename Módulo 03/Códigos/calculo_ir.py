"""
Programa para calculo do IR retido na Fonte
Author: Richard Brosler
Version: 2024-11-30
"""
from click import clear # Usar clear para Limpar a tela
clear() # Limpa a tela
# Definindo as variáveis de IR
"""
A partir de fevereiro de 2024.
Base de cálculo	Alíquota	Dedução
Até R$ 2.259,20	-	-
De R$ 2.259,21 até R$ 2.826,65	7,5%	R$ 169,44
De R$ 2.826,66 até R$ 3.751,05	15,0%	R$ 381,44
De R$ 3.751,06 até R$ 4.664,68	22,5%	R$ 662,77
Acima de R$ 4.664,68	27,5%	R$ 896,00
Rendimentos previdenciários isentos para maiores de 65 anos: R$ 1.903,98
Dedução mensal por dependente: R$ 189,59
"""
limite01 = 2259.20; perc01 = 0;    ded01 = 0
limite02 = 2826.65; perc02 = 7.5;  ded02 = 169.44
limite03 = 3751.05; perc03 = 15.0; ded03 = 381.44
limite04 = 4664.68; perc04 = 22.5; ded04 = 662.77
limite05 = 4664.69; perc05 = 27.5; ded05 = 896.00
ded_dep = 189.59
# Começando o programa
salario = float(input("Digite seu salário: "))
num_dep = int(input("Digite número de dependentes: "))
# Calculando
base_ir = salario - num_dep * ded_dep # subtrair o inss
# Calculo do IR
if base_ir > limite04:
    ir = base_ir * perc05 / 100 - ded05
elif base_ir > limite03:
    ir = base_ir * perc04 / 100 - ded04
elif base_ir > limite02:
    ir = base_ir * perc03 / 100 - ded03
elif base_ir > limite01:
    ir = base_ir * perc02 / 100 - ded02
else:
    ir = base_ir * perc01 / 100 - ded01
# Imprimindo o valor
print("Valor do imposto de renda:",ir)
