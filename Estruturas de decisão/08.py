p1 = float(input('Digite o preço do primeiro produto: R$'))
p2 = float(input('Digite o preço do segundo produto: R$'))
p3 = float(input('Digite o preço do terceiro produto: R$'))

if p1 < p2 and p1 < p3:
    print('O produto mais recomendável é o primeiro.')
elif p2 < p1 and p2 < p3:
    print('O produto mais recomendável é o segundo.')
elif p3 < p1 and p3 < p2:
    print('O produto mais recomendável é o terceiro.')