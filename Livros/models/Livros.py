class Livros:
    def __init__(self, titulo, autor, ano_publicado, num_pag, pag_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
        self.num_pag = num_pag
        self.pag_atual = pag_atual

    def avancar_pag(self):
        if self.pag_atual < self.num_pag:
            self.pag_atual += 1
            print(f"Você avançou para a página {self.pag_atual} do livro '{self.titulo}'")
        else:
            print(f"Você já está na última página do livro '{self.titulo}'")
    
    def voltar_pag(self):
        if self.pag_atual > 1:
            self.pag_atual -= 1
            print(f"Você voltou para a página {self.pag_atual} do livro '{self.titulo}'")
        else:
            print(f"Você já está na primeira página do livro '{self.titulo}'")
    
    def mostrar_infos(self):
        print(f"Livro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano Publicado: {self.ano_publicado}")
        print(f"Número de Páginas: {self.num_pag}")
        print(f"Página Atual: {self.pag_atual}")
