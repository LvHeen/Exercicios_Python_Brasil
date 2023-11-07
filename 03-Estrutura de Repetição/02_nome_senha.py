'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

while True:
    nome = str(input('Nome de usuário: '))
    senha = input('Senha: ')
    if senha == nome:
        print('Erro! A senha não pode ser igual o nome de usuário. Tente novamente.')
    else: 
        break
print('Programa finalizado.')