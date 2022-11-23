from criador_holerite.criador_holerite import criador_holerite
from tabulate import tabulate
import re

lista_salario_bruto = [
    900.00,
    1200.00,
    2400.00,
    3500.00,
    3900.00,
    4300.00,
    4500.00,
    5300.00,
    6900.00,
    7800.00,
    9500.00,
    16700.00
]

tabela_holerite = criador_holerite(lista_salario_bruto)


def impressor_txt(tabela_holerite):
    holerite_txt = tabulate(tabela_holerite, headers='keys',
                            tablefmt='rounded_outline', missingval='0', floatfmt=".2f")
    with open('holerites/holerite.txt', 'w') as file:
        file.write(holerite_txt)
    file.close()
    print(holerite_txt)


def impressor_csv(tabela_holerite):
    holerite_csv = tabulate(tabela_holerite, headers='keys',
                            tablefmt='tsv', missingval='0', floatfmt=".2f")
    holerite_csv = re.sub(r'\t', ';', holerite_csv)
    holerite_csv = re.sub(r'[.]', ',', holerite_csv)
    with open('holerites/holerite.csv', 'w') as file:
        file.write(holerite_csv)
    file.close()


impressor_txt(tabela_holerite)
impressor_csv(tabela_holerite)
