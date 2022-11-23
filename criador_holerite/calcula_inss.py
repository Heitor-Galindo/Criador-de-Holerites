
from criador_holerite.tabelas import *


def calculo_inss(salario_bruto: float):
    primeira_faixa = False
    quarta_faixa = False

    for i in range(8):

        if salario_bruto < inss_fim_primeira_faixa:
            aliquota_faixa_inss = inss_aliquota_primeira_faixa
            primeira_faixa = True

        elif inss_fim_primeira_faixa < salario_bruto < inss_fim_segunda_faixa:
            aliquota_faixa_inss = inss_aliquota_segunda_faixa
            faixa = inss_inicio_segunda_faixa
            desconto_faixa = inss_desconto_primeira_faixa

        elif inss_fim_segunda_faixa < salario_bruto < inss_fim_terceira_faixa:
            aliquota_faixa_inss = inss_aliquota_terceira_faixa
            faixa = inss_inicio_terceira_faixa
            desconto_faixa = inss_desconto_primeira_faixa + inss_desconto_segunda_faixa

        elif inss_fim_terceira_faixa < salario_bruto < inss_fim_quarta_faixa:
            aliquota_faixa_inss = inss_aliquota_quarta_faixa
            faixa = inss_inicio_quarta_faixa
            desconto_faixa = inss_desconto_primeira_faixa + \
                inss_desconto_segunda_faixa + inss_desconto_terceira_faixa

        elif salario_bruto > inss_fim_quarta_faixa:
            quarta_faixa = True
            desconto_faixa = inss_desconto_primeira_faixa + inss_desconto_segunda_faixa + \
                inss_desconto_terceira_faixa + inss_desconto_quarta_faixa

    if primeira_faixa:
        contribuicao_inss = salario_bruto * aliquota_faixa_inss
        aliquota_efetiva_inss = aliquota_faixa_inss
    elif quarta_faixa:
        contribuicao_inss = desconto_faixa
        aliquota_efetiva_inss = (contribuicao_inss * 100) / salario_bruto
    else:
        contribuicao_inss = ((salario_bruto - faixa) *
                             aliquota_faixa_inss) + desconto_faixa
        aliquota_efetiva_inss = (contribuicao_inss * 100) / salario_bruto

    return aliquota_faixa_inss, aliquota_efetiva_inss, contribuicao_inss
