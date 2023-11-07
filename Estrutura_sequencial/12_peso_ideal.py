'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58'''

altura = float(input('Qual sua altura? '))
peso = (72.7 * altura) - 58
print(f'Se sua altura for {altura}m, seu peso ideal é {peso:.2f}')
