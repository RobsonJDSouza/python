
# """ Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""
while True:
    usuario = input('Nome de usuário: ')
    senha = input('Qual a senha? ')
    if usuario != senha:
        break
    print('Digite uma senha diferente do usuário')
print(f'Seu nome de usuário {usuario} e senha é {senha}')