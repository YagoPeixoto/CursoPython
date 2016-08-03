'''
Created on 3 de ago de 2016

@author: yago
'''

"""
Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
"""
n = int(input("Digite o numero: "))
cont = 0
soma = 1
aux = n
if 1 <= n <= 9 :
    while cont < n:
        aux = aux % 2
        if aux == 1:
            soma = soma + 2
            cont = cont + 1
            print("O impares são:")
            print(soma)
            
        elif aux == 0:
            soma = soma + 1
            soma = soma + 2            
            cont = cont + 1
            
            print("O inpares são:")
            print(soma)
else: 
    print("Digite um numero entre 1 e 9 ")