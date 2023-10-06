hora = int(input('Quantas horas você trabalha por mês? '))
valor = float(input('Qual é o valor da sua hora de trabalho? R$'))
sal = hora * valor

'''DESCONTOS'''
sind = (sal * 3) / 100
fgts = (sal * 11) / 100
if sal < 900:
    ir = 0
elif sal < 1500:
    ir = (sal * 5) / 100
elif sal < 2500:
    ir = (sal * 10) / 100
elif sal > 2500:
    ir = (sal * 20) /100
descontos = ir + sind + fgts
liquido = sal - descontos

print(f'-Sálario bruto: R${sal:.2f}')
print(f'-Desconto do IR: R${ir:.2f}')
print(f'-Desconto do Sindicato: R${sind:.2f}')
print(f'-Desconto do FGTS: R${fgts:.2f}')
print(f'-Total de descontos: R${descontos:.2f}')
print(f'-Salário liquido: R${liquido:.2f}')