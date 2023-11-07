'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma 
ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, 
informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa
não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''

print('=====EQUAÇÃO DE SEGUNDO GRAU=====')
a = 0
b = 0
c = 0
d = (b**2) - (4 * a * c)
raiz1 = -b + (d**(1/2)) / 2 * a
raiz2 = -b - (d**(1/2)) / 2 * a

a = int(input('Digite o valor de A: '))
if a == 0:
    print('A = 0. Não é uma equação de primeiro grau. Fim do programa.')
else:
    b = int(input('Digite o valor de b: '))
    c = int(input('digite o valor de c: '))
    d = (b**2) - (4 * a * c)
    raiz1 = -b + (d**(1/2)) / 2 * a
    raiz2 = -b - (d**(1/2)) / 2 * a
    if d < 0:
        print('A equação não possui raizes reais.')
    elif d == 0:
        print(f'A equação possui apenas uma raiz real: {raiz1:.2f}')
    elif d > 0:
        print(f'A equação possui duas raizes reais: {raiz1:.2f} e {raiz2:.2f}')

'''VOLTAR MAIS TARDE! Tem algo errado, mas não achei o que'''
