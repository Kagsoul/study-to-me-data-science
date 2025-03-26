# biblioteca from e import poderia usa as para camuflar

from datetime import datetime

# Entrada dos Dados

data_nasc = input("informe a data do seu nascimento (dd/mm/aaaa):")

data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")

idade = datetime.now().year - data_nasc.year

# Processamento dos Dados
if datetime.now().month < data_nasc.month or (datetime.now().month == data_nasc.month and datetime.now(). day < data_nasc.day):
 idade -= 1

# Saída dos Dados
print(f'A sua idade é {idade} anos.')

#dor de cabeça, data em forma de variavel não pode ser date, presta atenção nisso na proxima vez