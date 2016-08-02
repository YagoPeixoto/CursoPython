'''
Created on 1 de ago de 2016

@author: yago
'''
num = int(input("digite um numero positivo para calcular o fatorial: "))

valorFinal = num
cont = valorFinal

while cont > 1:
    valorFinal = valorFinal * (cont -1)
    cont = cont - 1
    
print("O fatorial de", num, "é", valorFinal)