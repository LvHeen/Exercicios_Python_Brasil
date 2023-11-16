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

salario = float(input("Digite o seu salário: R$"))

desconto_20 = salario * 0.20
novo_20 = salario * 1.20 
desconto_15 = salario * 0.15
novo_15 = salario * 1.15
desconto_10 = salario * 0.10
novo_10 = salario * 1.10
desconto_5 = salario * 0.05
novo_5 = salario * 1.05

print(f'Antes Reajuste: R${salario:.2f}')

if salario <= 280: 
    print('20% de aumento')
    print(f'Valor do aumento: R${desconto_20:.2f}')
    print(f'Salário depois do reajuste: R${novo_20:.2f}')
elif salario > 200 and salario <= 700: 
    print('15% de aumento')
    print(f'Valor do aumento: R${desconto_15:.2f}')
    print(f'Salário depois do reajuste: R${novo_15:.2f}')    
elif salario > 700 and salario <= 1500: 
    print('10% de aumento')
    print(f'Valor do aumento: R${desconto_10:.2f}')
    print(f'Salário depois do reajuste: R${novo_10:.2f}')    
else: 
    print('5% de aumento')
    print(f'Valor do aumento: R${desconto_5:.2f}')
    print(f'Salário depois do reajuste: R${novo_5:.2f}')