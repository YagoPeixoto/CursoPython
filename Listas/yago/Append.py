'''
Created on 25 de ago de 2016

@author: yago
'''
"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
lista = []
for i in range(1, 6):
    num = int(input("Digite o número %i de 5: "%i))
    lista.append(num)#adiciona a lista o numero digitado
 
print(lista)