'''
Created on 27 de jul de 2016

@author: yago
'''
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
num3 = int(input("Digite o terceiro numero:"))

if num1 > num2 > num3:
    print("O maior numero é", num1, "e o menor é", num3)
    
elif num1 > num3 > num2:
    print("O maior numero é", num1, "e o menor é", num2)
    
elif num2 > num1 > num3:
    print("O maior numero é", num2, "e o menor é", num3)

elif num2 > num3 > num1:
    print("O maior numero é", num2, "e o menor é", num1)

elif num3 > num2 > num1:
    print("O maior numero é", num3, "e o menor é", num1)

elif num3 > num1 > num2:
    print("O maior numero é", num3, "e o menor é", num2)
    
else:
    print("Você digitou numeros repitidos.")