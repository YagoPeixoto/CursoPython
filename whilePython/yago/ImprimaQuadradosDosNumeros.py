'''
Created on 3 de ago de 2016

@author: yago
'''
"""imprimir o quadrado do numero digitado e parar o programa quando for digitado 
um 0"""

num = int(input("Digite um numero: "))
while num != 0:
    print ("O quadrado de", num, "é", num*num)
    num = int(input("Digite um numero: "))
