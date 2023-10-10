'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

sal = float(input('Qual seu sálario: R$'))
sal1 = 0
percentual = 0

if sal <= 280:
    sal1 = (sal * 20) / 100
    percentual = 20
elif sal > 281 and sal < 700:
    sal1 = (sal * 15) / 100
    percentual = 15
elif sal > 700 and sal < 1500:
    sal1 = (sal * 10) / 100
    percentual = 10
elif sal >= 1500:
    sal1 = (sal * 5) / 100
    percentual = 5

print(f'Sálario antes do reajusto: R${sal:.2f}')
print(f'Percentual do aumento: {percentual}%')
print(f'Valor do aumento: {sal1:.2f}')
print(f'Novo sálario: R${sal + sal1:.2f}')

'''A ordem em que escolhi para fazer a lógica ingluenciou. Lembrar de sempre codar em ordem crescente'''