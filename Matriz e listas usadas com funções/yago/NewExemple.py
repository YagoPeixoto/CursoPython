'''

Created on 20 de set de 2016

@author: yago
'''
prod = 2

def soma(prod):
    prod += 3
    
print(prod)#quando  a variavel esta fora da função ela apenas cria uma copia dendro da função
#pois esta em outro endereço de memoria

lista1 = [1,2,3,4,5,6]
  
def modificaLista():
    lista1[0] += 9
    
print(lista1)# já uma lista que esta de fora da função pode ser usada dentro e ser modificada pois o endereço de memoria é modificado diferentemente  de uma variavel comum

