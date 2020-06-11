# Programa que lê o nome, idade e peso de uma pessoa. Obter o IMC dessa pessoa, e ano em que ela nasceu.
import datetime, time

ano = datetime.datetime.now()
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
nome = input('Digite seu nome: ')

imc = peso / (altura * altura)
datanasc = ((ano.year) - idade)

print(f'Você nasceu no ano de {datanasc}. O seu IMC é de {imc:.2f}.')
