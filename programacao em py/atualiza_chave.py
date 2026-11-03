meu_dicionario = {'nome': 'Mariana', 'idade': 20}

#Atualizar chave que ja existe
meu_dicionario['idade'] = 25

#Atualizar chave que não existe
meu_dicionario['cidade'] = 'Brasília'

print(meu_dicionario)

# Quando a chave já existe o python sobrescreve o valor antigo pelo novo
# Quando a chave não existe ele cria uma nova entrada no dicionario, adicionando
# o novo par chave-valor