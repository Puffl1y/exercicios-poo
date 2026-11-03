class Quiz:
    def __init__(self):
        self.perguntas = []

    def adicionar_pergunta(self, enuciado, resposta_correta):
        self.perguntas.append({
            'enuciado': enuciado,
            'resposta_correta': resposta_correta
        })

    def calcular_pontuacao(self, respostas_usuario):
        pontuacao = 0
        for i, pergunta in enumerate(self.perguntas):
            if i < len(respostas_usuario):
                if str(respostas_usuario[i]).strip().lower() == str(pergunta['resposta_correta'].strip().lower()):
                    pontuacao += 1 
        return pontuacao

#Exemplo
quiz = Quiz()
quiz.adicionar_pergunta("Qual é a capital do Brasil?", "Brasília")
quiz.adicionar_pergunta("Quanto é 80 - 50?", "30")

respostas = ["Brasília", "30"]
pontos = quiz.calcular_pontuacao(respostas)
print(f"Pontuação do usuário: {pontos}") 
