'''
Created on 28 de jul de 2016

@author: yago
'''
"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula
    entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades 
    Testar com: 326, 300, 100, 320, 310,305, 301,
    101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
num = int(input("Digite um numero entre 0 e 1000 para verificar\n" 
"a quantidade de centenas, dezenas e unidades:"))

if 0 <= num <= 1000:
    
    birl = num
    
    centena = birl // 100
    birl = birl % 100
    
    dezena = birl // 10
    birl = birl % 10
    
    unidade = birl // 1
    
    if num >= 100:
        if dezena > 10:
            if unidade > 1:
                print("O numero tem", centena, "centena(s),", dezena, "dezena(s) e", unidade, "unidade(s)")
            else:
                print("O numero tem", centena, "centena(s),", dezena, "dezena(s) e", unidade, "unidade(s)")

    elif num >= 100:
        if dezena < 10:
            if unidade >= 1:
                print("O numero tem", centena, "centena(s) e", unidade, "unidade(s)")

        
else:
    print("Digite um munero entre 0 e 1000") 
    