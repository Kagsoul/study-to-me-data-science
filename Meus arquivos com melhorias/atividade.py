import sys 
import math

enter =  input("aperte <enter>")

p_onibus = int(input("coloque quantos onibus voce possui: "))
t_acicular = int(input("coloque quantos onibus esta circulando:" ))

n_garante =  p_onibus - t_acicular 
    

print (f'voce tem {t_acicular} circulando hoje: ')
print (f'voce possui {p_onibus} ônibus') 
print (f'você tem na garagem {n_garante}: ')


print (f"voce tem guardado {n_garante} na garagem, neste momento: ")

print (f" voce tem {t_acicular} circulando, e parados estão {n_garante}, em sua garagem voce possui um total de {n_garante} ")

print (".")
print (".")
opcao = input("<pressione qualquer tecla para ver as opção>")
opcao = print(f" oq voce gostaria de fazer com os onibus que estão na garagem que são {n_garante}?")


print('[1] Fazer manutençao. ')
print('[2] ativa a verificaçao da estrutura.')
print('[3] Limpar ônibus')

opcao_E = input ("escolha umas das opção")

if (opcao_E) == '1':
    print ("_____")
    print (f"enviaremos os veiculos da garagem para a manutenção total {n_garante}")
    print("_____")

elif (opcao_E) == '2':
    print ("_____")
    print ('verificação foi ativada para todos os onibus')
    print ("_____")
    
    
elif (opcao_E) == '3':
    print ("_____")
    print (f'enviaremos para limpar{n_garante}')
    print ("_____")

    
    print (f'baseado na quantidade de veiculos circulando que são {t_acicular} dentro a 30 cadeira e o valor: ')
    
c_passageiro = eval(input(f' digite quantos passageiro foram transportado hoje: '))
d_valorP = float(input(f'digite o valor da passagem: '))

print (".")
print (f"a quantidade de passageiro que foram transportado fora {c_passageiro} e cada um pagou {d_valorP}")
print (".")



valorP = c_passageiro * d_valorP 

(print(f'o valor adquerido foi de {valorP:,.2f} '))

class valores: 
 #a ideia é: puxa todas as variaveis para a class valores, e importa para o novo script imput.py

 print (f"total adquerido foi de R${valorP:,.2f} com {c_passageiro} passageiro, e cada um pagou um valor de R${d_valorP:,.2f}, e voce tem guardado na garagem {n_garante} onibus, e a circular são {t_acicular} ")

 valores = {valorP, c_passageiro, n_garante, t_acicular, d_valorP }
 


sair = input ("pressione <enter> para sair")

sair = print ('script fechado')