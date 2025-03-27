
carry = input(print('qual a marca do carro?: '))
cm = eval(input("informe o quilometro da estrada: "))
d = int(input("Informe a distância percorrida (Km): "))
t = float(input("Informe o tempo de viagem (Horas): "))
Placa = input(print('qual e a placa do carro: '))

# Processamento dos Dados
vm = d / t
l = d / cm

# Saída dos Dados
print(f"A velocidade média do veículo foi {vm:.2f} Km/h.")

print(f"A quantidade gasta de combustível foi {l:.1f} litros.")

print(f'a marca do carro e "{carry}" placa "{Placa}"')
