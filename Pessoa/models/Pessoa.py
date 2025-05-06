class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def aniversario(self):
        print(f"Parabéns {self.nome}, hoje é seu aniversário! Você agora tem {self.idade + 1} anos.")
        self.idade += 1
    
    def crescer(self, altura: float):
        self.altura += altura
        print(f"{self.nome} cresceu {altura} metros e agora tem {self.altura} metros de altura.")
    
    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Altura: {self.altura} metros")
       