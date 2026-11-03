class Impressora:
    def imprimir(self, texto):
        print(f"[IMPRESSÃO]: {texto}")

class Relatorio:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def gerar_e_imprimir(self):
        impressora = Impressora()
        mensagem = f"{self.titulo} \n{self.conteudo}"
        impressora.imprimir(mensagem)

#Exemplo
relatorio = Relatorio("Relatório Abril", "Foi um bom mes para vendas")
relatorio.gerar_e_imprimir()