'''
Created on 10 de ago de 2016

@author: yago
'''

peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))

imc = peso/(altura * altura)

print("Seu peso é %dKg, sua altura é %d e seu IMC é %f" %(peso,altura,imc))

if imc < 17:
    print("voce esta muito abaixo do peso")
elif imc >= 17 and imc <= 18.49:
    print("voce esta abaixo do peso")
elif imc > 18.49 and imc <= 24.99:
    print("voce esta dentro do peso")
elif imc > 24.99 and imc <= 29.99:
    print("voce esta acima do peso")
elif imc > 29.99:
    print("voce ta parecendo um porco de granja...\nseu gordo vai comer direito e fazer uma atividade fisica")