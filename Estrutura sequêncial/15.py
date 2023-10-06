qto = float(input('Quanto você ganha por hora? R$'))
hr = int(input('Quantas horas você trabalhou esse mês? '))
bruto = qto * hr
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - (ir + inss + sind)

print(f'- Sálario bruto: R${bruto}')
print(f'- IR (11%): R${ir}')
print(f'- INSS (8%): R${inss}')
print(f'- Sindicato (5%): R${sind}')
print(f'- Sálario liquido: R${liquido}')