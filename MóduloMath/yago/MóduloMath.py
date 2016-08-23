'''
Created on 23 de ago de 2016

@author: yago
'''
import math #importa o modulo math
 
print(math.sin(1))#imprime o seno
print(math.cos(2))#imprime o cosceno
print(math.tan(3))#imprime a tangente
print(math.pow(2, 2))#imprime o primeiro numero elevado ao segundo
print(math.sqrt(4))#imprime a raiz quadrada
 
from math import sin#importa apenas a função sin do modulo math
 
print(sin(1))

import math as m#muda o nome do modulo
 
print(m.sin(1))
print(m.cos(2))
print(m.tan(3))
print(m.pow(2, 2))
print(m.sqrt(4))
 
 
 
from math import sin as s#muda o nome da função 
print(s(1))

# o modulo math contem muitas outras utilidades e funções matematicas