'''
Created on 6 de ago de 2016

@author: yago
'''

n = int(input("Digite um numero: "))
cont = 0
soma = 0
 
if n > 1: 
 
    while cont < n:
        num = int(input("Digite um numero: "))
        if num%2 == 0:
            soma += num
        cont += 1
        
    print ("A soma dos pares é ", soma)    
else :
    print("Digite um nuemro maior que 1")