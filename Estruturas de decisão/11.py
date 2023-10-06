sal = float(input('Qual seu salário atual? R$'))

baixissimo = (sal * 20) / 100
baixo = (sal * 15) / 100
medio = (sal * 10) / 100
alto = (sal * 5) / 100

if sal <= 280:
    novo = sal + baixissimo
    print('-Percentual do ajuste: 20%')
elif sal > 280 and sal < 700:
    novo = sal + baixo
    print('-Percentual do ajuste: 15%')
elif sal > 701 and sal < 1500:
    novo = sal + medio
    print('-Percentual do ajuste: 10%')
else:
    novo = sal + alto
    print('-Percentual do ajuste: 5%')

print(f'-Sálario antes do reajuste: R${sal}')
print(f'-Valor do aumento: R${novo - sal}')
print(f'-Novo valor: R${novo}')