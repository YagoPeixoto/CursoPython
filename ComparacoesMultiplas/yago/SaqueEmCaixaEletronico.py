'''
Created on 26 de jul de 2016

@author: yago
'''
"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
    notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
 
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
    três notas de 100, uma nota de 50, quatro notas de 10,
    uma nota de 5 e quatro notas de 1.
// %
"""
valorSaque = int(input("Digite o valor que deseja sacar (entre 10 a 600 reais):"))

if 10 <= valorSaque <= 600:
    
    notasCem = valorSaque // 100
    valorSaque = valorSaque % 100
 
    notasCinquenta = valorSaque // 50
    valorSaque = valorSaque % 50
 
    notasDez = valorSaque // 10
    valorSaque = valorSaque % 10
 
    notasCinco = valorSaque // 5
    valorSaque = valorSaque % 5
 
    notasUm = valorSaque // 1
 
    if notasCem > 0:
        print(notasCem, "notas de 100 R$")
        
    if notasCinquenta > 0:
        print(notasCinquenta, "notas de 10 R$")
        
    if notasDez > 0:
        print(notasDez, "notas de 10 R$")
        
    if notasCinco > 0:
        print(notasCinco, "notas de 5 R$")
        
    if notasUm > 0:
        print(notasUm, "notas de 1 R$")
               
else:
    print("O saque é apenas entre 10 a 600 reais.")