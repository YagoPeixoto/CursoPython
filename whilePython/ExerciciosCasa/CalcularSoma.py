'''
Created on 3 de ago de 2016

@author: yago
'''
"""
Dado um número inteiro positivo n,
calcular a soma dos n primeiros números inteiros positivos.
"""
 
n = int(input("Digite um numero: "))
cont = 0
soma = 0

while cont < n:
    num = int(input("Digite um número da sequência: "))
    if num > 0:
        soma = soma + num
    cont = cont + 1
print("O Resultado é", soma)