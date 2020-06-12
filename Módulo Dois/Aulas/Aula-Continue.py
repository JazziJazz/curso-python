# Teste de continue com while e lações de repetições.

nomes = ['Rodrigo', 'Bruno', 'Florisval', 'Adriana', 'Guiomar', 'Roberto']

x = 0

while (x < len(nomes)):
    if (nomes[x] == 'Roberto'):
        x += 1
        continue  # Continue faz o laço de repetição pular uma vez. As instruções são puladas uma única vez quando o continue é utilizado. Nesse código, um bom explo é que quando na tabela o nome Roberto for encontrado as instruções seram puladas. 
    print(nomes[x])
    x += 1
