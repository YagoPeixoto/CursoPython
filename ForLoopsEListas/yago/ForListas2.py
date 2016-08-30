'''
Created on 30 de ago de 2016

@author: yago
'''
"""
Escreve um programa que recebe uma lista de números até que seja dada a entrada
-1, e depois imprima todos os números pares da sequência
"""
lista = []

valor = int(input("digite um valor :"))
while valor != -1:
    lista.append(valor)
    valor = int(input("digite um valor :"))
print("Os numeros pares da lista são : ")
for i in lista:
    aux = i % 2
    if aux == 0:
        print(i)