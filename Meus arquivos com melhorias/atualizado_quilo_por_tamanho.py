
altura = float(input('Informe a sua altura em metros: '))

print(f"sua altura e {altura:,.2f}")


print("[1] - se voce for homen digite 1: ")

print ("[2] - se voce for mulher digite 2: ")

escolha = input ('escolha uma das opção: ')


if (escolha) == '1':
     input (1)
     print ("pressione enter para saber o resultado: ")
     h = (72.7*altura) - 58
     print(f'O peso ideal para homens é {h:,.2f} Kg.')


elif (escolha) == '2':
     input (2)
     print ("pressione enter para saber o resultado: ")
     m = (62.1*altura) - 44.7
     print(f'O peso ideal para mulheres é {m:,.2f} Kg.')
 
