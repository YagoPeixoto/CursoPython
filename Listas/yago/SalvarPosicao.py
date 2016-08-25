'''
Created on 25 de ago de 2016

@author: yago
'''
"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os dois vetores.
"""
listaPar = []
listaImpar=[]

print("digite somente numeros inteiros!!!")
 
for i in range(1,21):
    num = int(input("digite o %dº numero :"%i))
   
    restoDivisao = num % 2
    
    if restoDivisao == 0:
        listaPar.append(num)
    
    else:
        listaImpar.append(num)
        
print("A lista par comtém os seguintes numeros:", listaPar)
print("A lista impar comtém os seguinets numeros:", listaImpar)