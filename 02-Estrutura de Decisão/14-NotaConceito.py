'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

from time import sleep

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
sleep(0.5)
if m >= 9.0 and m <= 10:
    print(f'Sua média foi {m}')
    print('Seu conceito foi A')
    print('APROVADO!')
elif m >= 7.5 and m <= 9.0:
    print(f'Sua média foi {m}')
    print('Seu conceito foi B')
    print('APROVADO')
elif m >= 6.5 and m <= 7.5:
    print(f'Sua média foi: {m}')
    print('Seu conceito foi C')
    print('APROVADO')
elif m >= 4 and m <= 6.0:
    print(f'Sua média foi: {m}')
    print('Seu conceito foi D')
    print('REPROVADO')
elif m < 4:
    print(f'Sua média foi {m}')
    print('Seu conceito foi E')
    print('REPROVADO')
else:
    print('Ops, algo deu errado... Verifique os dados e tente de novo')