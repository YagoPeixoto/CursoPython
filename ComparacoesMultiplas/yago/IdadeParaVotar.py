'''
Created on 26 de jul de 2016

@author: yago
'''
idade = int(input("Digite sua idade: "))

if 18 <= idade <= 65:
    
    print("Você é obrigado a votar")
    
if 16 <= idade <= 17:
        print("Você vota só se você quiser")

else:
    if idade > 65: 
        print("Você vota só se você quiser")
