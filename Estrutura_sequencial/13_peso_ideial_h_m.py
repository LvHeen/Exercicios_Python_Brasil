'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

sexo = input('Indique seu sexo [M/F]: ').upper()
altura = float(input('Agora indique sua altura: '))
if sexo == 'F':
    print(f'Com {altura}m, sua altura ideal seria {(62.1 * altura) - 44.7:.2f}')
elif sexo == 'M':
    print(f'Com {altura}m, sua altura ideal seria {(72.7 * altura) - 58:.2f}')
else:
    print('Alguma coisa deu errado :/')
