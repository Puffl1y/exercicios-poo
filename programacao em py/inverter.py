dicionario_original = {'a': 1, 'b': 2, 'c': 3}

dicionario_invertido = {valor: chave for chave, valor in dicionario_original.items()}

print("Dicionário original:", dicionario_original)
print("Dicionário invertido:", dicionario_invertido)