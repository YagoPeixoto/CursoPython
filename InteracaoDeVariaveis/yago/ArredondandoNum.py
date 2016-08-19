'''
Created on 19 de ago de 2016

@author: yago
'''
#int1 = int(input("Digite um numero inteiro: "))
decimal =float(input("digite um numero decimal: "))

if decimal != int(decimal):

    auxDecimal = decimal - int(decimal) 
    arredondar = int(decimal)
    
    if auxDecimal >= 0.5 :
        print(arredondar + 1)
        
    else:
        print(arredondar)
        
        #print(round(decimal))