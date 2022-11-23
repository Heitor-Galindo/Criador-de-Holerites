from criador_holerite.criador_holerite import criador_holerite
from tabulate import tabulate

lista_salario_bruto = [
    2450.00,
    3500.00,
    3500.00,
    3500.00,
    4375.00,
    4375.00,
    4520.25,
    5031.25,
    5031.25,
    5031.25,
    5534.38
]

tabela_holerite = criador_holerite(lista_salario_bruto)
holerite = tabulate(tabela_holerite, headers='keys',
                    tablefmt='rounded_outline', missingval='N/A')
print(holerite)
