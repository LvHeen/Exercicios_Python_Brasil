n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

if m > 9 and m < 10:
    print('Seu conceito foi A. APROVADO!')
if m > 7.5 and m < 9:
    print('Seu conceito foi B. APROVADO!')
if m > 6 and m < 7.5:
    print('Seu conceito foi C. APROVADO!')
if m > 4 and m < 6:
    print('Seu conceito foi D. REPROVADO!')
if m < 4:
    print('Seu conceiro foi E. REPROVADO!')