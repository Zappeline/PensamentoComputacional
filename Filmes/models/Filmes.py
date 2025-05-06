class Filmes:
    def __init__(self, titulo, genero, duracao, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.avaliacao = avaliacao

    def avaliar(self, avaliacao):
        if 0 <= avaliacao <= 10:
            self.avaliacao = avaliacao
            print(f"Avaliação do filme '{self.titulo}' atualizada para {avaliacao}")
        else:
            print("Avaliação invalida, avaliação deve ser entre 0 e 10")

    def exibir_info(self):
        print(f"Título: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Duração: {self.duracao} minutos")
        print(f"Avaliação: {self.avaliacao}/10")    


