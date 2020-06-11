# Programa que lê o nome de um usuário, se tiver quatro letras ou menos imprima que o nome é curto, se tiver entre quatro e oito letras imprima que o nome é normal, e se tiver mais que oito letras imprima que o nome é grande.

name = input('Qual é o seu nome?: ')

if (len(name) <= 4):
    print('O seu nome é CURTO.')
elif (len(name) <= 8):
    print('O seu nome é NORMAL.')

if (len(name) > 8):
    print('O seu nome é GRANDE.')
