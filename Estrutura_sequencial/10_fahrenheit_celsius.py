'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

c = float(input('Digite a temperatura em graus Celsius: '))
f = (c - 32) * 5/9
print(f'{c}°C são {f:.2f}°F')