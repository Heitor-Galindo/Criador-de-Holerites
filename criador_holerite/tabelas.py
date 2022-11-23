"""
https://www.in.gov.br/en/web/dou/-/portaria-interministerial-mtp/me-n-12-de-17-de-janeiro-de-2022-375006998

Tabela INSS 2022
Salário de Contribuição (R$) | ALIQUOTA (%) | DESCONTO POR FAIXA (R$)
00,00       até 1.212,00     | 7,5%         | 90,90
de 1,212,01 até 2.427,35     | 9%           | 109,38
de 2.427,36 até 3.641,03     | 12%          | 145,64
de 3.641,04 até 7.087,22     | 14%          | 482,47
"""

inss_inicio_segunda_faixa = float(1212.01)
inss_inicio_terceira_faixa = float(2427.36)
inss_inicio_quarta_faixa = float(3641.04)

inss_fim_primeira_faixa = float(1212.00)
inss_fim_segunda_faixa = float(2427.35)
inss_fim_terceira_faixa = float(3641.03)
inss_fim_quarta_faixa = float(7087.22)

inss_aliquota_primeira_faixa = float(0.075)
inss_aliquota_segunda_faixa = float(0.09)
inss_aliquota_terceira_faixa = float(0.12)
inss_aliquota_quarta_faixa = float(0.14)

inss_desconto_primeira_faixa = float(90.90)
inss_desconto_segunda_faixa = float(109.38)
inss_desconto_terceira_faixa = float(145.64)
inss_desconto_quarta_faixa = float(482.47)

"""
https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/tributos/irpf-imposto-de-renda-pessoa-fisica#tabelas-de-incid-ncia-mensal

Tabela Imposto de Renda 2022
Base de Cálculo             | Alíquota (%)	| Parcela a Deduzir do IR (R$)
De 00,00    até 1.903,98	| 0             | 0
De 1.903,99 até 2.826,65	| 7,5	        | 142,80
De 2.826,66 até 3.751,05	| 15	        | 354,80
De 3.751,06 até 4.664,68	| 22,50	        | 636,13
Acima de 4.664,68	        | 27,50	        | 869,36
"""

irrf_inicio_segunda_faixa = float(1903.99)
irrf_inicio_terceira_faixa = float(2826.66)
irrf_inicio_quarta_faixa = float(3751.06)
irrf_inicio_quinta_faixa = float(4664.68)

irrf_fim_primeira_faixa = float(1903.98)
irrf_fim_segunda_faixa = float(2826.65)
irrf_fim_terceira_faixa = float(3751.05)
irrf_fim_quarta_faixa = float(4664.68)

irrf_aliquota_segunda_faixa = float(0.075)
irrf_aliquota_terceira_faixa = float(0.15)
irrf_aliquota_quarta_faixa = float(0.225)
irrf_aliquota_quinta_faixa = float(0.275)

irrf_desconto_segunda_faixa = float(142.80)
irrf_desconto_terceira_faixa = float(345.80)
irrf_desconto_quarta_faixa = float(636.13)
irrf_desconto_quinta_faixa = float(869.36)
