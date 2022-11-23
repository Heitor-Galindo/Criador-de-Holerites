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

        lista_bruto.append(salario_bruto)
        lista_liquido.append(salario_liquido)
        lista_aliquota_faixa_inss.append(aliquota_faixa_inss)
        lista_aliquota_efetiva_inss.append(aliquota_efetiva_inss)
        lista_aliquota_faixa_irrf.append(aliquota_faixa_irrf)
        lista_aliquota_efetiva_irrf.append(aliquota_efetiva_irrf)
        lista_contribuicao_inss.append(contribuicao_inss)
        lista_base_calculo_irrf.append(base_calculo_irrf)
        lista_desconto_irrf.append(desconto_irrf)
        lista_desconto_total.append(desconto_total)

    tabela_holerite = {
        "MES REF": lista_referencia,
        "SAL BRUTO (R$)": lista_bruto,
        "BASE IRRF (R$)": lista_base_calculo_irrf,
        "DESC NSS (R$)": lista_contribuicao_inss,
        "DESC IRRF (R$)": lista_desconto_irrf,
        "DESC TOTAL (R$)": lista_desconto_total,
        "SAL LIQUIDO (R$)": lista_liquido,
        "ALIQ INSS (%)": lista_aliquota_faixa_inss,
        "ALIQ IRRF (%)": lista_aliquota_faixa_irrf,
        "EFET INSS (%)": lista_aliquota_efetiva_inss,
        "EFET IRRF (%)": lista_aliquota_efetiva_irrf,
    }

    return tabela_holerite
