'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

h = float(input('Altura de uma pessoa: '))
hom = (72.7 * h) - 58
mul = (62.1 * h) - 44.7
print ('Baseado nessa altura, o peso ideal seria: \n Para homem: {:.2f}kg\n Para mulher: {:.2f}kg' .forma(hom, mul))