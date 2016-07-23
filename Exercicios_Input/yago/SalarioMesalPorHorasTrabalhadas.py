'''
Created on 23 de jul de 2016

@author: yago
'''
valorGanhoPorHora = (input("Digite quanto voçê ganha por hora(R$): "))
horasPorDia = (input("Digite o numero de horas que vc trabalha por dia: "))
diasNoMes = (input("Digite o numero de dias que vc trabalhou no mês: "))

valorGanhoPorHora = float(valorGanhoPorHora)
horasPorDia = int(horasPorDia)
diasNoMes = int(diasNoMes)

salarioDia = valorGanhoPorHora * horasPorDia
salario = salarioDia * diasNoMes


print("Voçê ganha", salarioDia, "reais por dia")
print("O seu salario mesal deve ser R$", salario)