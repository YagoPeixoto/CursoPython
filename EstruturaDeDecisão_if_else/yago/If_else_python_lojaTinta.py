'''
Created on 24 de jul de 2016

@author: yago
'''
"""
O programa devera pedir o tamanho em metros quadrados da area a ser pintada.
considere que a cobertura da tita é de 1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros que custam R$ 80,00.Informe ao usuario 
a quatidade de latas de tinta a serem compradas e o preço total.
"""
tamanhoArea = float(input("Digite o tamanho da area que vai ser pintada: "))

litrosTinta = tamanhoArea // 3

if tamanhoArea % 3 > 0:
    litrosTinta = litrosTinta + 1
 
latas = litrosTinta//18

if litrosTinta % 18 > 0:
    latas = latas + 1
    
print("voce vai gastar", litrosTinta, "litro(s)")
print("Você vai precisar de", latas, "lata(s).")
print("O valor das latas será R$", latas*80)
