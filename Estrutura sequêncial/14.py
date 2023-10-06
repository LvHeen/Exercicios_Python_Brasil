peso = float(input('Peso do peixe em kg: '))
excesso = peso - 50
multa = 4 * excesso

if peso < 50:
    print('O peixe está dentro dos limites.')
else:
    print(f'O peixe excedeu {excesso}kg do peso permitido. Sua multa será de R${multa:.2f}')