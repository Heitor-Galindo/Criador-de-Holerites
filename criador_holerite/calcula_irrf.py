
from criador_holerite.tabelas import *


def calculo_irrf(aliquota_efetiva_inss, contribuicao_inss, salario_bruto):

    base_calculo_irrf = salario_bruto - contribuicao_inss
    primeira_faixa = False

    if base_calculo_irrf < irrf_fim_primeira_faixa:
        primeira_faixa = True

    elif irrf_fim_primeira_faixa < base_calculo_irrf < irrf_fim_segunda_faixa:
        aliquota_faixa_irrf = irrf_aliquota_segunda_faixa
        desconto_faixa = irrf_desconto_segunda_faixa

    elif irrf_fim_segunda_faixa < base_calculo_irrf < irrf_fim_terceira_faixa:
        aliquota_faixa_irrf = irrf_aliquota_terceira_faixa
        desconto_faixa = irrf_desconto_terceira_faixa

    elif irrf_fim_terceira_faixa < base_calculo_irrf < irrf_fim_quarta_faixa:
        aliquota_faixa_irrf = irrf_aliquota_quarta_faixa
        desconto_faixa = irrf_desconto_quarta_faixa

    elif base_calculo_irrf > irrf_inicio_quinta_faixa:
        aliquota_faixa_irrf = irrf_aliquota_quinta_faixa
        desconto_faixa = irrf_desconto_quinta_faixa

    if primeira_faixa:
        base_calculo_irrf = 0
        desconto_irrf = 0
        aliquota_faixa_irrf = 0
        aliquota_efetiva_irrf = 0
    else:
        desconto_irrf = (base_calculo_irrf *
                         aliquota_faixa_irrf) - desconto_faixa
        aliquota_efetiva_irrf = (desconto_irrf * 100) / salario_bruto

    return aliquota_faixa_irrf, aliquota_efetiva_irrf, base_calculo_irrf, desconto_irrf
