# Programa que pergunta as horas, exibe na tela a saudação apropriada. Bom dia 0-11, boa tarde 12-17, boa noite 18-23.

horas = int(input('Que horas são?: '))

if horas in range(0, 11):
    print('Bom dia.')

if horas in range(12, 17):
    print('Boa tarde.')

if horas in range(18, 23):
    print('Boa noite.')