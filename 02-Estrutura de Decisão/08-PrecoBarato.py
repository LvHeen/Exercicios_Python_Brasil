'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

lista = {}
lista.update({
    'Produto 1': float(input('Digite o valor do primeiro produto: ')), 
    'Produto 2': float(input('Digite o valor do segundo produto: ')), 
    'Produto 3': float(input('Digite o valor do terceiro produto: '))
    })

print(f'A opção mais barata é o {min(lista, key=lista.get)}, custando {min(lista.values())}')
