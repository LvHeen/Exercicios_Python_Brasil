'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota1 = float(input ('Primeira nota: '))
nota2 = float(input ('Segunda nota: '))
media = (nota1 + nota2) / 2

if media == 10:
    print('APROVADO COM DISTINÇÃO. Média final 10!')
elif media >= 7:
    print(f'APROVADO! Média final {media:.1f}')
if media <= 6:
    print(f'REPROVADO! Média final {media:.1f}')
