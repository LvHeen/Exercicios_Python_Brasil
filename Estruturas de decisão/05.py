n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

if m == 10:
    print('APROVADO COM DISTIÇÃO')
elif m >= 7:
    print('APRVADO COM DISTINÇÃO')
elif m < 7:
    print('REPROVADO')