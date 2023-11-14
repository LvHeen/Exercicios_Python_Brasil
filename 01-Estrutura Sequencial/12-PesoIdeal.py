'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''

h = float(input('Qual é a sua altura? '))
peso = (72.7 * h) - 58
print('Baseado na sua altura, o seu peso ideal é: {:.2f}' .format(peso))