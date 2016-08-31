'''
Created on 31 de ago de 2016

@author: yago
'''
"""
Peça uma lista de números inteiros para o usuário
e imprima a lista sem repetições
"""

num = int(input("Digite o número de elementos da lista: "))

lista = []
aux = []

for i in range(num):
    elemento = int(input("Digite o elemento %i de %i: "%(i+1, num)))
    lista.append(elemento)
    aux.append(elemento)

print(lista)

for ele in aux:
    aparicoes = lista.count(ele)
    for i in range(aparicoes-1):
        lista.remove(ele)

print(lista)

