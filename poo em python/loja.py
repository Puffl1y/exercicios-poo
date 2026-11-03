class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto}' adicionado.")
   
    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            print(f"Produto '{produto}' removido.")
        else:
            print(f"Produto '{produto}' não encontrado no estoque.")

    def listar_produtos(self):
        print(f"Produtos na loja {self.nome}")
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            for i, prod in enumerate(self.produtos, 1):
                print(f"{i}. {prod}") 
