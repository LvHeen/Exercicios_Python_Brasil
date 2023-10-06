n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'Entre os três {n1} é maior.')
elif n2 > n1 and n2 > n3:
    print(f'Entre todos {n2} é maior.')
elif n3 > n1 and n3 > n2:
    print(f'Entre todos {n3} é maior.')