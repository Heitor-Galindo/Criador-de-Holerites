from criador_holerite.calcula_irrf import calculo_irrf
from criador_holerite.calcula_inss import calculo_inss


lista_referencia = [
    '01/22',
    '02/22',
    '03/22',
    '04/22',
    '05/22',
    '06/22',
    '07/22',
    '08/22',
    '09/22',
    '10/22',
    '11/22',
    '12/22'
]

lista_bruto = []
lista_liquido = []
lista_desconto_total = []
lista_aliquota_faixa_inss = []
lista_aliquota_efetiva_inss = []
lista_aliquota_faixa_irrf = []
lista_aliquota_efetiva_irrf = []
lista_contribuicao_inss = []
lista_base_calculo_irrf = []
lista_desconto_irrf = []


def criador_holerite(lista_salario_bruto: list):

    for salario_bruto in lista_salario_bruto:

        aliquota_faixa_inss, aliquota_efetiva_inss, contribuicao_inss = calculo_inss(
            salario_bruto)

        aliquota_faixa_irrf, aliquota_efetiva_irrf, base_calculo_irrf, desconto_irrf = calculo_irrf(
            aliquota_efetiva_inss, contribuicao_inss, salario_bruto)

        aliquota_faixa_inss = aliquota_faixa_inss * 100
        aliquota_faixa_irrf = aliquota_faixa_irrf * 100
        desconto_total = contribuicao_inss + desconto_irrf
        salario_liquido = salario_bruto - desconto_total

        lista_bruto.append(f"R$ {salario_bruto:.2f}")
        lista_liquido.append(f"R$ {salario_liquido:.2f}")
        lista_aliquota_faixa_inss.append(f"{aliquota_faixa_inss:.2f}%")
        lista_aliquota_efetiva_inss.append(f"{aliquota_efetiva_inss:.2f}%")
        lista_aliquota_faixa_irrf.append(f"{aliquota_faixa_irrf:.2f}%")
        lista_aliquota_efetiva_irrf.append(f"{aliquota_efetiva_irrf:.2f}%")
        lista_contribuicao_inss.append(f"R$ {contribuicao_inss:.2f}")
        lista_base_calculo_irrf.append(f"R$ {base_calculo_irrf:.2f}")
        lista_desconto_irrf.append(f"R$ {desconto_irrf:.2f}")
        lista_desconto_total.append(f"R$ {desconto_total:.2f}")

    tabela_holerite = {
        "MES REF": lista_referencia,
        "SAL BRUTO": lista_bruto,
        "ALIQ INSS": lista_aliquota_faixa_inss,
        "EFET INSS": lista_aliquota_efetiva_inss,
        "DESC INSS": lista_contribuicao_inss,
        "BASE IRRF": lista_base_calculo_irrf,
        "DESC IRRF": lista_desconto_irrf,
        "ALIQ IRRF": lista_aliquota_faixa_irrf,
        "EFET IRRF": lista_aliquota_efetiva_irrf,
        "DESC TOTAL": lista_desconto_total,
        "SAL LIQUIDO": lista_liquido,
    }

    return tabela_holerite
