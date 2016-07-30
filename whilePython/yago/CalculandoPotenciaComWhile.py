'''
Created on 30 de jul de 2016

@author: yago
'''
#Ex para testar while em python na pratica, 
#calcular potencia sem usar EX: "2**4" or "2*2*2*2"

base = int(input("Digite o numero base para calcular sua potencia: "))
expoente = int(input("Digite o valor do expoente: "))

cont = 0
valorFinal = 1

while cont < expoente:
    valorFinal = valorFinal*base
    #valorFinal = valorFinal*expoente
    
    cont = cont+1

print("A potencia de", base ,"evadado a", expoente,"é", valorFinal)

