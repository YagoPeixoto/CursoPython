'''
Created on 6 de ago de 2016

@author: yago
'''
n = int(input("Digite um nuemro: "))
cont, soma = 2, 1
if 0 <  n < 0:  
    while cont < n:
        if n % cont == 0:
            soma += cont
            cont += 1
            if soma == n:
                print ("O número", n, "é perfeito")
            else:
                print ("O número", n, "não é perfeito")
                
else : 
    print("digite um numero maior que 0")