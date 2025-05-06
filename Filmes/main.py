from models.Filmes import Filmes

Avatar = Filmes(titulo="Avatar - O mestre do ar", genero="Ficção Científica", duracao=162, avaliacao=8.5)
Avatar.exibir_info()
Avatar.avaliar(9.0)
Avatar.exibir_info()
Avatar.avaliar(11)  # Teste com avaliação inválida
Avatar.avaliar(-1)  # Teste com avaliação inválida
Avatar.avaliar(10)  # Teste com avaliação válida
Avatar.exibir_info()

