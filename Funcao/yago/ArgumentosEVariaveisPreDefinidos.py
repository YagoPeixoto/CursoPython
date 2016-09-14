'''
Created on 14 de set de 2016

@author: yago
'''
def soma(*nums):
    soma_num = 0
    for num in nums:
        soma_num += num
 
    return soma_num
 
def media(p1, p2, p3, peso1 = 1, peso2 = 1, peso3 = 1):#aki eu ja defino o peso das provas sem precisar ficar repetindo
    return(p1*peso1 + p2*peso2 + p3*peso3)/soma(peso1, peso2, peso3)
 
print(media(6, 6, 9, 2))#os 3 primeiros valores são as notas o 4ºvalor subistitui o valor do peso 1, ou seja quando precisar mudar algum valor a preferenci será para o valor dessa linha se e não for necessario já pode deichar o valor pré definido 