itens = ['mouse', 'teclado', 'cadeira', 'mouse', 'monitor', 'cadeira']
contagem = {}

for item in itens:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1

print(contagem)