'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

hrs = int(input('Quantas horas foram trabalhadas esse mês? '))
qto = float(input('Quanto você ganha por hora? '))
sal_bruto = hrs * qto
ir = (sal_bruto * 11) / 100
inss = (sal_bruto * 8) / 100
sind = (sal_bruto * 5) / 100
sal_liq = sal_bruto - (ir + inss + sind)
print(f'''- Sálario bruto R${sal_bruto}: 
- IR: R${ir} (11%)
- INSS: R${inss} (8%)
- Sindicato: R${sind} (5%)
- Sálario liquido: {sal_liq}''')

'''Isso daqui é terapia XD'''