class Filme:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

class Streaming:
    def __init__(self):
        self.acervo = []

    def adicionar_filmes(self, titulo, genero):
        novo_filme = Filme(titulo, genero)
        self.acervo.append(novo_filme)
        print(f"Filme '{titulo}' adicionado.")

    def listar_por_genero(self, genero_buscado):
        print(f"Filmes do genero: {genero_buscado}")
        encontrados = [f.titulo for f in self.acervo if f.genero.lower() == genero_buscado.lower()]

        if encontrados:
            for titulo in encontrados:
                print(f"- {titulo}")
        else:
            print("Nenhum filme encontrado para este genero.")