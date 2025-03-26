import time as tempo

nome = (input('digite seu nome completo: '))
print (f"obrigado {nome} por voce está a fazer uma doação de sangue, veremos se voce esta adaptado a está condição")
numero_consulta = float(input('por favor digite seu numero da consulta: '))
lp = 0
pl = 49
pm = 50
pmax = 100
peso = pm <= pmax # 50 ta meio confuso isso mais foi nescessario
bit =lp <= pl # 0 < 49


peso_consulta = float (input(" me diga qual e o seu peso: "))

if pm <= peso_consulta <= pmax:
    print(f"{peso_consulta} kg - Voce está no peso adequado!")
elif lp <= peso_consulta <= pl:
    print(f"{peso_consulta} kg - Voce não está no peso adequado.")
else:
    print("Obrigado, mas voce nao está qualificado para doar.")

horas = 24 
jejum_meia = 12
jejum_oito = 8

horas_d = float(input(f"quantas horas voce esta de jejum {jejum_meia}horas ou {jejum_oito}horas: "))
print ("______aviso importante_______")
print ("se você esta sentindo fraqueza ou tontura algum sintomas diferente informe algum agente medico por perto na infermaria")


if horas_d >= jejum_meia:
    print(f"{horas_d} Parabens Voce conseguiu passar nesta etapa. Agora veremos se voce esta apto pela sua idade.")
elif jejum_oito <= horas_d < jejum_meia:
    print(f"{horas_d} horas, voce esta qualificado, parabens, veremos ser voce esta apto pela sua idade")
else:
    print("Obrigado, mas voce nao esta qualificado para doar devido ao tempo de jejum insuficiente.")

age = float (input("digite sua idade: "))

if (age) == 16 <69:
    age = 16 < 69 
    print (f'você tem {age} anos você esta adaptado a esta condição')
elif(age):
    print (f"{age} e sua idade? você não esta com a idade qualificada para doar, obrigado")
else: 
 print ("fechando a chamada")




