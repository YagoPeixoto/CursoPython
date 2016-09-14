'''
Created on 14 de set de 2016

@author: yago
'''
"""
Escreva uma função que obtenha o maior número de uma sequência de números
"""
 
def maiorNum(*nums):
    maior = nums[0]
 
    for num in nums:
        if num > maior:
            maior = num
 
    return maior

print(maiorNum(1,2,32,4,5,5,7,8,2))