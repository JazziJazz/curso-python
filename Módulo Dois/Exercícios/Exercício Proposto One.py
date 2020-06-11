# Programa que lê um número inteiro, exibe na tela se ele for par ou impar mas se ele não for um inteiro retorna na tela o resultado informando que ele não é um inteiro.

num = float(input('Digite um número inteiro: '))

if (num // 1 == num): 
    if (num % 2 == 0):
        print(f'O número {num:.0f} é um número PAR.')
    else:
        print(f'O número {num:.0f} é um número IMPAR.')
else:
    print(f'O número {num:.1f} é invalido.')
