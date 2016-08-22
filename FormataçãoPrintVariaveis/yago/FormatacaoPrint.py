'''
Created on 22 de ago de 2016

@author: yago
'''
num1 = 10

print("%d, %i"%(num1, 20) )# o %d or %i significa que ira imprimir valores inteiros
print("%f"%(num1))# o %f colocada dessa forma signinica que ira imprimir um numero floute 
print("%.3f"%(num1))# o valor depois do ponto no caso 3 define o numero de casas francionadas que vira depois do numero inteiro em um print float
print("%15.5f"%(num1))#quando colocado assim a sua impresão deve ocupar o numero minimo de espaços definido antes do ponto no caso aqui é 15
print("%g"%100000000000000)#quando o numero é grande é comveniente usar o %g assim o numero sai como anotação cientifica
print("%g"%0.23829382382)# quando o numero é tem muitas casas dps do ponto o %g limita as casa a 6 digitos
print("%12.g"%0.27829382382)