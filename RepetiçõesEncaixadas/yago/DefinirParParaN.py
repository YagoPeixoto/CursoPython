'''
Created on 7 de ago de 2016

@author: yago
'''
"""
Dados dois naturais m e n determinar, entre todos os pares de números naturais
(x,y) tais que x < m e y < n, um par para o qual o valor da expressãox*y - x**2 + y 
seja máximo e calcular também esse máximo.
"""
 
n = int(input("Digite um valor para n: "))
m = int(input("Digite um valor para m: "))
x = y = z = 0
 
a = b = 0
for a in range(m):
    for b in range(n):
        if a*b - a*a + b > z:
            z = a*b - a*a + b
            x = a
            y = b
 
print ("O maior par possivel é (%i,%i) o valor maximo é %i" %(x, y, z))